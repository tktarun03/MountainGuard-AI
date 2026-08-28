# Student Learning Path

## Level 1 — Run a sensor
Open `sensor-simulator/gnss/simulator.py`. Change the baseline ranges and observe output.

## Level 2 — MQTT
Run Mosquitto and publish telemetry. Inspect topics with an MQTT client.

## Level 3 — Persistence
Implement SQLAlchemy models for `sensors`, `sensor_readings`, `anomalies`, `risk_assessments`, `alerts`, and `events`. Add TimescaleDB hypertables.

## Level 4 — Rules
Read `config/thresholds.yaml`. Explain why hard-coded demo thresholds cannot be treated as science.

## Level 5 — Anomaly detection
Use `DemoAnomalyDetector`. Generate synthetic normal/abnormal samples. Measure precision/recall instead of claiming success from one demo.

## Level 6 — Sensor fusion
Change weights and observe how the risk score changes. Discuss why real weights require evidence and validation.

## Level 7 — GIS
Load `gis/data/fictional_map.geojson` in QGIS or a web map. Add a fictional river line and evacuation route.

## Level 8 — Test alerts
Generate a CAP test message. Explain why detection and public warning authorization are different responsibilities.

## Level 9 — Failure engineering
Simulate packet loss, stale data, clock drift, low battery, low quality, impossible values, and contradictory sensors.

## Level 10 — Research
Choose one component and review peer-reviewed literature. Write `docs/research/<topic>.md` with references, assumptions, uncertainty, and limitations before changing the model.
