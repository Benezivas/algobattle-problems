"""Simple dummy generator for the Tsptimewindows problem, outputting a static instance."""
import json

with open("output/instance.json", "w+") as output:
    json.dump(
        {
            "locations": [
                {
                    "x": 0,
                    "y": 0,
                    "min_time": 0,
                    "max_time": 1,
                },
                {
                    "x": 0,
                    "y": 2,
                    "min_time": 6,
                    "max_time": 7,
                },
                {
                    "x": 1,
                    "y": 1,
                    "min_time": 2,
                    "max_time": 9,
                },
                {
                    "x": 0,
                    "y": 2,
                    "min_time": 3,
                    "max_time": 3,
                },
                {
                    "x": 2,
                    "y": 2,
                    "min_time": 2,
                    "max_time": 6,
                },
            ],
        },
        output,
    )

with open("output/solution.json", "w+") as output:
    json.dump(
        {
            "tour": [0, 3, 4, 1, 2],
        },
        output,
    )
