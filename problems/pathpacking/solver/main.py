"""Simple dummy solver for the PathPacking problem, outputting a static solution."""
import json

with open("output/solution/solution.json", "w") as output:
    json.dump({
        "paths": [
            [2, 1, 0],
        ],
    }, output)
