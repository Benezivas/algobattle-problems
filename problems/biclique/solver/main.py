"""Simple dummy solver for the BiClique problem, outputting a static solution."""
import json

with open("output/solution/solution.json", "w") as output:
    json.dump({
        "s_1": [0],
        "s_2": [1, 2, 3],
    }, output)
