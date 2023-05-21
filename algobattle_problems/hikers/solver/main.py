"""Simple dummy solver for the Hikers problem, outputting a static solution."""
import json

with open("output/solution.json", "w+") as output:
    json.dump(
        {
            "assignments": {
                2: 1,
                0: 2,
                3: 2,
                4: 2,
            },
        },
        output,
    )
