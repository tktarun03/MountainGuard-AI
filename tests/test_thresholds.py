from rules.threshold_engine import score_readings

def test_faulty_single_river_sensor_does_not_score_as_hazard():
    scores, reasons = score_readings({'river': {'water_level_m': 20.0, 'level_change_m_min': 17.5, 'quality': 0.1}})
    assert scores['river'] == 0.0
    assert any('SENSOR QUALITY WARNING' in r for r in reasons)
