from risk_engine.risk_levels import from_score
from ai.sensor_fusion.fusion import fuse
from scripts.scenarios import VALID, run_scenario

def test_risk_levels():
    assert from_score(0.1).value == 'NORMAL'
    assert from_score(0.9).value == 'CRITICAL'

def test_fusion_range():
    assert 0 <= fuse({'gnss':1,'seismic':1,'weather':1,'river':1}, 1) <= 1

def test_every_demo_scenario_runs():
    for scenario in VALID:
        result = run_scenario(scenario)
        assert result['simulation_only'] is True
        assert result['risk']['simulation_only'] is True
