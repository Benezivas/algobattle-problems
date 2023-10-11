# Traveling Salesman with Time Windows

This problem is a variant of the well known traveling salesman problem, in particular of the (euclidean) metric TSP.
Here every location has a time window where it accepts visits from the salesman, if it's too early they will have to
wait and if it's too late they will not be able to complete their tour.

**Given**: `size` many locations.  
**Problem**: Find a tour visiting every location exactly once such that the total time taken is minimal.

The solver is given an advantage for this problem. Its salesman moves 10% faster.

The generator outputs both an instance and a certificate solution. Solvers are scored based on how fast their
salesman can complete its tour.

## Instances

An instance contains the list of locations. Each location is a dict containing its x and y coordinates and the time
window it is available during.

```json
{
    "locations": [
        {
            "x": 0,
            "y": 0,
            "min_time": 0,
            "max_time": 1
        },
        {
            "x": 0,
            "y": 2,
            "min_time": 6,
            "max_time": 7
        },
        {
            "x": 1,
            "y": 1,
            "min_time": 2,
            "max_time": 9
        },
        {
            "x": 0,
            "y": 2,
            "min_time": 3,
            "max_time": 3
        },
        {
            "x": 2,
            "y": 2,
            "min_time": 2,
            "max_time": 6
        }
    ]
}
```

## Solutions

Solutions just contain the tour of locations in the order they are visited.

```json
{
    "tour": [0, 3, 4, 1, 2]
}
```
