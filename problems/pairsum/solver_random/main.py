"""Solver that tries to solve a pairsum instance by a random approach.

Shuffles the instance, divides it into two sections and searches a matching pair between both sections.
"""

import random
import sys

line = None
with open("input", "r") as input:
    line = input.readline()

ints = [int(a) for a in line.split()]
n = len(ints)

with open("output", "w") as output:
    while True:
        shuffeled = [x for x in range(n)]
        random.shuffle(shuffeled)
        A = shuffeled[:len(ints) // 2]
        B = shuffeled[len(ints) // 2:]
        D = {}
        for x in range(len(A)):
            for y in range(x + 1, len(A)):
                s = ints[A[x]] + ints[A[y]]
                D[s] = (A[x], A[y])

        for x in range(len(B)):
            for y in range(x + 1, len(B)):
                s = ints[B[x]] + ints[B[y]]
                if s in D:
                    q = D[s][0]
                    w = D[s][1]
                    e = B[x]
                    r = B[y]
                    output.write(" ".join(str(x) for x in [q, w, e, r]))
                    output.close()
                    sys.exit()
