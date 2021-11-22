n = 0
with open("input", "r") as input:
    n = int(input.readline())
with open("output", "w") as output:
    for i in range(n):
        output.write("n {}\n".format(i))
    output.write("s ")
    for i in range(n):
        output.write("{} ".format(i))
