# The Dominating Set Approximation Problem

The *Dominating Set* problem is a classic NP-complete problem.
A _dominating set_ is a subset of vertices `S` such that every vertex either is adjacent to one in `S` or is in `S`
itself. Trivially, the entire vertex set always is a dominating set. As such the problem is to find one that is as
small as possible.

**Given**: Undirected graph `G = (V,E)` with `|V(G)| = n`  
**Problem**: Find a dominating set `S' subseteq V(G)`, with `|S|` as small as possible.

The generator needs to output a graph with at most `size` many vertices, and a certificate solution. The solver's
score is the ratio of the generator's vertex cover to the one it found.

## Instance

An instance is a standard undirected graph. For example:

```json
{
    "num_vertices": 7,
    "edges": [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 0],
        [1, 5],
        [2, 4],
    ]
}
```

## Solution

A solution just contains the dominating set of vertices. Its score is the number of vertices in it. A valid solution
for the instance above is

```json
{
    "vertices": [0, 3]
}
```
