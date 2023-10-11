"""Simple dummy generator for the BiClique problem, outputting trivial instances."""
import json

with open("input/max_size.txt", "r") as file:
    size = int(file.read())

with open("output/instance.json", "w+") as output:
    json.dump(
        {
            "neighbors": {i: set() for i in range(size)},
        },
        output,
    )

with open("output/solution.json", "w+") as output:
    json.dump(
        {
            "vertex_order": list(range(size)),
        },
        output,
    )
