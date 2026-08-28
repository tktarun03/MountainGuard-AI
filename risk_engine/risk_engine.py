from dataclasses import asdict, dataclass
from ai.sensor_fusion.fusion import fuse
from risk_engine.risk_levels import from_score

@dataclass
class RiskAssessment:
    risk_score: float
    risk_level: str
    evidence: dict
    reason: list[str]
    simulation_only: bool = True

    def to_dict(self):
        return asdict(self)

def assess(sensor_scores: dict[str, float], reasons: list[str], ai_score: float = 0.0) -> RiskAssessment:
    risk_score = fuse(sensor_scores, ai_score)
    return RiskAssessment(
        risk_score=risk_score,
        risk_level=from_score(risk_score).value,
        evidence={**sensor_scores, 'ai': ai_score},
        reason=reasons or ['No synthetic anomaly evidence'],
    )
