"""Simple dummy solver for the BiClique problem, outputting a static solution."""
import json
from random import random

sol = [1, 2]
if random() <= 0.9:
    sol.append(3)

with open("output/solution.json", "w") as output:
    json.dump(
        {
            "s_1": [0],
            "s_2": sol,
        },
        output,
    )
