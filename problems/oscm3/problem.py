import logging

from algobattle.problem import Problem
from .parser import OSCM3Parser
from .verifier import OSCM3Verifier

logger = logging.getLogger('algobattle.problems.oscm3')


class OSCM3(Problem):
    """The OSCM3 problem class."""

    name = 'One-Sided Crossing Minimization-3'
    n_start = 3
    parser = OSCM3Parser()
    verifier = OSCM3Verifier()
    approximable = True
