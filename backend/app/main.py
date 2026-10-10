from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.db import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables (dev convenience — use Alembic in production)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: dispose engine
    await engine.dispose()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Threat Intelligence Platform API",
    lifespan=lifespan,
)


@app.get("/health", tags=["health"])
async def health_check():
    """Liveness / readiness probe."""
    return {"status": "ok", "version": settings.VERSION}
