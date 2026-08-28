import random

def generate(mode='normal'):
    return {
        'sensor_type': 'weather', 'sensor_id': 'WEATHER-001',
        'temperature_c': random.uniform(-8, 3), 'humidity_pct': random.uniform(45, 90),
        'rainfall_mm_hr': max(0, random.gauss(0.5, 1.0)),
        'wind_speed_mps': random.uniform(1, 14), 'freeze_thaw_index': random.uniform(0.1, 0.9),
        'quality': random.uniform(0.95, 1.0)
    }
