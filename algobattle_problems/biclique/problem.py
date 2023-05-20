"""The Biclique problem class."""
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel, ValidationError


class Biclique(UndirectedGraph):
    """The Biclique problem class."""

    name: ClassVar[str] = "Bipartite Clique"
    min_size: ClassVar[int] = 5

    class Solution(SolutionModel):
        """A solution to a bipartite clique problem"""

        direction: ClassVar = "maximize"

        s_1: set[int] = Field(ge=0, le=2**63 - 1)
        s_2: set[int] = Field(ge=0, le=2**63 - 1)

        def validate_solution(self, instance: "Biclique") -> None:
            edge_set = set(instance.edges) | set(edge[::-1] for edge in instance.edges)
            super().validate_solution(instance)
            if any(i >= instance.num_vertices for i in self.s_1 | self.s_2):
                raise ValidationError("Solution contains vertices that aren't in the instance.")
            if len(self.s_1.intersection(self.s_2)) != 0:
                raise ValidationError("Solution contains vertex sets that aren't disjoint.")
            if any((u, v) not in edge_set for u in self.s_1 for v in self.s_2):
                raise ValidationError("The instance graph is missing an edge between the solution vertex sets.")
            if (any((u, v) in edge_set for u in self.s_1 for v in self.s_1)
                or any((u, v) in edge_set for u in self.s_2 for v in self.s_2)):
                raise ValidationError("The solution is not a bipartite graph.")

        def score(self, instance: "Biclique") -> float:
            return len(self.s_1) + len(self.s_2)
