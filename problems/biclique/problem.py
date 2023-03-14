"""The Biclique problem class."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel

logger = logging.getLogger('algobattle.problems.biclique')


class Biclique(UndirectedGraph):
    """The Biclique problem class."""

    name: ClassVar[str] = "Bipartite Clique"
    min_size: ClassVar[int] = 5

    class Solution(SolutionModel):
        """A solution to a bipartite clique problem"""

        direction: ClassVar = "maximize"

        s_1: set[int] = Field(ge=0)
        s_2: set[int] = Field(ge=0)

        def is_valid(self, instance: "Biclique", size: int) -> bool:
            edge_set = set(instance.edges) | set(edge[::-1] for edge in instance.edges)
            return (
                all(i < instance.num_vertices for i in self.s_1)
                and all(i < instance.num_vertices for i in self.s_2)
                and len(self.s_1.intersection(self.s_2)) == 0
                and all((u, v) in edge_set for u in self.s_1 for v in self.s_2)
                and all((u, v) not in edge_set or u == v for u in self.s_1 for v in self.s_1)
                and all((u, v) not in edge_set or u == v for u in self.s_2 for v in self.s_2)
            )

        def score(self, size: int, instance: "Biclique") -> float:
            return len(self.s_1) + len(self.s_2)
