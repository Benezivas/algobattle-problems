"""Simple dummy generator for the BiClique problem, outputting a static instance."""
import json

with open("output/instance.json", "w+") as output:
    json.dump({
        "num_vertices": 4,
        "edges": [
            [0, 1],
            [0, 2],
            [0, 3],
        ],
    }, output)

with open("output/solution.json", "w+") as output:
    json.dump({
        "s_1": [0],
        "s_2": [1, 2, 3]
    }, output)
