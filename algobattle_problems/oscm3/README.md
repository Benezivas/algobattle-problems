# The One-Sided Crossing Minimization-3 Problem
In the area of *graph drawing*, one is interested in the two-dimensional visualization of graphs. One of the problems
from this area is the *One-Sided Crossing Minimization* problem, which is concerned with drawing graphs in layers while
minimizing the number of edge crossings between each layer.

**Given**: Bipartite Graph `G = (V_1 \dot\cup V_2, E)` with `|V_1| = |V_2| = n`, with `V_1` and `V_2` each ordered on a
virtual line, parallel to one another. Each node of `V_1` has degree at most 3.  
**Problem**: Find a permutation of `V_1`, that minimizes the number of edge crossings.

The generator needs to output both an instance and a certificate solution. The solver's solution is scored based on how
small the number of edges that cross in it are.

## Instance

Since the graph is bipartite it is enough to only specify edges from `V_1` to `V_2`. Vertices in both sets are numbered
1 through `size - 1`, meaning that an instance actually contains twice as many vertices as `size` is. We use a
dictionary to define adjacency lists. Each key is an element of `V_1` and its item the neighboring elements in `V_2`.

```json
{
    "neighbors": {
        "0": [1, 2],
        "1": [0, 1, 2],
        "2": [0, 1]
    }
}
```

Note that each list can only contain up to three elements and that keys are strings while list elements are integers.

## Solution

The solution just contains the permutation of `V_1` that minimizes the number of crossings, encoded as a single list.

```json
{
    "vertex_order": [2, 1, 0]
}
```
