import logging

from algobattle.problem import Problem
from .parser import DomsetParser
from .verifier import DomsetVerifier

logger = logging.getLogger('algobattle.problems.domset')


class Domset(Problem):
    """The DomSet problem class."""

    name = 'Dominating Set'
    n_start = 6
    parser = DomsetParser()
    verifier = DomsetVerifier()
    approximable = True
