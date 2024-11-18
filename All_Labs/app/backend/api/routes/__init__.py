from fastapi import APIRouter
from backend.api.routes.city.current import current_router
from backend.api.routes.city.information import information_router

router = APIRouter()


router.include_router(current_router, prefix="", tags=["current_city"], include_in_schema=True)
router.include_router(information_router, prefix="", tags=["city_forecast"], include_in_schema=True)

# router.include_router(city_router, prefix="", tags=["current_city"], include_in_schema=True)