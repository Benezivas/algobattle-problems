# The Pairsum Problem

The Pairsum problem is a simple task which proved to be a good primer task for students to get used to the environment.

The task is the following:

**Given**: List `L = [z_1,...,z_n]`, `z_i in [0,2^{63})`  
**Question**: Are there pairwise different `a, b, c, d in [0,...,n-1]` such that `L[a] + L[b] = L[c] + L[d]`?  

I.e. given a list of natural numbers the task is to find two pairs of these numbers with the same sum.
The `size` of an instance limits the length of the list of numbers.

The generator should create a hard to solve instance and a certificate solution to prove that such a pair of pairs
indeed exists. The generator should be able to efficiently find the solution for any input list.

## Instance
An instance just contains the list of numbers. For example:
```json
{
    "numbers": [1, 2, 3, 4, 5]
}
```
## Solution
A solution contains a list with the four indices `a, b, c, d` in this order. For example:
```json
{
    "indices": [1, 4, 2, 3]
}
```
This is a valid solution since `L[1] + L[4] = 2 + 5 = 3 + 4 = L[2] + L[3]`.
