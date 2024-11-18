from typing import Optional
from pydantic import BaseModel
from beanie import Document, PydanticObjectId, init_beanie
from backend.config import client


class CitySchema(BaseModel):
    name: str
    population: int
    country: str
    region: str
    latitude: float
    longitude: float

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Kyiv",
                "population": 2900000,
                "country": "Ukraine",
                "region": "Kyiv Region",
                "latitude": 50.4501,
                "longitude": 30.5236
            }
        }


class CityReportInDB(Document):
    name: str
    population: int
    country: str
    region: str
    latitude: float
    longitude: float

    class Settings:
        name = "cityReport"

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "name": "Kyiv",
                "population": 2900000,
                "country": "Ukraine",
                "region": "Kyiv Region",
                "latitude": 50.4501,
                "longitude": 30.5236
            }
        }


class CityResponse(CitySchema):
    id: Optional[PydanticObjectId] = None


async def init():
    await init_beanie(
        database=client.db_name,
        document_models=[CityReportInDB]
    )