import asyncio
from backend.api.routes.city.current import get_city_info

result_coroutine = get_city_info(city="Lviv")
result = asyncio.run(result_coroutine)

print(result)
