"""Simple dummy solver for the Tsptimewindows problem, outputting a static solution."""
import json

with open("output/solution.json", "w") as output:
    json.dump({
        "tour": [0, 3, 4, 1, 2],
    }, output)
