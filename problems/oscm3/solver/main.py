"""Simple dummy solver for the OSCM3 problem, outputting a trivial solution."""
lines = []
with open("input", "r") as input:
    for line in input:
        lines.append(line)
n = len(lines)

with open("output", "w") as output:
    output.write("s ")
    for i in range(n):
        output.write("{} ".format(i))
