"""Simple dummy generator for the Tsptimewindows problem, outputting a static instance."""
import json

with open("output/instance/instance.json", "w+") as output:
    json.dump({
        "num_vertices": 5,
        "positions": [
            [0, 0],
            [0, 2],
            [1, 1],
            [0, 2],
            [2, 2],
        ],
        "time_windows": [
            [0, 1],
            [6, 7],
            [2, 9],
            [3, 3],
            [2, 6],
        ],
    }, output)

with open("output/solution/solution.json", "w+") as output:
    json.dump({
        "tour": [0, 3, 4, 1, 2],
    }, output)
