# The Hikers Problem
The *Hikers* problem is a spin on the paper
[Group Activity Selection Problem With Approval Preferences](https://doi.org/10.1007/s00182-017-0596-4)
which can be described as follows:

There are `n` hikers who would like to go on a hike in groups. Each hiker has a preference interval of the size of the
group they want to hike in, which includes the hiker themselves. Find a distribution of as many hikers into groups
as possible, such that their preferences are met. An optimal solution for an instance may be unable to assign every
hiker to a group.

**Given**: Set `H` of `n` hikers, and for each hiker a minimal and maximal preferred group size.  
**Problem**: Find a subset of hikers `S subseteq H` of maximum size and an assignment of `S` into groups, such that each
hiker of `S` is in a group of their preferred size.

The generator needs to output a list of hiker preferences, and a certificate solution. The solver's solution score is
the ratio of hikers satisfied with its solution to the number of hikers happy with the generator's solution.

## Instances

Instances just contain a list of the hiker's group preferences. For example:

```json
{
    "hikers": [
        [1, 3],
        [10, 12],
        [1, 1],
        [2, 5],
        [3, 3]
    ]
}
```

Here, the first hiker prefers groups containing between 1 and 3 people, the third hiker wants to only walk alone, etc.

## Solutions

The Solution consists of just the mapping of hikers to groups. Every group is identified via a natural number. A
possible solution to the instance above is:

```json
{
    "assignments": {
        "0": 1,
        "3": 1,
        "4": 1,
        "2": 2
    }
}
```

Which puts the first, fourth, and fifth (note the zero indexing) hikers into a single group, and the third hiker into
their own group.
