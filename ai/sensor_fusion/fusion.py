from pathlib import Path
import yaml

CONFIG = Path(__file__).resolve().parents[2] / 'config' / 'thresholds.yaml'

def fuse(evidence: dict[str, float], ai_score: float = 0.0) -> float:
    cfg = yaml.safe_load(CONFIG.read_text())
    weights = cfg['weights']
    values = {**evidence, 'ai': ai_score}
    score = sum(float(values.get(k, 0.0)) * float(w) for k, w in weights.items())
    return round(max(0.0, min(1.0, score)), 3)
