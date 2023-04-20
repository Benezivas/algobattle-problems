"""Simple dummy solver for the Scheduling problem, outputting static solutions."""
import json

with open("output/solution.json", "w") as output:
    json.dump({
        "assignments": [
            [0, 3],
            [1, 0],
            [2, 4],
            [3, 2],
            [4, 1],
        ],
    }, output)
