import random

def generate(mode='normal'):
    rms = random.uniform(0.05, 0.20)
    peak = random.uniform(0.10, 0.40)
    duration = random.uniform(1.0, 4.0)
    if mode in {'seismic-only', 'seismic-river', 'gnss-seismic', 'multi-hazard'}:
        rms = random.uniform(0.7, 1.4)
        peak = random.uniform(1.3, 2.6)
        duration = random.uniform(8.0, 25.0)
    return {
        'sensor_type': 'seismic', 'sensor_id': 'SEIS-001', 'rms': rms,
        'peak_amplitude': peak, 'dominant_frequency_hz': random.uniform(8, 25),
        'duration_sec': duration, 'quality': random.uniform(0.93, 1.0)
    }
