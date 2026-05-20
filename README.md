```markdown
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
```

### 2. 安装依赖

建议使用虚拟环境（venv 或 conda）：

```bash
pip install langchain langchain-community langchain-openai langchain-classic chromadb python-dotenv tiktoken requests tavily-python
```

### 3. 配置 API 密钥

在项目根目录创建 `.env` 文件，填入以下内容：

```env
DASHSCOPE_API_KEY=你的阿里云通义千问API Key
TAVILY_API_KEY=你的Tavily API Key
```

> 获取方式：
> - 阿里云 DashScope API Key：[https://dashscope.console.aliyun.com/](https://dashscope.console.aliyun.com/)
> - Tavily API Key：[https://tavily.com/](https://tavily.com/)

### 4. 准备本地文档

默认读取项目根目录下的 `doc.txt` 文件。如果文件不存在，程序会自动创建一个测试文档。

你也可以替换或修改 `doc.txt` 的内容（支持 UTF-8 编码）。

## 运行

```bash
python main.py
```

然后在终端输入问题，输入 `exit` 退出程序。

## 使用示例

```
你想问：我们公司的文档里写了什么？
AI回答：根据文档内容，里面提到了“LangChain的RAG检索测试成功！”...

你想问：今天上海的天气怎么样？
AI回答：今天上海多云，气温18-25℃...（来自Tavily搜索）

你想问：刚才我第一个问题问了什么？
AI回答：你问了“我们公司的文档里写了什么？”
```

## 代码结构

```
.
├── main.py              # 主程序入口
├── doc.txt              # 本地知识库文档（可替换）
├── .env                 # API 密钥配置（需自行创建，不提交到 Git）
├── requirements.txt     # 依赖列表（可选）
└── README.md            # 项目说明
```

## 注意事项

- 确保 API 密钥有效且账户有足够余额。
- 首次运行会自动创建 `doc.txt` 测试文件。
- 由于使用 LangChain 1.x 新接口，`create_agent` 需要 langchain>=1.0.0。

## 后续改进方向

- [ ] 支持上传多种格式（PDF、Word、Markdown）
- [ ] 增加 Web 界面（Streamlit / Gradio）
- [ ] 添加对话历史持久化存储
- [ ] 支持更多搜索引擎（如 Bing、Google）

## 许可证

MIT License

## 联系作者

- GitHub: [你的用户名](https://github.com/你的用户名)
- 邮箱: [你的邮箱]
```

---

## 3. 建议同时创建 `requirements.txt`

为了让别人方便运行，请在你的项目根目录创建 `requirements.txt`，内容如下：

```
langchain>=1.0.0
langchain-community>=0.3.0
langchain-openai>=0.3.0
langchain-classic>=0.1.0
chromadb>=0.5.0
python-dotenv>=1.0.0
tiktoken>=0.7.0
tavily-python>=0.5.0
```

---

## 4. 别忘了 `.gitignore`

在项目根目录创建 `.gitignore`，至少包含：

```
.env
__pycache__/
*.pyc
chroma/
.DS_Store
venv/
.idea/
```

---


需要我帮你把这段项目描述按照你现有简历的格式（日期、项目名称、项目描述、GitHub链接）完整写出来吗？这样你可以直接复制粘贴到简历中。
