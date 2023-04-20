"""Simple dummy generator for the Scheduling problem, outputting static instances."""
import json

with open("output/instance.json", "w+") as output:
    json.dump({
        "job_lengths": [30, 120, 24, 40, 60],
    }, output)

with open("output/solution.json", "w+") as output:
    json.dump({
        "assignments": [
            [0, 3],
            [1, 0],
            [2, 4],
            [3, 2],
            [4, 1],
        ],
    }, output)
