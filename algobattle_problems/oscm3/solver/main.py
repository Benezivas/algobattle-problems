"""Simple dummy solver for the OSCM3 problem, outputting trivial solutions."""
import json

with open("input/info.json", "r") as infofile:
    info = json.load(infofile)
    size = int(info["max_size"])

with open("output/solution.json", "w") as output:
    json.dump(
        {
            "vertex_order": list(range(size)),
        },
        output,
    )
