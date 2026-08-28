import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for p in [
    ROOT/'sensor-simulator'/'gnss', ROOT/'sensor-simulator'/'seismic',
    ROOT/'sensor-simulator'/'weather', ROOT/'sensor-simulator'/'river'
]:
    sys.path.insert(0, str(p))

# Load modules by explicit file path to avoid same-name collisions.
def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

gnss = _load('mg_gnss', ROOT/'sensor-simulator'/'gnss'/'simulator.py')
seismic = _load('mg_seismic', ROOT/'sensor-simulator'/'seismic'/'simulator.py')
weather = _load('mg_weather', ROOT/'sensor-simulator'/'weather'/'simulator.py')
river = _load('mg_river', ROOT/'sensor-simulator'/'river'/'simulator.py')

from rules.threshold_engine import score_readings
from risk_engine.risk_engine import assess
from alerting.alert_service import build_test_alert

VALID = {
    'normal', 'sensor-failure', 'gradual-instability', 'gnss-only',
    'seismic-only', 'river-flood', 'weather-freeze-thaw', 'gnss-seismic',
    'seismic-river', 'rainfall-river', 'multi-hazard', 'sensor-outage',
    'recovery',
}

def run_scenario(name: str):
    if name not in VALID:
        raise ValueError(f'Unknown scenario {name!r}. Valid: {sorted(VALID)}')
    readings = {
        'gnss': gnss.generate(name),
        'seismic': seismic.generate(name),
        'weather': weather.generate(name),
        'river': river.generate(name),
    }
    if name == 'sensor-outage':
        readings.pop('seismic')
    scores, reasons = score_readings(readings)
    # Educational synthetic AI score, intentionally simple in the scenario runner.
    ai_score = min(1.0, max(scores.values()) * 0.85)
    risk = assess(scores, reasons, ai_score).to_dict()
    alert = build_test_alert(risk) if risk['risk_level'] in {'HIGH', 'CRITICAL'} else None
    return {'scenario': name, 'readings': readings, 'risk': risk, 'alert': alert, 'simulation_only': True}
