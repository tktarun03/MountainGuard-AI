# MountainGuard-AI

> **Observe → Understand → Detect → Warn → Prepare**

**Open Educational Multi-Hazard Early Warning Simulator**

MountainGuard-AI is a student-friendly, open-source proof of concept that demonstrates how **IoT sensor streams, transparent rules, anomaly detection, sensor fusion, GIS context, simulated risk propagation, and test alerts** can work together in a mountain / glacier / river hazard-monitoring workflow.

The aim is not to claim that AI can predict or prevent natural disasters. The aim is to help students, researchers, designers, engineers, emergency-management learners, and domain experts explore how a responsible **end-to-end early-warning architecture** might be structured.

> [!CAUTION]
> **EDUCATIONAL / RESEARCH PROTOTYPE ONLY — NOT FOR OPERATIONAL LIFE-SAFETY USE.**  
> This project does **not** predict real disasters and must not be used to issue real-world emergency alerts. Operational early-warning systems require validated scientific models, calibrated field instrumentation, redundant communications, local hazard studies, emergency-management integration, regulatory approval, trained operators, community preparedness, and continuous professional monitoring.

---

## Why this project exists

Natural hazards can develop through chains of events: slope or glacier instability, rock/ice collapse, river blockage, debris movement, downstream flooding, infrastructure disruption, and communication failure.

The engineering question is therefore larger than "Can an AI model predict a disaster?"

A more useful question is:

> **How can multiple observations, physical context, transparent decision logic, AI-assisted anomaly detection, communications, and human judgment work together to buy people more time?**

MountainGuard-AI demonstrates that question using **synthetic data and fictional locations only**.

### Core learning principle

```text
AI ALONE IS NOT THE SOLUTION.

OBSERVATION
+
GOOD DATA
+
MULTIPLE SENSORS
+
PHYSICAL SCIENCE
+
GIS
+
AI
+
COMMUNICATION
+
HUMAN JUDGMENT
+
COMMUNITY PREPAREDNESS
```

---

## What this repository demonstrates

```text
IoT Sensor Simulators
        ↓
      MQTT
        ↓
 Python Data Ingestion
        ↓
 PostgreSQL / TimescaleDB
        ↓
 ┌──────────────┬────────────────┬───────────────┐
 │              │                │               │
Rules Engine  ML Engine      GIS Engine      History
 │              │                │               │
 └──────────────┴────────┬───────┴───────────────┘
                         ↓
                  Sensor Fusion
                         ↓
                    Risk Engine
                         ↓
                 Test Alert Generator
                         ↓
            Dashboard / CAP / Simulators
```

The repository deliberately includes a **false-positive scenario** and **human-in-the-loop review** because a life-safety architecture must not treat one noisy sensor or one model output as unquestionable truth.

---

## Repository structure

```text
MountainGuard-AI/
│
├── README.md
├── SAFETY.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── LICENSE
├── docker-compose.yml
├── Makefile
├── .env.example
├── requirements.txt
│
├── config/
│   └── thresholds.yaml
│
├── sensor-simulator/
│   ├── common/
│   ├── gnss/
│   ├── seismic/
│   ├── weather/
│   ├── river/
│   ├── run_all.py
│   └── README.md
│
├── ingestion/
│   ├── mqtt_consumer.py
│   ├── schemas.py
│   └── database.py
│
├── api/
│   ├── main.py
│   └── state.py
│
├── ai/
│   ├── anomaly_detection/
│   ├── sensor_fusion/
│   ├── training/
│   └── evaluation/
│
├── rules/
│   └── threshold_engine.py
│
├── gis/
│   ├── data/
│   └── risk_propagation/
│
├── risk_engine/
│   ├── risk_engine.py
│   └── risk_levels.py
│
├── alerting/
│   ├── cap/
│   ├── sms_simulator/
│   ├── siren_simulator/
│   └── alert_service.py
│
├── dashboard/
│   └── frontend/
│
├── historical-events/
│   └── synthetic/
│
├── scripts/
│   └── run_scenario.py
│
├── tests/
│
└── docs/
    └── STUDENT_LEARNING_PATH.md
```

---

## Technology stack

### Backend

- Python 3.12+
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- TimescaleDB
- MQTT / Eclipse Mosquitto
- Pandas
- NumPy
- scikit-learn
- PyYAML
- GeoPandas / Shapely / Rasterio / PostGIS — planned GIS extension
- pytest

### Dashboard

A minimal React + TypeScript + Vite starter is included. The boilerplate exposes APIs first so students can learn the data flow before UI complexity is added.

Recommended visualization stack:

- React
- TypeScript
- Vite
- MapLibre or Leaflet
- Recharts

### Infrastructure

- Docker
- Docker Compose
- No paid cloud dependency is required for the starter project.

---

# Quick start

## Option A — Docker Compose

```bash
git clone <YOUR_REPOSITORY_URL>
cd MountainGuard-AI
cp .env.example .env
docker compose up --build
```

Services:

| Service | Default endpoint |
|---|---|
| FastAPI | http://localhost:8000 |
| Swagger/OpenAPI | http://localhost:8000/docs |
| PostgreSQL/TimescaleDB | localhost:5432 |
| MQTT | localhost:1883 |
| Dashboard starter | http://localhost:5173 |

Run a scenario from another terminal:

```bash
python scripts/run_scenario.py multi-hazard
```

## Option B — Python only

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn api.main:app --reload
```

Then open:

```text
http://localhost:8000/docs
```

---

# Demo scenarios

The boilerplate contains five educational scenarios.

## 1. Normal operating day

All sensors remain within synthetic baseline ranges.

Expected progression:

```text
NORMAL
```

## 2. Single faulty sensor

A river sensor suddenly reports an implausible 20 m rise while every other signal remains normal.

Expected response:

```text
SENSOR QUALITY WARNING
```

Not:

```text
DISASTER
```

This demonstrates why redundancy, plausibility checks, and multi-sensor confirmation matter.

## 3. Gradual instability

Synthetic GNSS displacement begins accelerating.

Expected progression:

```text
NORMAL → WATCH
```

A later exercise can add scientifically justified corroborating evidence and explore when an `ELEVATED` state would be appropriate.

## 4. Seismic + river anomaly

Two independent synthetic signals become abnormal.

Expected progression:

```text
WATCH → HIGH
```

## 5. Synthetic multi-hazard event

Example timeline:

```text
09:00 NORMAL

09:03 GNSS acceleration detected
09:04 Seismic anomaly detected
09:05 AI anomaly score increases
09:06 River level changes rapidly
09:06 Sensor fusion = HIGH
09:07 Multiple signals confirmed
09:07 Risk = CRITICAL
09:07 TEST ALERT generated
```

Every generated alert starts with:

```text
EXERCISE — EDUCATIONAL SIMULATION — NOT A REAL EMERGENCY
```

---

# Sensor messages

## GNSS

```json
{
  "sensor_id": "GNSS-001",
  "timestamp": "2026-08-28T10:00:00Z",
  "latitude": 28.1,
  "longitude": 86.8,
  "displacement_mm": 1.8,
  "velocity_mm_day": 2.1,
  "acceleration_mm_day2": 0.1,
  "quality": 0.98
}
```

## Seismic / geophone

```json
{
  "sensor_id": "SEIS-001",
  "timestamp": "2026-08-28T10:00:00Z",
  "rms": 0.12,
  "peak_amplitude": 0.29,
  "dominant_frequency_hz": 18.4,
  "duration_sec": 3.1,
  "quality": 0.97
}
```

Synthetic classes may include:

- normal background
- local vibration
- rockfall-like anomaly
- ice-collapse-like anomaly
- major synthetic event

These labels are **educational abstractions**, not validated real-world seismic classifiers.

## Weather

```json
{
  "sensor_id": "WEATHER-001",
  "timestamp": "2026-08-28T10:00:00Z",
  "temperature_c": -3.2,
  "humidity_pct": 73,
  "rainfall_mm_hr": 0,
  "wind_speed_mps": 8.4,
  "freeze_thaw_index": 0.7,
  "quality": 0.99
}
```

## River

```json
{
  "sensor_id": "RIVER-001",
  "timestamp": "2026-08-28T10:00:00Z",
  "water_level_m": 2.15,
  "level_change_m_min": 0.02,
  "flow_velocity_ms": 1.8,
  "turbidity_ntu": 120,
  "quality": 0.96
}
```

---

# MQTT topics

```text
mountainguard/gnss/+
mountainguard/seismic/+
mountainguard/weather/+
mountainguard/river/+
```

The consumer validates messages using Pydantic and rejects malformed payloads safely.

---

# Transparent rules first

Before machine learning, MountainGuard-AI uses configurable rules.

Conceptually:

```python
if gnss_acceleration > threshold:
    gnss_score += 0.3

if seismic_peak > threshold:
    seismic_score += 0.3

if river_rate_of_change > threshold:
    river_score += 0.4
```

> **All thresholds in this repository are DEMO VALUES ONLY. They are not scientific or operational thresholds.**

See `config/thresholds.yaml`.

---

# Anomaly detection

The starter includes a beginner-friendly anomaly detector using **Isolation Forest** plus a simple rolling/z-score style utility.

Example features:

```text
GNSS acceleration
Seismic RMS
Seismic duration
Temperature change
River level change
River velocity
Turbidity
```

Example output:

```json
{
  "anomaly": true,
  "anomaly_score": 0.81,
  "contributors": [
    "seismic_rms",
    "gnss_acceleration"
  ]
}
```

Do not treat an anomaly score as certainty.

> **A model confidence score is not the same as certainty.**

---

# Sensor fusion

The starter uses a transparent weighted model rather than pretending a black-box model is authoritative.

Default educational weights:

```text
GNSS        20%
SEISMIC     30%
WEATHER     10%
RIVER       30%
AI ANOMALY  10%
```

These weights are demonstration values and must be replaced by scientifically justified methods before any serious research use.

Example result:

```json
{
  "risk_score": 0.72,
  "risk_level": "HIGH",
  "evidence": {
    "gnss": 0.61,
    "seismic": 0.91,
    "weather": 0.22,
    "river": 0.84,
    "ai": 0.73
  }
}
```

---

# Risk levels

```text
NORMAL
WATCH
ELEVATED
HIGH
CRITICAL
```

Every assessment should explain its evidence.

Example:

```json
{
  "risk_level": "HIGH",
  "reason": [
    "Rapid river level change detected",
    "Seismic anomaly confirmed",
    "GNSS velocity increasing"
  ]
}
```

---

# GIS and fictional geography

The starter uses fictional locations and sample GeoJSON.

Example names:

```text
Valley Village A
River Hamlet B
Mountain Camp C
Safe Zone Alpha
```

A simple downstream-arrival simulation may produce:

```json
{
  "settlement": "Valley Village A",
  "estimated_arrival_minutes": 14,
  "simulation_only": true
}
```

Every such result must be displayed as:

> **SIMULATED — NOT A REAL FORECAST**

Future students can extend this module with DEM, slope, river-network, route, and exposure layers using public datasets and proper scientific review.

---

# Alert simulation

The project does **not** send real alerts.

Supported educational outputs:

- dashboard alert
- console alert
- mock SMS
- mock siren event
- CAP-style XML test message

Example:

```text
EXERCISE — EDUCATIONAL SIMULATION

Synthetic multi-sensor event detected.
Risk Level: HIGH
Affected simulated zone: Valley Village A
Estimated simulated arrival: 14 minutes

THIS IS NOT A REAL EMERGENCY ALERT.
```

CAP test messages use test-oriented status/scope values only. The starter intentionally avoids production emergency-service integration.

---

# Human in the loop

The educational workflow is:

```text
AI DETECTS
↓
SYSTEM CORRELATES
↓
OPERATOR REVIEWS
↓
SIMULATED ALERT
```

AI is **not** treated as final authority.

---

# API endpoints

Starter endpoints include:

```text
GET  /health
GET  /sensors
GET  /readings/latest
GET  /risk/current
GET  /risk/history
GET  /risk/explanation
GET  /anomalies
GET  /events
GET  /alerts
GET  /map
POST /simulation/scenario/{scenario_name}
POST /risk/{risk_id}/acknowledge
```

OpenAPI documentation is available at `/docs`.

---

# Student learning path

## Level 1 — Sensor simulation
Understand how time-series sensor messages are created.

## Level 2 — MQTT
Publish and subscribe to telemetry.

## Level 3 — Time-series storage
Persist and query readings.

## Level 4 — Transparent thresholds
Understand deterministic rule engines before ML.

## Level 5 — Anomaly detection
Train a simple model using synthetic normal and abnormal data.

## Level 6 — Sensor fusion
Combine independent signals and understand uncertainty.

## Level 7 — GIS context
Connect a detected event to terrain, rivers, settlements, and safe zones.

## Level 8 — Test alerting
Convert evidence into standardized simulated warning messages.

## Level 9 — False-positive reduction
Handle missing data, broken sensors, and contradictory signals.

## Level 10 — Scientific research
Replace educational assumptions with domain-reviewed models and validated datasets.

See `docs/STUDENT_LEARNING_PATH.md` for exercises.

---

# Suggested student challenges

1. Add a second GNSS sensor and test spatial correlation.
2. Simulate packet loss and delayed telemetry.
3. Add sensor-health scoring.
4. Improve anomaly explanations.
5. Compare Isolation Forest with One-Class SVM.
6. Add a rainfall-driven synthetic scenario.
7. Build a MapLibre/Leaflet hazard map.
8. Add multilingual **test** alert rendering.
9. Add accessibility checks to the dashboard.
10. Create a replay engine for synthetic historical events.
11. Add model/data versioning.
12. Add drift detection.
13. Create a human operator review screen.
14. Build resilience against temporary MQTT/database outages.
15. Research how operational systems validate warning thresholds.

---

# Known limitations

This boilerplate intentionally simplifies many hard problems:

- no validated geophysical model
- no calibrated field sensors
- no real terrain model
- no operational communications
- synthetic data only
- simplified sensor-fusion weights
- simplified hazard propagation
- simplified anomaly detection
- no real evacuation decision logic
- no production emergency-services integration

That is a feature, not a hidden limitation: **the project is designed to teach the architecture without pretending to be a real warning system.**

---

# What NOT to build on top of this starter without professional governance

Do not use this project to implement:

- real public emergency broadcasting
- autonomous siren activation
- automatic government notifications
- automatic evacuation orders
- unsupported disaster-prediction claims
- fake scientific thresholds
- autonomous life-safety decisions

Any real-world research extension should involve appropriate domain scientists, local authorities, emergency-management professionals, community stakeholders, ethics/safety review, and validated instrumentation.

---

# Development commands

```bash
make start
make stop
make normal
make sensor-failure
make gradual-instability
make seismic-river
make multi-hazard
make tests
```

Equivalent Python commands are documented in the Makefile.

---

# Example terminal output

```text
MountainGuard-AI

10:01:01 GNSS-001      NORMAL
10:01:03 SEIS-001      NORMAL
10:01:04 RIVER-001     NORMAL

10:04:11 GNSS-001      ACCELERATION DETECTED
10:05:16 SEIS-001      ANOMALY DETECTED
10:06:02 AI ENGINE     ANOMALY SCORE 0.74
10:06:14 RIVER-001     RAPID CHANGE
10:06:15 SENSOR FUSION HIGH
10:07:00 RISK ENGINE   CRITICAL
10:07:01 ALERT ENGINE

EXERCISE — EDUCATIONAL SIMULATION ONLY
```

---

# Testing

```bash
pytest -q
```

The starter includes tests for:

- API health
- sensor schema validation
- threshold logic
- risk-level mapping
- sensor fusion
- false-positive handling
- CAP test-message generation

---

# Contributing

Contributions are welcome from:

- AI / ML engineers
- IoT developers
- GIS students and engineers
- geologists
- glaciologists
- hydrologists
- telecommunications engineers
- emergency-management researchers
- UX designers
- accessibility specialists
- universities
- students

The most important contribution rule is:

> **Scientific corrections are more valuable than additional features.**

Please read `CONTRIBUTING.md` and `SAFETY.md` before opening a pull request.

---

# Responsible research checklist

Before claiming that an improvement has real hazard-detection value, ask:

- Is the dataset real, traceable, and appropriate?
- Is the sensor calibrated?
- Is the ground truth trustworthy?
- Were false positives measured?
- Were false negatives measured?
- Does the model work outside its training period/location?
- Can the result be explained to an operator?
- What happens if power, network, or one sensor fails?
- Who is authorized to issue a warning?
- How does the warning reach people without smartphones?
- Are language and accessibility requirements covered?
- Has a relevant domain expert reviewed the method?

---

# Roadmap

### Phase 1 — included in this boilerplate
- repository structure
- safety documentation
- Docker Compose
- MQTT broker
- PostgreSQL/TimescaleDB
- FastAPI starter
- synthetic sensors
- rules
- sensor fusion
- risk engine
- simulated alerting
- test suite
- minimal dashboard starter

### Phase 2
- durable sensor persistence
- replayable synthetic datasets
- improved dashboard
- sensor-health metrics

### Phase 3
- richer anomaly detection
- model evaluation reports
- drift monitoring
- explainability improvements

### Phase 4
- richer fictional GIS terrain
- route/safe-zone modeling
- test warning maps

### Phase 5
- literature-driven research modules with domain-expert review

---

# References and scientific grounding

This repository is intentionally not tied to one disaster. Students extending it should start with peer-reviewed literature and official guidance from organizations working on:

- multi-hazard early-warning systems
- glacier and slope monitoring
- seismic / geophone event detection
- GNSS deformation monitoring
- river-level and flash-flood warning
- satellite SAR / optical change detection
- Common Alerting Protocol (CAP)
- last-mile warning dissemination
- community preparedness

Do not copy thresholds or operational procedures from random online examples. Cite every scientific assumption introduced into the project.

---

# Independence and public-content disclaimer

This is a personal, open educational project for technology learning and humanitarian discussion. It is not presented on behalf of any employer, government, emergency-management agency, university, or other organization.

**Personal perspectives on technology, AI, careers and the digital future. Views expressed are my own and do not represent my employer or any organization I am associated with.**

---

# License

Apache License 2.0. See `LICENSE`.

---

## Final idea

Technology cannot control nature.

But responsible observation, science, communication, engineering, and collaboration may help **buy time**.

**For humanity. Openly shared.**
