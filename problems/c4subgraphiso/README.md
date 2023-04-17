# The Square Subgraph Isomorphism Problem
In this problem of graph isomorphism we want to identify as many disjoint
induced Circles of length four (`C_4`) in a given graph as possible.

**Given**: Undirected graph `G = (V,E)` with `|V(G)| = n`  
**Problem**: Find the maximum number of pairwise disjoint, induced `C_4` in `G`

The generator is given an instance size and outputs an undirected graph of at
most this size. Along with the graph, it outputs a certificate solution
containing the set of circles as described above. A certificate solution is only
valid if there is at least one `C_4` given.

The solver then receives this graph and has to find a set of `C_4` within the
time limit and output it. The solution is valid if its size is at least as big
as the certificate solution of the generator.

# Instance
An instance is a standard undirected graph. For example:
```json
{
    "num_vertices": 11,
    "edges": [
        [1, 2],
        [2, 3],
        [3, 4],
        [3, 5],
        [5, 6],
        [6, 7],
        [7, 8],
        [8, 9],
        [9, 10],
        [10, 1],
        [2, 9],
        [5, 9],
        [5, 8],
    ],
}
```

# Solution
The solution contains a set of 4-tuples, each of which identify a copy of `C_4` in the instance.
It is scored by the number of such squares identified, with more squares being better.
A valid solution for the above example would be:
```json
{
    "squares": [
        [5, 6, 7, 8],
        [9, 2, 1, 10],
    ]
}
```
