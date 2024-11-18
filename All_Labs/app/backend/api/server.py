from fastapi import FastAPI
from contextlib import asynccontextmanager
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from backend.api.routes import router as main_router
from backend.api.city_controller import router as city_router
from backend.models.city_models import CityReportInDB
from backend.config import MONGODB_URL, MONGO_DATABASE
from backend.db.database import client

client = AsyncIOMotorClient(MONGODB_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for managing the application lifecycle
    """
    try:
        await init_beanie(
            database=client[MONGO_DATABASE],
            document_models=[CityReportInDB]
        )
        print("Connected to MongoDB")

        yield
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise
    finally:
        client.close()
        print("Closed MongoDB connection")


def create_app() -> FastAPI:
    """
    Factory for creating a FastAPI application
    """
    app = FastAPI(
        title="City Report API",
        description="API for managing city information",
        version="1.0.0",
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc"
    )

    app.include_router(main_router, prefix="/api")
    app.include_router(city_router, prefix="/api/cities", tags=["cities"])

    return app


app = create_app()


@app.get("/health")
async def health_check():
    return {"status": "healthy"}