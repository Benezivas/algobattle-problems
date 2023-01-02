"""Simple dummy solver for the Pairsum} problem, outputting a static solution."""
import json

with open("/output/instance/instance.json", "w+") as output:
    json.dump({
        "indices": [0, 1, 2, 3],
    }, output)