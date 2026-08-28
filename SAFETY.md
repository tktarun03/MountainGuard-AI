# Safety, Ethics and Responsible Use

## Mandatory notice

**MountainGuard-AI is an educational and research prototype. It is not an operational warning system.**

It must not be used to predict real disasters, trigger real sirens, issue public alerts, make evacuation decisions, or replace professional scientific and emergency-management systems.

## Why safety matters

Life-safety systems fail in more ways than ordinary software. A wrong result can create panic, complacency, unnecessary evacuation, loss of trust, or delayed response.

### False positives
A system may flag a dangerous event when none exists. Causes include broken sensors, electromagnetic noise, clock drift, bad calibration, data corruption, environmental interference, or model error.

### False negatives
A system may fail to identify a dangerous event. This is often more serious than a false positive and must be measured explicitly in any real research program.

### Sensor failure
Assume sensors can fail, freeze, lose power, drift, be buried, become disconnected, or report impossible values.

### Model drift
A model trained on one period, terrain type, season, sensor network, or region may not generalize.

### Insufficient training data
Rare disasters provide limited labeled data. Synthetic data is useful for software learning but cannot prove real-world predictive performance.

### Dataset bias
If training data excludes important seasons, event types, terrains, sensor qualities, or communities, model behavior may be misleading.

### Communication failure
Detection is not enough. Networks, mobile towers, power, backhaul, radio, and internet can fail during extreme events.

### Cybersecurity
Any connected monitoring system must consider authentication, authorization, device identity, tampering, replay attacks, data integrity, update security, network segmentation, logging, and incident response.

### Human oversight
A machine-generated score should not automatically become a public warning.

```text
AI DETECTS
↓
SYSTEM CORRELATES
↓
TRAINED HUMAN / AUTHORIZED PROCESS REVIEWS
↓
APPROVED WARNING WORKFLOW
```

### Community trust
Warnings must be understandable, credible, culturally appropriate, actionable, and tested with the communities expected to use them.

### Accessibility
Warning interfaces should account for vision, hearing, mobility, cognitive, literacy, language, and connectivity constraints.

### Multilingual communication
Operational messages require validated translations and locally understood terminology. Machine translation alone is insufficient for emergency messages without review.

### Governance
Real systems require clear responsibility for sensing, maintenance, model ownership, warning authorization, escalation, auditing, incident review, and public communication.

## Core rule

> **A model confidence score is not the same as certainty.**

## Prohibited operational use

Do not connect this starter to:

- public warning infrastructure
- emergency sirens
- production SMS gateways
- government emergency channels
- automatic evacuation systems
- real incident command systems

without appropriate professional authority, validation, review, and governance.

## Synthetic-data rule

All included datasets, coordinates, thresholds, hazard paths, settlements, and timing estimates are fictional/demo values unless explicitly documented otherwise.

## Research extension checklist

Any serious extension should document:

1. scientific hypothesis
2. data provenance
3. instrument characteristics
4. calibration method
5. labeling / ground truth
6. train/validation/test separation
7. false-positive rate
8. false-negative rate
9. uncertainty
10. generalization limits
11. human-review process
12. communication assumptions
13. failure-mode testing
14. ethical/community review
15. domain-expert review

Scientific corrections are more valuable than additional features.
