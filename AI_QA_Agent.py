# 基础
from dotenv import load_dotenv
import os

# --- 核心修改：使用 LangChain 1.x 最新的 create_agent 接口 ---
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

# 基础组件
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser

# 记忆 + 联网工具
from langchain_classic.memory import ConversationBufferMemory  
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools.retriever import create_retriever_tool

# 大模型和 Embeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# 如果当前目录下没有 doc.txt，就自动创建一个并写入测试内容
if not os.path.exists("doc.txt"):
    with open("doc.txt", "w", encoding="utf-8") as f:
        f.write("这是自动生成的测试文档。\nLangChain的RAG检索测试成功！\n")
# 1. 加载环境
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# 2. 初始化双模型
llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen3-vl-32b-thinking",
    temperature=0.1
)

embeddings = OpenAIEmbeddings(
    api_key=api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="text-embedding-v3", # 显式指定阿里云的 Embedding 模型,
    check_embedding_ctx_length=False  # 加上这一行，禁止 LangChain 提前做 token 检查
)

# 3. 本地文档RAG流水线
loader = TextLoader("doc.txt", encoding="utf-8")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
split_docs = splitter.split_documents(docs)
vector_store = Chroma.from_documents(documents=split_docs, embedding=embeddings)
retriever = vector_store.as_retriever()

# 4. 把RAG检索器包装成「Agent可用的工具」
retriever_tool = create_retriever_tool(
    retriever,
    name="company_knowledge_search",
    description="用来查询公司内部业务文档、私有知识库相关问题"
)

# 5. 联网搜索工具
search_tool = TavilySearchResults(k=3)

# 6. 把两个工具放一起
tools = [retriever_tool, search_tool]

# 7. 初始化短期记忆
memory = ConversationBufferMemory(return_messages=True)

# 8. 直接用纯字符串定义 Agent 的系统提示词
system_prompt = """
你有两个工具可以使用：
1. company_knowledge_search：查公司内部私有文档、业务知识
2. tavily_search_results_json：查实时新闻、外网最新信息
请自己判断调用哪个工具，不知道就如实回答，不要编造。
"""
# 9. 创建Agent (使用最新的 create_agent)
agent = create_agent(
    model=llm, 
    tools=tools, 
    system_prompt=system_prompt
)

# 多轮测试
if __name__ == "__main__":
    while True:
        user_q = input("你想问：")
        if user_q == "exit":
            break
        
        # 获取历史消息
        chat_history = memory.load_memory_variables({})["history"]
        
        # --- 核心修改：新版 invoke 必须传入标准的 messages 列表 ---
        messages = []
        # 把历史对话拼接到 messages 里
        for msg in chat_history:
            if msg.type == 'human':
                messages.append(HumanMessage(content=msg.content))
            else:
                messages.append({"role": "assistant", "content": msg.content})
        
        # 加入当前用户的提问
        messages.append(HumanMessage(content=user_q))
        
        # 调用新版 Agent
        res = agent.invoke({"messages": messages})
        
        # --- 核心修改：新版返回结果在 result["messages"] 的最后一条 ---
        ai_output = res["messages"][-1].content
        print("AI回答：", ai_output)
        
        # 手动保存历史
        memory.save_context({"input": user_q}, {"output": ai_output})
        print("-" * 50)