from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from .database import Base

# class Location(Base):
#     __tablename__ = "locations"
#     id = Column(Integer, primary_key=True)
#     location = Column(String)

#     weather_data = relationship("WeatherData", back_populates="location")

class WeatherData(Base):
    __tablename__ = "weather_data"
    
    id = Column(Integer, primary_key=True)
    
    # location_id = Column(Integer, ForeignKey("locations.id"))
    # location = relationship("Location", back_populates="weather_data")
    location = str
    temperature = Column(Float)
    temperature_feels_like = Column(Float)
    temperature_min = Column(Float)
    temperature_max = Column(Float)
    humidity = Column(Float)
    wind = Column(Float)
    pressure = Column(Float)
    description = Column(String(255), nullable=True)
    timestamp = Column(DateTime)
    # weather_alerts = relationship("WeatherAlert", secondary="weather_data_weather_alert", back_populates="weather_data")

# weather_data_weather_alert = Table(
#     "weather_data_weather_alert",
#     Base.metadata,
#     Column("weather_data_id", Integer, ForeignKey("weather_data.id")),
#     Column("weather_alert_id", Integer, ForeignKey("weather_alert.id"))
# )

# class WeatherAlert(Base):
#     __tablename__ = "weather_alerts"
#     id = Column(Integer, primary_key=True)
#     alert = Column(String(255))

#     weather_data = relationship("WeatherData", secondary=weather_data_weather_alert, back_populates="weather_alerts")



