from fastapi import APIRouter, HTTPException
from pymongo.errors import DuplicateKeyError
from backend.models.city_models import CitySchema, CityReportInDB
from backend.db import crud

router = APIRouter()

@router.post("/add_city/", response_model=CityReportInDB)
async def add_city(city: CitySchema):
    try:
        city_report = await crud.create_city(city)
        return city_report
    except DuplicateKeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding city: {str(e)}")

@router.get("/cities/", response_model=list[CityReportInDB])
async def get_cities():
    return await crud.get_all_cities()

@router.get("/city/{city_name}", response_model=CityReportInDB)
async def get_city(city_name: str):
    city = await crud.get_city_by_name(city_name)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.put("/city/{city_name}", response_model=CityReportInDB)
async def update_city(city_name: str, city_data: CitySchema):
    updated_city = await crud.update_city(city_name, city_data)
    if not updated_city:
        raise HTTPException(status_code=404, detail="City not found")
    return updated_city

@router.delete("/city/{city_name}")
async def delete_city(city_name: str):
    deleted = await crud.delete_city(city_name)
    if not deleted:
        raise HTTPException(status_code=404, detail="City not found")
    return {"message": f"City {city_name} successfully deleted"}

@router.get("/cities/country/{country}", response_model=list[CityReportInDB])
async def get_cities_by_country(country: str):
    return await crud.get_cities_by_country(country)

@router.get("/cities/population/", response_model=list[CityReportInDB])
async def get_cities_by_population(min_pop: int, max_pop: int):
    return await crud.get_cities_by_population_range(min_pop, max_pop)