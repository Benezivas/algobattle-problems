"""Simple dummy solver for the C4SubGraphIso problem, outputting a static solution."""
import json

with open("output/solution/solution.json", "w") as output:
    json.dump({
        "path": [
            [2, 1, 0],
        ],
    }, output)
