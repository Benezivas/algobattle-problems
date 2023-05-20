"""Simple dummy solver for the Scheduling problem, outputting static solutions."""
import json

with open("output/solution.json", "w") as output:
    json.dump({
        "assignments": [4, 1, 5, 3, 2],
    }, output)
