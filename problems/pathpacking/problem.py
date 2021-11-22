"""The PathPacking problem class."""
import logging

from algobattle.problem import Problem
from .parser import PathpackingParser
from .verifier import PathpackingVerifier

logger = logging.getLogger('algobattle.problems.pathpacking')


class Pathpacking(Problem):
    """The PathPacking problem class."""

    name = 'P_3 Path Packing'
    n_start = 4
    parser = PathpackingParser()
    verifier = PathpackingVerifier()
    approximable = True
