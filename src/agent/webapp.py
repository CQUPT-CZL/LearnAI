# ./src/agent/webapp.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

@asynccontextmanager
async def lifespan(app: FastAPI):
    # for example...
    engine = create_async_engine("postgresql+asyncpg://user:pass@localhost/db")
    # Create reusable session factory
    async_session = sessionmaker(engine, class_=AsyncSession)
    # Store in app state
    app.state.db_session = async_session
    yield
    # Clean up connections
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

# ... can add custom routes if needed.