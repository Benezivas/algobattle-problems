"""Simple dummy solver for the ClusterEditing problem, outputting a static solution."""
import json

with open("output/solution.json", "w") as output:
    json.dump(
        {
            "add": [
                [1, 3],
            ],
            "delete": [
                [1, 2],
            ],
        },
        output,
    )
