"""Simple dummy generator for the C4SubGraphIso problem, outputting a static instance."""
import json

with open("output/instance/instance.json", "w+") as output:
    json.dump({
        "num_vertices": 3,
        "edges": [
            [0, 1],
            [1, 2],
            [2, 0],
        ],
        "fvs": [1]
    }, output)

with open("output/solution/solution.json", "w+") as output:
    json.dump({
        "path": [
            [0, 1, 2],
        ],
    }, output)
