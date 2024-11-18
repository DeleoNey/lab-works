from urllib.parse import urlencode
import os
from backend.config import GEO_DB_API_KEY


def build_city_query(base_url: str, city: str) -> str:
    request_data = {
        "namePrefix": city,
        "limit": 1,
        "apiKey": GEO_DB_API_KEY,
    }
    url_values = urlencode(request_data)
    return f"{base_url}?{url_values}"
