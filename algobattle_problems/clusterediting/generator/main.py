"""Simple dummy generator for the ClusterEditing problem, outputting a static instance."""
import json

with open("output/instance.json", "w+") as output:
    json.dump(
        {
            "num_vertices": 4,
            "edges": [
                [0, 1],
                [1, 2],
                [0, 3],
            ],
        },
        output,
    )

with open("output/solution.json", "w+") as output:
    json.dump(
        {
            "add": [
                [0, 2],
            ],
            "delete": [
                [0, 3],
            ],
        },
        output,
    )
