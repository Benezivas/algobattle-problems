import logging

from algobattle.problem import Problem
from .parser import BicliqueParser
from .verifier import BicliqueVerifier

logger = logging.getLogger('algobattle.problems.biclique')


class Biclique(Problem):
    """The Biclique problem class."""

    name = 'Bipartite Clique'
    n_start = 5
    parser = BicliqueParser()
    verifier = BicliqueVerifier()
    approximable = True
