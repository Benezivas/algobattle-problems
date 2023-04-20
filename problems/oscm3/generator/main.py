"""Simple dummy generator for the BiClique problem, outputting trivial instances."""
import json

with open("input/info.json", "r") as infofile:
    info = json.load(infofile)
    size = int(info["size"])

with open("output/instance.json", "w+") as output:
    adjacent_edges = []
    for i in range(size):
        adjacent_edges.append(list())  # No edge at each node
    json.dump({
        "num_vertices": size,
        "adjacent_edges": adjacent_edges,
    }, output)

with open("output/solution.json", "w+") as output:
    permutation = []
    for i in range(size):
        permutation.append(i)  # Identity as permutation
    json.dump({
        "permutation": permutation,
    }, output)
