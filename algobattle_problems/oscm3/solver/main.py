"""Simple dummy solver for the OSCM3 problem, outputting trivial solutions."""
import json

with open("input/info.json", "r") as infofile:
    info = json.load(infofile)
    size = int(info["size"])

with open("output/solution.json", "w") as output:
    permutation = []
    for i in range(size):
        permutation.append(i)
    json.dump({
        "permutation": permutation,
    }, output)
