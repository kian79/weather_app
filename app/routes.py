from fastapi import APIRouter, Depends
from .schemas import WeatherCreate, WeatherResponse
from .models import WeatherData
from fastapi_cache.decorator import cache
import dotenv
import requests
import os

dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric"

router = APIRouter()

def is_weather_id_alert(weather_id:int) -> bool:
    if weather_id > 232 or weather_id < 200:
        return True
    return False

@router.get("/weather/{location}", response_model=WeatherResponse)
@cache(expire=60)
async def get_weather(location: str):
    
    response = requests.get(API_URL.format(location, API_KEY))
    data = response.json()
    main_data = data["main"]
    wind_data = data["wind"]
    timestamp = data["dt"]
    weather_id = data["weather"][0]["id"]
    weather_alerts = []
    

    
    # location_obj = Location(location=location)
    weather_data = WeatherData(
        location=location,
        weather_id = weather_id,
        temperature=main_data["temp"],
        temperature_feels_like=main_data["feels_like"],
        temperature_min=main_data["temp_min"],
        temperature_max=main_data["temp_max"],
        humidity=main_data["humidity"],
        wind=wind_data["speed"],
        pressure=main_data["pressure"],
        timestamp=timestamp,

    )
    return weather_data


