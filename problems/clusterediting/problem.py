"""The Clusterediting problem class."""
import logging

from algobattle.problem import Problem
from .parser import ClustereditingParser
from .verifier import ClustereditingVerifier

logger = logging.getLogger('algobattle.problems.clusterediting')


class Clusterediting(Problem):
    """The Clusterediting problem class."""

    name = 'Cluster Editing'
    n_start = 4
    parser = ClustereditingParser()
    verifier = ClustereditingVerifier()
    approximable = True
