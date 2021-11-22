"""Simple dummy generator for the ClusterEditing problem, outputting a static instance."""
with open("output", "w") as output:
    output.write("e 1 2\ne 3 2\ne 1 4\ns del 1 4\ns add 1 3")
