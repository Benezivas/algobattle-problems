"""Simple dummy generator for the Hikers problem, outputting a static instance."""
import json

with open("output/instance.json", "w+") as output:
    json.dump({
        "hikers": [
            [1, 3],
            [10, 12],
            [1, 1],
            [2, 5],
            [3, 3],
        ],
    }, output)

with open("output/solution.json", "w+") as output:
    json.dump({
        "assignments": {
            0: 1,
            3: 1,
            4: 1,
            2: 2,
        },
    }, output)
