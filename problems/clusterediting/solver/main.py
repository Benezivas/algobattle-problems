"""Simple dummy solver for the ClusterEditing problem, outputting a static solution."""
with open("output", "w") as output:
    output.write("s add 1 3\ns del 1 4")
