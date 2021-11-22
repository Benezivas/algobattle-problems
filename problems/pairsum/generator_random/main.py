"""Generate a list of random numbers, with 4 random numbers manually set to be a valid solution."""
import random

n = 0
with open("input", "r") as input:
    n = int(input.readline())

randlist = [random.randint(0, 2**62) for i in range(n)]
sol = random.sample(range(n), 4)
randlist[sol[0]] = random.randint(2**60, 2**62)
randlist[sol[1]] = random.randint(2**60, 2**62)
randlist[sol[2]] = random.randint(0, 2**59)
randlist[sol[3]] = randlist[sol[0]] + randlist[sol[1]] - randlist[sol[2]]

with open("output", "w") as output:
    output.write(" ".join(str(i) for i in randlist))
    output.write("\n")
    output.write(" ".join(str(i) for i in sol))
