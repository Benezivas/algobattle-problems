"""The Biclique problem class."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, Optimization, OptimiztionSolution

logger = logging.getLogger('algobattle.problems.biclique')


class Biclique(UndirectedGraph, Optimization):
    """The Biclique problem class."""

    name: ClassVar[str] = "Bipartite Clique"
    min_size: ClassVar[int] = 5

    class Solution(OptimiztionSolution):
        """A solution to a bipartite clique problem"""

        s_1: set[int] = Field(ge=0)
        s_2: set[int] = Field(ge=0)

        def check_semantics(self, size: int, instance: "Biclique") -> bool:
            edge_set = set(instance.edges)
            return (
                all(i < instance.num_vertices for i in self.s_1)
                and all(i < instance.num_vertices for i in self.s_2)
                and len(self.s_1.intersection(self.s_2)) != 0
                and all((u, v) in edge_set or (v, u) in edge_set for u in self.s_1 for v in self.s_2)
            )

        def score(self, size: int, instance: "Biclique") -> float:
            return len(self.s_1) + len(self.s_2)
