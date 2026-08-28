import random

def generate(mode='normal'):
    acceleration = random.uniform(0.02, 0.20)
    velocity = random.uniform(1.0, 2.5)
    if mode == 'gradual-instability':
        acceleration = random.uniform(0.9, 2.2)
        velocity = random.uniform(3.0, 8.0)
    if mode == 'multi-hazard':
        acceleration = random.uniform(2.1, 4.0)
        velocity = random.uniform(8.0, 15.0)
    return {
        'sensor_type': 'gnss', 'sensor_id': 'GNSS-001', 'latitude': 28.1,
        'longitude': 86.8, 'displacement_mm': random.uniform(0.5, 5.0),
        'velocity_mm_day': velocity, 'acceleration_mm_day2': acceleration,
        'quality': random.uniform(0.94, 1.0)
    }
