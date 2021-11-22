# Algorithmic Battle: Problems
Collection of problems to be used in the [algobattle](https://github.com/Benezivas/algobattle) project.

This repository contains several problem tasks that you may use for your
students. Each problem directory contains a `README.md` describing the problem
and the I/O that the generator and solver use. The `generator` and `solver`
directories contain dummy solvers that output instances which are technically
legal, but rather unexiting.

The simplest problem is currently the `pairsum` problem, which is well suited
as a primer task at the start of the lab. For this task, a simple randomized generator and solver are 
implemented which you may use to see how the program behaves when the
solver runs into a timeout at some instance size.

# Setup and Usage
Clone the [algobattle](https://github.com/Benezivas/algobattle) repository:
```
git clone https://github.com/Benezivas/algobattle.git
```
Follow the installation and usage instructions in the `README`.
Use the specific problem folders as input paths for the `battle` script.