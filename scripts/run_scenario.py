import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.scenarios import run_scenario

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'normal'
    print(json.dumps(run_scenario(name), indent=2))
