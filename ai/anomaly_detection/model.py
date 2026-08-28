from dataclasses import dataclass
import numpy as np
from sklearn.ensemble import IsolationForest

FEATURES = [
    'gnss_acceleration', 'seismic_rms', 'seismic_duration',
    'temperature_change', 'river_level_change', 'river_velocity', 'turbidity'
]

@dataclass
class AnomalyResult:
    anomaly: bool
    anomaly_score: float
    contributors: list[str]

class DemoAnomalyDetector:
    """Educational anomaly detector trained on synthetic baseline samples."""
    def __init__(self, random_state: int = 42):
        rng = np.random.default_rng(random_state)
        baseline = rng.normal(0, 1, size=(500, len(FEATURES)))
        self.model = IsolationForest(contamination=0.04, random_state=random_state)
        self.model.fit(baseline)

    def predict(self, feature_vector: list[float]) -> AnomalyResult:
        x = np.asarray(feature_vector, dtype=float).reshape(1, -1)
        pred = self.model.predict(x)[0]
        raw = -float(self.model.score_samples(x)[0])
        score = max(0.0, min(1.0, (raw - 0.35) / 0.45))
        abs_values = np.abs(x[0])
        top = np.argsort(abs_values)[-2:][::-1]
        return AnomalyResult(pred == -1, round(score, 3), [FEATURES[i] for i in top])
