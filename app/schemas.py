from pydantic import BaseModel
from typing import List, Optional

class LocationBase(BaseModel):
    int: int
    location: str

class WeatherBase(BaseModel):
    location: LocationBase

class WeatherCreate(WeatherBase):
    pass

class WeatherResponse(WeatherBase):
    id: Optional[int]
    location: str
    # weather_id: int
    temperature: float
    temperature_feels_like: float
    temperature_min: float
    temperature_max: float
    humidity: float
    wind: float
    pressure: float
    timestamp: int
    # weather_alerts: List[str]

    class config():
        orm_mode = True