import pytest
from pydantic import ValidationError
from ingestion.schemas import RiverReading

def test_river_quality_bounds():
    with pytest.raises(ValidationError):
        RiverReading(sensor_id='R', water_level_m=2, level_change_m_min=.1, flow_velocity_ms=1, turbidity_ntu=100, quality=2)
