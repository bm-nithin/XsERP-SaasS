from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import async_engine as engine
from api.v1.endpoints.erp.purchase.purchase import router as user_router
from middleware.auth_middleware import AuthMiddleware
from middleware.exception_middleware import exception_handler
from logging import logger
from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        print("Fastapi Engine Started")
        # await conn.run_sync(Base.metadata.create_all)  # ✅ Auto-create tables
    yield  # ✅ App Starts
    await engine.dispose()  # ✅ Closes DB connection on shutdown

# ✅ Create FastAPI App with Docs
app = FastAPI(
    title="FastAPI PostgreSQL App",
    description="API documentation for our FastAPI project",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc UI
    openapi_url="/openapi.json"  # OpenAPI Schema
)

app.add_middleware(AuthMiddleware)
app.add_exception_handler(Exception, exception_handler)

# ✅ Include API Routers
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])


@app.get("/")
async def root():
    return {"message": "FastAPI with PostgreSQL!"}


@app.get("/health")
def health_check():
    return {"status": "ok", "version": settings.CURRENT_VERSION}
