"""Simple dummy generator for the C4SubGraphIso problem, outputting a static instance."""
import json

with open("output/instance/instance.json", "w+") as output:
    json.dump({
        "num_vertices": 4,
        "edges": [
            [3, 0],
            [0, 1],
            [1, 2],
            [2, 3],
        ],
    }, output)

with open("output/solution/solution.json", "w+") as output:
    json.dump({
        "squares": [
            [0, 1, 2, 3],
        ],
    }, output)
