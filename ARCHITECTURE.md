# Architecture

## Design goals

1. **Transparent before clever** — rules and evidence are visible.
2. **Multi-sensor before single-sensor** — one noisy input should not dominate.
3. **Human in the loop** — risk scoring and public warning are separate concepts.
4. **Synthetic by default** — safe for students to run locally.
5. **Failure-aware** — sensor quality and contradictory evidence are first-class inputs.
6. **Explainable** — each risk result returns contributing signals.

## Logical flow

```text
Synthetic Sensors
  ├── GNSS
  ├── Seismic
  ├── Weather
  └── River
       ↓
MQTT Broker
       ↓
Validated Ingestion
       ↓
Time-series Storage
       ↓
Rules + AI anomaly scoring
       ↓
Sensor Fusion
       ↓
Risk Level + Explanation
       ↓
Fictional GIS impact estimate
       ↓
Operator acknowledgement
       ↓
TEST alert outputs only
```

## Failure philosophy

If a single sensor reports an extreme value but its quality is low and peer signals disagree, the system should lower confidence and produce a sensor-health warning rather than immediately escalating to CRITICAL.

## Future real-research boundary

Operational work would require physically meaningful hazard models, site-specific geotechnical/glaciological/hydrological analysis, validated thresholds, instrument calibration, reliability engineering, communications redundancy, legal authority, and community procedures. Those are intentionally outside this boilerplate.
