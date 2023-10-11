"""Solver that tries to solve a pairsum instance by a random approach.

Shuffles the instance, divides it into two sections and searches a matching pair between both sections.
"""

from itertools import combinations
import json
import random

line = None
with open("/input/instance.json", "r") as input:
    instance = json.load(input)

ints: list[int] = instance["numbers"]
sol: tuple[int, int, int, int] | None = None
indices = list(range(len(ints)))

while sol is None:
    random.shuffle(indices)
    first_half = indices[: len(ints) // 2]
    second_half = indices[len(ints) // 2 :]
    found_sums = {ints[x] + ints[y]: (x, y) for x, y in combinations(first_half, 2)}

    for x, y in combinations(second_half, 2):
        sum = ints[x] + ints[y]
        if sum in found_sums:
            sol = (*found_sums[sum], x, y)

with open("/output/solution.json", "w+") as f:
    json.dump({"indices": sol}, f)
    raise SystemExit
