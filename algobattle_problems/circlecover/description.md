# The Circle Cover Problem

The _Circle Cover_ problem is a geometric problem where circles of fixed sizes need to be placed in the plane to cover
as many points as possible. We restrict the plane to only include coordinates in `0 <= x, y <= 100` with
fractional coordinates being allowed. Each circle has a different predetermined radius of `10`, `20`, and `30`, the only
choice to be made is where to place each one.

# Instance
An instance is a set of coordinate pairs `[x, y]` with each coordinate being within `0 <= x, y, <= 100`. Its size is
the number of points it contains. For example:
```json
{
    "points": [
        [0, 1],
        [50, 50],
        [100, 17]
    ]
}
```

# Solution
A solution contains the coordinates of the center of each of the circles. They are stored as a mapping from their radius
to their center coordinate. It is scored based on how many of the instance's points are covered by the circles.

```json
{
    "circles": {
        "10": [5, 5],
        "20": [60, 65],
        "30": [80, 10]
    }
}
```
