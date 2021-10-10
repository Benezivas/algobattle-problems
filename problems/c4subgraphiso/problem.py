import logging

from algobattle.problem import Problem
from .parser import C4subgraphisoParser
from .verifier import C4subgraphisoVerifier

logger = logging.getLogger('algobattle.problems.c4subgraphiso')


class C4subgraphiso(Problem):
    """The C4subgraphiso problem class."""

    name = 'Square Subgraph Isomorphism'
    n_start = 4
    parser = C4subgraphisoParser()
    verifier = C4subgraphisoVerifier()
    approximable = True
