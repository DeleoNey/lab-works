import os
from dotenv import load_dotenv
import motor.motor_asyncio

load_dotenv()

GEO_DB_API_KEY="smth"
MONGODB_HOST="localhost"
MONGODB_PORT="27017"
MONGO_DATABASE="city"
MONGODB_USERNAME="deleon"
MONGODB_PASSWORD="deleon"
MONGODB_URL = f"mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}/{MONGO_DATABASE}" \
              f"?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.get_database()
