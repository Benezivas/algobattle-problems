# The Cluster Editing Problem
The *Cluster Editing* problem is an NP-complete problem 
concerned with adding and removing edges in
a graph such that it becomes a set of cliques.

**Given**: Undirected graph `G = (V,E)` with `|V(G)| = n`  
**Problem**: Find edge sets `E'` and `E''` such that for each connected
subgraph `C subseteq G` it holds that `(V(C), E cup E' setminus E'') = K_i` for
some `i in {1,...,n}`.

For a given `n`, the generator is to create a graph with at most `n` vertices.
Additionally, as a certificate, sets of edges `E'` and `E''` as specified above
are to be supplied.

The solver is given a graph of size at most `n` and is supposed to find and
output edge sets `E'` and `E''` as described above. The solver wins the round
for a given `n` if its solution is at most as big as the certificate solution
of the generator.

# Instance
An instance is a standard undirected graph. For example:
```json
{
    "num_vertices": 7,
    "edges": [
        [0, 1],
        [1, 2],
        [1, 3],
        [2, 3],
        [0, 3],
        [3, 4],
        [1, 6],
        [4, 6],
        [5, 6],
        [4, 5],
    ]
}
```

# Solution
A solution contains two sets of edges, `add` and `delete`. The first are edges in `E'`, the second in `E''`.
It is scored by the total number of edges in both sets, with smaller sets being better.

For the instance above, a valid solution may look like this:
```json
{
    "add": [
        [0, 2],
    ],
    "delete": [
        [3, 4],
        [1, 6],
    ],
}
```
