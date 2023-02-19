"""Simple dummy solver for the DomSet problem, outputting a static solution."""
import json

with open("output/solution/solution.json", "w") as output:
    json.dump({
        "domset": [1],
    }, output)
