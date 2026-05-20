# 企业智能知识库问答 Agent

基于 LangChain 和通义千问大模型构建的智能问答 Agent，集成本地文档检索（RAG）与 Tavily 实时联网搜索，支持多轮对话记忆，能够自主判断调用哪个工具来回答用户问题。

## 功能特点

- 📚 **私有知识库问答**：上传本地文档（`doc.txt`），通过 RAG 技术检索相关内容进行回答
- 🌐 **实时联网搜索**：集成 Tavily Search API，获取最新的互联网信息
- 🧠 **智能工具选择**：Agent 根据用户问题自动判断调用检索器还是搜索引擎
- 💬 **多轮对话记忆**：使用 `ConversationBufferMemory` 维持对话上下文
- 🚀 **基于 LangChain 1.x**：使用最新的 `create_agent` 接口，代码简洁易扩展

## 技术栈

| 类别 | 技术 |
|------|------|
| 大模型 | 通义千问 (qwen3-vl-32b-thinking) |
| Embedding | 阿里云 text-embedding-v3 |
| 框架 | LangChain 1.x |
| 向量数据库 | Chroma |
| 联网搜索 | Tavily Search API |
| 文档加载 | TextLoader |
| 文本分割 | CharacterTextSplitter |
| 记忆管理 | ConversationBufferMemory |

## 安装与配置

### 1. 克隆仓库

```bash
git clone https://github.com/你的用户名/你的仓库名.git
cd 你的仓库名
