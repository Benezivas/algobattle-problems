# The Job Shop Scheduling Problem
There are many variants of the *Job Shop Scheduling* Problem. In this variant our job is to schedule jobs onto 5
machines of different execution speed. Our goal is to minimize the *makespan*, i.e. the latest job completion time over
all machines.

**Given**: `n` jobs and 5 machines of different execution speeds  
**Problem**: Find a distribution of the jobs onto the machines that minimizes the *makespan*.

The index of a machine indicates its speed, specifically how much the machine slows down the execution of a job. Machine
1 runs the jobs normally, while e.g. machine three slows down execution time by a factor of three.

The generator outputs both an instance and a certificate solution. Solvers are scored based on how fast their
solution's makespan is compared to the generator's.

## Instance

An instance contains the list of job lengths. For example:

```json
{
    "job_lengths": [30, 120, 24, 40, 60]
}
```

## Solution

A solution contains a list of the machine numbers each job is assigned to. For example:

```json
{
    "assignments": [4, 1, 5, 3, 2]
}
```

This solution assigns the first job (with a runtime of 30) to the fourth machine, the second to the first, etc. The
total makespan of it is 120.
