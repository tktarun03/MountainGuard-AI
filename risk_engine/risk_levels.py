from enum import StrEnum

class RiskLevel(StrEnum):
    NORMAL = 'NORMAL'
    WATCH = 'WATCH'
    ELEVATED = 'ELEVATED'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'

def from_score(score: float) -> RiskLevel:
    if score < 0.20: return RiskLevel.NORMAL
    if score < 0.40: return RiskLevel.WATCH
    if score < 0.60: return RiskLevel.ELEVATED
    if score < 0.80: return RiskLevel.HIGH
    return RiskLevel.CRITICAL
