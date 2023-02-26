"""Simple dummy solver for the C4subgraphiso problem, outputting a static solution."""
import json

with open("output/solution/solution.json", "w") as output:
    json.dump({
        "squares": [
            [0, 1, 2, 3],
        ],
    }, output)
