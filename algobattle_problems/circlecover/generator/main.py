"""Simple dummy generator for the Circle Cover problem, outputting a static instance."""
import json
from pathlib import Path

Path("output/instance.json").write_text(
    json.dumps(
        {"points": [[0, 1], [50, 50], [100, 17]]},
    )
)

Path("/output/solution.json").write_text(json.dumps({"circles": {"10": [5, 5], "20": [60, 65], "30": [80, 10]}}))
