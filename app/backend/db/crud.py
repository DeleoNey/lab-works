from backend.models.city_models import CitySchema, CityReportInDB
from pymongo.errors import DuplicateKeyError
from typing import Optional, List


async def create_city(city_data: CitySchema) -> CityReportInDB:
    """
    Creates a new record for a city

    Args:
        city_data: City data in the CitySchema format

    Returns:
        CityReportInDB: The created city document

    Raises:
        DuplicateKeyError: If a city with this name already exists
    """

    existing_city = await CityReportInDB.find_one(CityReportInDB.name == city_data.name)
    if existing_city:
        raise DuplicateKeyError(f"City {city_data.name} already exists in the database")

    city_doc = CityReportInDB(**city_data.model_dump())

    await city_doc.insert()
    return city_doc


async def get_city_by_name(city_name: str) -> CityReportInDB:
    """
    Retrieves a city by name

    Args:
        city_name: The name of the city

    Returns:
        Optional[CityReportInDB]: The found city or None
    """
    return await CityReportInDB.find_one(CityReportInDB.name == city_name)


async def get_all_cities() -> list[CityReportInDB]:
    """
    Retrieves all cities

    Returns:
        List[CityReportInDB]: A list of all cities
    """
    return await CityReportInDB.find_all().to_list()

async def update_city(city_name: str, city_data: CitySchema) -> Optional[CityReportInDB]:
    """
    Updates city information

    Args:
        city_name: The name of the city to update
        city_data: The new city data

    Returns:
        Optional[CityReportInDB]: The updated city or None
    """
    city = await CityReportInDB.find_one(CityReportInDB.name == city_name)
    if city:
        await city.update({"$set": city_data.model_dump(exclude_unset=True)})
        await city.fetch()
        return city
    return None


async def delete_city(city_name: str) -> bool:
    """
    Deletes a city from the database

    Args:
        city_name: The name of the city to delete

    Returns:
        bool: True if the city was deleted, False if the city was not found
    """
    city = await CityReportInDB.find_one(CityReportInDB.name == city_name)
    if city:
        await city.delete()
        return True
    return False


async def get_cities_by_country(country: str) -> List[CityReportInDB]:
    """
    Retrieves all cities in a specified country

    Args:
        country: The name of the country

    Returns:
        List[CityReportInDB]: A list of cities in the specified country
    """
    return await CityReportInDB.find(CityReportInDB.country == country).to_list()


async def get_cities_by_population_range(min_pop: int, max_pop: int) -> List[CityReportInDB]:
    """
    Retrieves cities within a specified population range

    Args:
        min_pop: The minimum population
        max_pop: The maximum population

    Returns:
        List[CityReportInDB]: A list of cities within the specified population range
    """
    return await CityReportInDB.find(
        CityReportInDB.population >= min_pop,
        CityReportInDB.population <= max_pop
    ).to_list()