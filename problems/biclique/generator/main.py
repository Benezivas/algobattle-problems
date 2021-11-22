"""Simple dummy generator for the BiClique problem, outputting a static instance."""
with open("output", "w") as output:
    output.write("e 1 2\n")
    output.write("e 1 3\n")
    output.write("e 1 4\n")
    output.write("s set1 1\n")
    output.write("s set2 2\n")
    output.write("s set2 3\n")
    output.write("s set2 4\n")
