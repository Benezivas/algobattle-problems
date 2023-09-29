"""Simple dummy solver for the CircleCover problem, outputting a static solution."""
import json
from pathlib import Path

Path("/output/solution.json").write_text(json.dumps({"circles": {"10": [5, 5], "20": [60, 65], "30": [80, 10]}}))
