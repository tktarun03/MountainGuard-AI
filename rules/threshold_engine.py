from pathlib import Path
import yaml

CONFIG = Path(__file__).resolve().parents[1] / 'config' / 'thresholds.yaml'

def load_thresholds():
    return yaml.safe_load(CONFIG.read_text())

def score_readings(readings: dict) -> tuple[dict, list[str]]:
    cfg = load_thresholds()
    scores = {'gnss': 0.0, 'seismic': 0.0, 'weather': 0.0, 'river': 0.0}
    reasons: list[str] = []

    gnss = readings.get('gnss')
    if gnss:
        a = gnss.get('acceleration_mm_day2', 0)
        if a >= cfg['gnss']['acceleration_high']:
            scores['gnss'] = 1.0; reasons.append('Strong synthetic GNSS acceleration')
        elif a >= cfg['gnss']['acceleration_watch']:
            scores['gnss'] = 0.6; reasons.append('Synthetic GNSS acceleration above demo watch threshold')

    seismic = readings.get('seismic')
    if seismic:
        if seismic.get('peak_amplitude', 0) >= cfg['seismic']['peak_high']:
            scores['seismic'] = 1.0; reasons.append('Synthetic seismic peak above demo high threshold')
        elif seismic.get('rms', 0) >= cfg['seismic']['rms_watch']:
            scores['seismic'] = 0.6; reasons.append('Synthetic seismic RMS above demo watch threshold')

    weather = readings.get('weather')
    if weather and weather.get('freeze_thaw_index', 0) >= cfg['weather']['freeze_thaw_watch']:
        scores['weather'] = 0.5; reasons.append('Synthetic freeze/thaw context elevated')

    river = readings.get('river')
    if river:
        if river.get('water_level_m', 0) >= cfg['river']['impossible_level_m'] and river.get('quality', 1) < 0.5:
            scores['river'] = 0.0; reasons.append('SENSOR QUALITY WARNING: implausible river reading with low quality')
        elif abs(river.get('level_change_m_min', 0)) >= cfg['river']['level_change_high']:
            scores['river'] = 1.0; reasons.append('Rapid synthetic river-level change')
        elif abs(river.get('level_change_m_min', 0)) >= cfg['river']['level_change_watch']:
            scores['river'] = 0.6; reasons.append('Synthetic river-level change above demo watch threshold')

    return scores, reasons
