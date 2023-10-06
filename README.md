# Algorithmic Battle: Problems
Collection of example problems that are ready to be used in the
[algobattle](https://algobattle.org) project, with a strong bias towards
problems of theoretical computer science.

Each problem directory contains a `description.md` describing the problem
and the I/O that the generator and solver use. The `generator` and `solver`
directories contain dummy solvers that output instances which are technically
legal, but rather unexiting. Finally, the `problem.py` implements the logic
described in the `description.md`.

# Setup and Usage
You need the [algobattle](https://github.com/Benezivas/algobattle) tool to use
any of the problems of this repository. Consult the
[official documentation](https://algobattle.org/docs)
on how to install the algobattle tool and how to use it for a given problem.

If you are using the [algobattle-web framework](https://github.com/Benezivas/algobattle-web),
you can simply import these problems in the framework. Consult the documentation
of the `algobattle-web` framework for more details.

A good and simple problem to start is the `pairsum` problem, which is well
suited as a primer task at the start of a lab course, should you want to host
one yourself.  For this task, a simple randomized generator and solver are
implemented which you may use to see how the everything behaves realistically.

# Compatibility
The head of the main branch of this repository is always compatible with
the head of the main branch of the [algobattle repository](https://github.com/Benezivas/algobattle).

If you are using an older version of `algobattle`, see the releases of this
repository in order to find versions of problems that are compatible with older
releases. We do not actively back-port problems to older versions of
`algobattle`.