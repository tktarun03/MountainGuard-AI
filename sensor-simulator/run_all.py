import importlib.util
import os
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE / 'common'))
from base import SensorPublisher

def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module

gnss = _load('mg_gnss_sim', BASE/'gnss'/'simulator.py')
seismic = _load('mg_seismic_sim', BASE/'seismic'/'simulator.py')
weather = _load('mg_weather_sim', BASE/'weather'/'simulator.py')
river = _load('mg_river_sim', BASE/'river'/'simulator.py')

MODE = os.getenv('SCENARIO', 'normal')

pub = SensorPublisher()
pub.connect()
print(f'MountainGuard-AI simulator started — scenario={MODE}')
try:
    while True:
        readings = [gnss.generate(MODE), seismic.generate(MODE), weather.generate(MODE), river.generate(MODE)]
        for reading in readings:
            pub.publish(f"mountainguard/{reading['sensor_type']}/{reading['sensor_id']}", reading)
        time.sleep(pub.interval)
finally:
    pub.close()
