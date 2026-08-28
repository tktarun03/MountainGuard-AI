from datetime import datetime, timezone

PREFIX = 'EXERCISE — EDUCATIONAL SIMULATION — NOT A REAL EMERGENCY'

def build_test_alert(risk: dict, zone='Valley Village A', eta_minutes=14):
    return {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'prefix': PREFIX,
        'risk_level': risk['risk_level'],
        'zone': zone,
        'estimated_arrival_minutes': eta_minutes,
        'simulation_only': True,
        'message': (
            f"{PREFIX}\nSynthetic multi-sensor event detected. "
            f"Risk Level: {risk['risk_level']}. Affected simulated zone: {zone}. "
            f"Estimated simulated arrival: {eta_minutes} minutes. THIS IS NOT A REAL EMERGENCY ALERT."
        ),
    }
