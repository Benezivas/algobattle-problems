n = 0
with open("input", "r") as input:
    n = int(input.readline())

with open("output", "w") as output:
    output.write(" ".join("1" for i in range(n)))
    output.write("\n")
    output.write("0 1 2 3")
