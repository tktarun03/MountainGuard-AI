from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field

class BaseReading(BaseModel):
    sensor_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    quality: float = Field(default=1.0, ge=0.0, le=1.0)

class GNSSReading(BaseReading):
    sensor_type: Literal["gnss"] = "gnss"
    latitude: float
    longitude: float
    displacement_mm: float
    velocity_mm_day: float
    acceleration_mm_day2: float

class SeismicReading(BaseReading):
    sensor_type: Literal["seismic"] = "seismic"
    rms: float = Field(ge=0.0)
    peak_amplitude: float = Field(ge=0.0)
    dominant_frequency_hz: float = Field(ge=0.0)
    duration_sec: float = Field(ge=0.0)

class WeatherReading(BaseReading):
    sensor_type: Literal["weather"] = "weather"
    temperature_c: float
    humidity_pct: float = Field(ge=0.0, le=100.0)
    rainfall_mm_hr: float = Field(ge=0.0)
    wind_speed_mps: float = Field(ge=0.0)
    freeze_thaw_index: float = Field(ge=0.0, le=1.0)

class RiverReading(BaseReading):
    sensor_type: Literal["river"] = "river"
    water_level_m: float = Field(ge=0.0)
    level_change_m_min: float
    flow_velocity_ms: float = Field(ge=0.0)
    turbidity_ntu: float = Field(ge=0.0)

Reading = GNSSReading | SeismicReading | WeatherReading | RiverReading
