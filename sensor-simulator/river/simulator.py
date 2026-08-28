import random

def generate(mode='normal'):
    level = random.uniform(1.8, 2.4)
    change = random.uniform(-0.03, 0.05)
    quality = random.uniform(0.94, 1.0)
    if mode in {'river-flood', 'seismic-river', 'rainfall-river', 'multi-hazard'}:
        level = random.uniform(3.2, 5.0)
        change = random.uniform(0.6, 1.4)
    if mode == 'sensor-failure':
        level = 20.0
        change = 17.5
        quality = 0.12
    return {
        'sensor_type': 'river', 'sensor_id': 'RIVER-001', 'water_level_m': level,
        'level_change_m_min': change, 'flow_velocity_ms': random.uniform(1.0, 4.0),
        'turbidity_ntu': random.uniform(70, 700), 'quality': quality
    }
