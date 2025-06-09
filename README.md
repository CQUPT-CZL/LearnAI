# 🤖 LearnAI 项目

<p align="center">
    <img src="static/logo.png" alt="LearnAI Logo"/>
</p>

<p align="center">
    <strong>🚀 基于 LangGraph 的智能 AI 助手平台</strong>
</p>

## 📖 项目简介

LearnAI 是一个现代化的人工智能学习和开发平台，基于 LangGraph 框架构建。项目提供了完整的 AI Agent 开发环境，包括前端聊天界面、后端 API 服务和智能对话功能。

### ✨ 主要特性

- 🎯 **智能对话**: 基于 LangGraph 的状态图管理，支持复杂对话流程
- 🌐 **Web 界面**: 现代化的聊天界面，支持实时对话
- 🔧 **工具集成**: 可扩展的工具系统，支持自定义功能
- 📊 **状态管理**: 完善的对话状态跟踪和管理
- 🚀 **快速部署**: 支持多种启动方式，开发和生产环境友好

## 📁 项目结构

```
LearnAI/
├── README.md              # 项目说明文档
├── langgraph.json          # LangGraph 配置文件
├── main.py                 # 主程序入口
├── pyproject.toml          # 项目依赖配置
├── frontend/               # 前端文件
│   └── index.html         # 聊天界面
├── src/                   # 源代码目录
│   └── agent/             # AI Agent 核心模块
│       ├── __init__.py
│       ├── my_agent.py    # Agent 主逻辑
│       ├── webapp.py      # FastAPI Web 应用
│       └── utils/         # 工具模块
│           ├── __init__.py
│           ├── nodes.py   # 节点定义
│           ├── state.py   # 状态管理
│           └── tools.py   # 工具集合
├── static/                # 静态资源
│   └── logo.png          # 项目 Logo
├── test/                  # 测试文件
│   └── test_cal_model.py
└── uv.lock               # 依赖锁定文件
```

## 🛠️ 技术栈

- **框架**: LangGraph + FastAPI
- **语言**: Python 3.11+
- **前端**: HTML5 + CSS3 + JavaScript
- **包管理**: uv
- **AI 集成**: LangChain + OpenAI
- **数据库**: SQLAlchemy (支持异步)

## 📦 安装指南

### 环境要求
- Python 3.11 或更高版本
- uv 包管理器

### 安装步骤

1. **克隆项目**
   ```bash
   git clone <repository-url>
   cd LearnAI
   ```

2. **安装依赖**
   ```bash
   uv sync
   ```

3. **环境配置**
    ```bash
    # 复制环境配置文件
    cp .env.example .env
    ```
    
    然后编辑 `.env` 文件，将 `OPENAI_API_KEY` 替换为你的实际 API 密钥：
    ```bash
    # 编辑配置文件
    nano .env
    # 或使用其他编辑器
    code .env
    ```
    
    **⚠️ 重要**: 请确保将 `sk-your-openai-api-key-here` 替换为你从 [OpenAI 官网](https://platform.openai.com/api-keys) 获取的真实 API 密钥！

## 🚀 使用说明

### 启动方式

#### 方式一：LangGraph 开发模式（推荐）
```bash
langgraph dev --allow-blocking
```

#### 方式二：直接启动 Web 服务
```bash
uvicorn src.agent.webapp:app --reload --host 0.0.0.0 --port 8000
```


### 访问应用

启动成功后，在浏览器中访问：
- **Web 界面**: http://localhost:8000
- **API 文档**: http://localhost:8000/docs

### 配置说明

- **LangGraph 配置**: `langgraph.json` - 定义图结构和应用配置
- **项目依赖**: `pyproject.toml` - Python 包依赖管理
- **环境变量**: `.env` - API 密钥和环境配置

## 🔧 开发指南

### 项目架构

- **Agent 核心**: `src/agent/my_agent.py` - 基于 LangGraph 的状态图
- **Web 服务**: `src/agent/webapp.py` - FastAPI 应用
- **工具模块**: `src/agent/utils/` - 节点、状态、工具定义
- **前端界面**: `frontend/index.html` - 聊天界面

### 扩展功能

1. **添加新工具**: 在 `src/agent/utils/tools.py` 中定义
2. **修改对话流程**: 编辑 `src/agent/my_agent.py` 中的状态图
3. **自定义界面**: 修改 `frontend/index.html`

## 🤝 贡献指南

我们欢迎所有形式的贡献！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系我们

如有问题或建议，请通过以下方式联系：

- 📧 Email: your-email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/your-username/LearnAI/issues)

---

<p align="center">
    Made with ❤️ by LearnAI Team
</p>

