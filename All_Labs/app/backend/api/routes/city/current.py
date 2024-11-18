import httpx
from fastapi import APIRouter, HTTPException
from backend.db.crud import *  # Функції роботи з БД вже є
from backend.config import GEO_DB_API_KEY
from backend.models.city_models import CitySchema  # Ваші моделі з Pydantic

# Ініціалізація роутера
current_router = APIRouter(include_in_schema=True)

GEO_DB_API_URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"

HEADERS = {
    "X-RapidAPI-Key": GEO_DB_API_KEY,
}

def build_city_query(city: str):
    return f"{GEO_DB_API_URL}?namePrefix={city}"

@current_router.get("/current/")
async def get_city_info(city: str):
    """Returns city info from GeoDB API."""
    url = build_city_query(city=city)
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="City not found")

        city_info = response.json()

    return city_info


@current_router.post("/current", response_model=CitySchema)
async def create_city_report(report: CitySchema):
    """Creates a new city report (stores city info)."""
    city_info = await get_city_info(city=report.name)  # Отримуємо інформацію з GeoDB

    if city_info is None:
        raise HTTPException(404, "City not found")

    city_report = await get_city_by_name(city=report.name)
    if city_report is not None:
        raise HTTPException(409, "The city report already exists")

    city_report = await create_city(city=report)
    return city_report


@current_router.get("/current/{city}", response_model=CitySchema)
async def get_weather_by_city(city: str):
    """Get city report by city name."""
    city_report = await get_city_by_name(city=city)
    if city_report is None:
        raise HTTPException(404, "The report for the city is not found")
    return city_report


@current_router.get("/current/all/", response_model=List[CitySchema])
async def get_all_reports():
    """Get all city reports."""
    city_reports = await get_all_cities()
    if not city_reports:
        raise HTTPException(404, "Database is empty")
    return city_reports


@current_router.put("/current/", response_model=CitySchema)
async def update_report(report: CitySchema):
    """Update an existing city report."""
    city_report = await update_city(city=report)
    if city_report is None:
        raise HTTPException(404, "There was an error updating the city report.")
    return city_report

@current_router.post("/city")
async def create_city(city: CitySchema):
    """Creates a new city in the database."""
    return {"message": "City created successfully", "city": city}


@current_router.delete("/city/{city_name}", response_model=CitySchema)
async def delete_city(city_name: str):
    """Deletes a city by its name."""
    city = await get_city_by_name(city=city_name)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")

    deleted_city = await delete_city(city_name=city_name)
    if deleted_city:
        return {"message": f"City {city_name} deleted successfully", "city": city}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete city")
