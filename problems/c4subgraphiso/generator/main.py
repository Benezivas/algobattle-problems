"""Simple dummy generator for the C4SubGraphIso problem, outputting a static instance."""
with open("output", "w") as output:
    output.write("s 1 2 3 4\n")
    output.write("e 4 1\n")
    output.write("e 1 2\n")
    output.write("e 2 3\n")
    output.write("e 3 4\n")
