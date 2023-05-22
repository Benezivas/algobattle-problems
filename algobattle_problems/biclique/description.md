# The Bipartite Clique Problem
The *Bipartite Clique* problem is closely related to the *Maximum Clique*
problem. In it, we want to find the biggest complete bipartite subgraph in a
given Graph.

**Given**: Undirected graph `G = (V,E)` with `|V(G)| = n`  
**Problem**: Find the biggest subgraph `G' = (V_1 union V_2, E')` of `G` such that
`G' = K_{i,j}`

The generator is given an instance size and outputs an undirected graph of at most this size.
Along with the graph, it outputs a certificate solution for the biggest
bipartite clique of the graph that it knows.

The solver then receives this graph and has to find a bipartite clique of
maximum size within the time limit and output it. The solution is valid if its
size is at least as big as the certificate solution of the generator.

# Instance
An instance is a standard undirected graph. For example:
```json
{
    "num_vertices": 11,
    "edges": [
        [1, 2],
        [2, 3],
        [2, 8],
        [8, 5],
        [8, 10],
        [8, 7],
        [6, 5],
        [6, 7],
        [6, 9],
        [10, 9],
        [10, 7],
    ],
}
```

# Solution
A solution contains two vertex sets, `s_1` and `s_2`. Each should form the independent sets of
a complete bipartite graph. I.e. the instance graph should contain no edges between any two vertices in each set,
but all edges that can lie between the sets.
It is scored based on the total size of the two sets, with bigger sets being better.

```json
{
    "s_1": [8, 6, 10],
    "s_2": [9, 7],
}
```
