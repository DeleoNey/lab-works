import httpx
from fastapi import APIRouter, HTTPException
from backend.config import GEO_DB_API_KEY
from backend.api.routes.utils import build_city_query

information_router = APIRouter(include_in_schema=True)

GEO_DB_API_URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"


@information_router.get("/city/")
async def get_city_info(city: str):
    """Returns city info from GeoDB Cities API.

    Args:
        city (str): Name of the city to fetch information for.

    Returns:
        city_info (dict~json): City information from GeoDB API.
    """
    url = build_city_query(base_url=GEO_DB_API_URL, city=city)
    headers = {"X-RapidAPI-Key": GEO_DB_API_KEY}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        # Перевіряємо статус відповіді API
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="City not found")

        city_info = response.json()
    return city_info
