from motor.motor_asyncio import AsyncIOMotorClient
from backend.config import MONGODB_URL
from beanie import init_beanie
from backend.models.city_models import CitySchema

client = AsyncIOMotorClient(MONGODB_URL)
db = client.get_database()
city_collection = db.city_collection

async def init():
    await init_beanie(database=client.get_database(), document_models=[CitySchema])