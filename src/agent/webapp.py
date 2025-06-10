# ./src/agent/webapp.py

# 标准库导入
import os
from contextlib import asynccontextmanager

# 第三方库导入
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import HumanMessage
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# 本地应用导入
from src.agent.my_agent import graph

class ChatMessage(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    status: str = "success"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # for example...
    # engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
    # Create reusable session factory
    # async_session = sessionmaker(engine, class_=AsyncSession)
    # Store in app state
    # app.state.db_session = async_session
    yield
    # Clean up connections
    # await engine.dispose()

app = FastAPI(title="LearnAI API", lifespan=lifespan)

# 挂载静态文件目录
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """返回前端页面"""
    # 优先使用Vue3版本的前端
    vue3_frontend_file = os.path.join(frontend_path, "index-vue3.html")
    if os.path.exists(vue3_frontend_file):
        with open(vue3_frontend_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    
    # 备用原版前端
    frontend_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(frontend_file):
        with open(frontend_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    
    return HTMLResponse(content="<h1>LearnAI Frontend Not Found</h1>")

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(chat_message: ChatMessage):
    """处理聊天消息"""
    try:
        user_message = chat_message.message
        
        # 使用真实的agent处理消息
        # 创建消息状态
        initial_state = {
            "messages": [HumanMessage(content=user_message)]
        }
        
        # 调用agent图
        result = graph.invoke(initial_state)
        
        # 获取AI响应
        ai_response = result["messages"][-1].content
        
        return ChatResponse(response=ai_response)
    
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return JSONResponse(
            status_code=500,
            content={"response": "抱歉，处理你的请求时出现了错误。请检查API配置。", "status": "error"}
        )

@app.get("/api/health")
async def health_check():
    """健康检查端点"""
    return {"status": "healthy", "message": "LearnAI API is running"}