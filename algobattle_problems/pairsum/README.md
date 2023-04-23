# The Pairsum Problem
The Pairsum problem is a simple task which proved to be a good primer task for students to get used to the environment.

The task is the following:

**Given**: List `L = [z_1,...,z_n]`, `z_i in [0,2^{63})`  
**Question**: Are there pairwise different `i_1,i_2,i_3,i_4 in [0,...,n-1]` such that `L[i_1] + L[i_2] = L[i_3] + L[i_4]`?  

Given such a list, the task is thus to find four numbers which can be divided up into two pairs such that the sum of one pair is the same as the sum of the other pair.

For a given `n in N` the generator is tasked with creating a *YES*-instance in the form of a list `L` of nonnegative integers of length `n` as described above. 
Additionally, it has to give four indices in the order `i_1,i_2,i_3,i_4` such that they form a valid solution.

The Solver receives this list `L` and is supposed to output four indices in order `i_1,i_2,i_3,i_4` which are also a valid solution. It may always assume that the instance is a *YES*-instance of size at least 4.

The generator should create a hard to solve instance, while the solver should be able to solve any kind of instance that is given in a quick way.

# I/O
The schema defining the solution and instance looks like this:
```json
{
    "title": "Pairsum",
    "description": "The pairsum problem class.",
    "type": "object",
    "properties": {
        "numbers": {
            "title": "Numbers",
            "minimum": 0,
            "maximum": 9223372036854775807,
            "minItems": 4,
            "type": "array",
            "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 9223372036854775807
            }
        },
        "solution": {
            "title": "Solution",
            "hidden": true,
            "allOf": [
                {
                    "$ref": "#/definitions/Solution"
                }
            ]
        }
    },
    "required": [
        "numbers",
        "solution"
    ],
    "definitions": {
        "Solution": {
            "title": "Solution",
            "description": "A solution to a Pairsum problem",
            "type": "object",
            "properties": {
                "indices": {
                    "title": "Indices",
                    "minimum": 0,
                    "minItems": 4,
                    "maxItems": 4,
                    "type": "array",
                    "items": {
                        "type": "integer",
                        "minimum": 0
                    }
                }
            },
            "required": [
                "indices"
            ]
        }
    }
}
```

The generator receives the number `n` at `/input/size` and outputs the instance `L` to `/output/instance/instance.json`.
A sample input and output for `n = 6` may look like this:  
Input:
```
6
```
Output:
```json
{
    "numbers": [0, 3, 1, 2, 5, 10],
    "solution": {
        "indices": [0, 1, 2, 3]
    }
}
```

The solver receives the generated instance at `/input/instance/instance.json` and outputs the solution to `/output/solution/solution.json`.
Applied to the the example above, the input and output may look like this:  
Input: 
```json
{
    "numbers": [0, 3, 1, 2, 5, 10]
}
```
Output:  
```json
{
    "indices": [4, 0, 1, 3]
}
```