# Sensor Simulator

Synthetic telemetry only. Nothing in this directory represents calibrated field behavior.

Set a scenario:

```bash
SCENARIO=multi-hazard python sensor-simulator/run_all.py
```

Supported values: `normal`, `sensor-failure`, `gradual-instability`, `seismic-river`, `multi-hazard`.
