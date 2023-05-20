# The Path Packing Problem

The *Path Packing* problem is a classical packing problem. In it, we are interested in identifying as many node-disjoint
paths as subgraphs in a given graph. For this problem, we are interested in very short paths for which the problem is
already NP-complete, i.e. packing paths with two edges (`P_3`).

**Given**: Undirected graph `G = (V,E)` with `|V(G)| = n`  
**Problem**: Find the maximum number of pairwise disjoint, `P_3` in `G`

The generator needs to output both an instance and a certificate solution. Solvers are scored based on how many paths
they found compared to the generator.

## Instance

An instance is a standard undirected graph. For example:

```json
{
    "edges": [
        [0, 1],
        [1, 2],
        [0, 3],
        [1, 4],
        [1, 5],
        [1, 3],
        [3, 6],
        [3, 7],
        [6, 7],
        [4, 7],
        [5, 7],
        [7, 9]
    ]
}
```

## Solution

A solution contains a set of 3-paths in the instance. A valid solution to the above instance is:

```json
{
    "paths": [
        [5, 2, 1],
        [1, 3, 6],
        [8, 7, 4]
    ]
}
```
