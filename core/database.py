from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# MYSQL_URL = (f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:"
#              f"{settings.MYSQL_PORT}/{settings.MYSQL_DBNAME}?charset=utf8mb4")

# Create an async engine for MySQL
async_engine = create_async_engine(
    settings.DATABASE_URL,  # Example: "mysql+aiomysql://user:password@host:port/dbname"
    future=True,
    echo=True,
    pool_recycle=3600,
    pool_pre_ping=True,
)

# Create an async session factory
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Dependency Injection for Async DB Session
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
