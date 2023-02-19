"""Simple dummy generator for the DomSet problem, outputting a static instance."""
import json

with open("output/instance/instance.json", "w+") as output:
    json.dump({
        "num_vertices": 2,
        "edges": [
            [0, 1],
        ],
    }, output)

with open("output/solution/solution.json", "w+") as output:
    json.dump({
        "domset": [0],
    }, output)
