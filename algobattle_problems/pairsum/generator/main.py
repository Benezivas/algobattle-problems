"""Simple dummy generator for the Pairsum problem, outputting a trivial instance."""
import json

with open("/input/size", "r") as input:
    n = int(input.readline())

with open("/output/instance.json", "w+") as output:
    json.dump(
        {
            "numbers": [1] * n,
        },
        output,
    )

with open("/output/solution.json", "w+") as output:
    json.dump(
        {
            "indices": [0, 1, 2, 3],
        },
        output,
    )
