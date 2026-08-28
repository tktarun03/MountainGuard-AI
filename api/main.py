from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from api.state import STATE
from scripts.scenarios import run_scenario

app = FastAPI(
    title='MountainGuard-AI',
    version='0.1.0',
    description='EDUCATIONAL / RESEARCH SIMULATION ONLY — NOT FOR OPERATIONAL LIFE-SAFETY USE.',
)

@app.get('/health')
def health():
    return {'status': 'ok', 'simulation_only': True, 'warning': 'NOT A REAL EMERGENCY SYSTEM'}

@app.get('/sensors')
def sensors(): return {'items': STATE['sensors']}

@app.get('/readings/latest')
def latest(): return STATE['latest_readings']

@app.get('/risk/current')
def current_risk():
    return STATE['risk_history'][-1] if STATE['risk_history'] else {'risk_score': 0.0, 'risk_level': 'NORMAL', 'simulation_only': True}

@app.get('/risk/history')
def risk_history(): return STATE['risk_history']

@app.get('/risk/explanation')
def risk_explanation():
    if not STATE['risk_history']:
        return {'risk_score': 0.0, 'level': 'NORMAL', 'top_factors': [], 'simulation_only': True}
    r = STATE['risk_history'][-1]
    factors = sorted(r['evidence'].items(), key=lambda kv: kv[1], reverse=True)[:3]
    return {'risk_score': r['risk_score'], 'level': r['risk_level'], 'top_factors': [{'signal': k, 'contribution': v} for k,v in factors], 'simulation_only': True}

@app.get('/anomalies')
def anomalies(): return STATE['anomalies']

@app.get('/events')
def events(): return STATE['events']

@app.get('/alerts')
def alerts(): return STATE['alerts']

@app.get('/map')
def map_data():
    path = Path(__file__).resolve().parents[1] / 'gis' / 'data' / 'fictional_map.geojson'
    return json.loads(path.read_text())

@app.post('/simulation/scenario/{scenario_name}')
def simulation(scenario_name: str):
    try:
        result = run_scenario(scenario_name)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    STATE['latest_readings'] = result['readings']
    STATE['risk_history'].append(result['risk'])
    STATE['events'].append({'scenario': scenario_name, 'simulation_only': True})
    if result.get('alert'):
        STATE['alerts'].append(result['alert'])
    return result

@app.post('/risk/{risk_id}/acknowledge')
def acknowledge(risk_id: str):
    STATE['acknowledged'].add(risk_id)
    return {'risk_id': risk_id, 'acknowledged': True, 'simulation_only': True}
