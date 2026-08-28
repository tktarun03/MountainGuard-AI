def estimate_arrival(distance_km: float, speed_mps: float) -> dict:
    """Educational arithmetic only; NOT a physical hazard model."""
    if speed_mps <= 0:
        raise ValueError('speed_mps must be positive')
    minutes = (distance_km * 1000) / speed_mps / 60
    return {'estimated_arrival_minutes': round(minutes, 1), 'simulation_only': True}
