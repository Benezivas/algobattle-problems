"""The Clusterediting problem class."""
from typing import ClassVar

from algobattle.problem import UndirectedGraph, SolutionModel, ValidationError
from algobattle.util import u64


class Domset(UndirectedGraph):
    """The DomSet problem class."""

    name: ClassVar[str] = "Dominating Set"
    min_size: ClassVar[int] = 2

    class Solution(SolutionModel):
        """A solution to a Dominating Set problem"""

        domset: set[u64]

        direction: ClassVar = "minimize"

        def validate_solution(self, instance: "Domset") -> None:
            if any(u >= instance.num_vertices for u in self.domset):
                raise ValidationError(
                    "A number in the domset is too large to be a vertex"
                )

            dominated = set(self.domset)
            for u, v in instance.edges:
                if u in self.domset:
                    dominated.add(v)
                elif v in self.domset:
                    dominated.add(u)
            if len(dominated) != instance.num_vertices:
                raise ValidationError(
                    "Not every vertex is dominated.",
                    detail=f"{instance.num_vertices - len(dominated)} vertices are not dominated",
                )

        def score(self, instance: "Domset") -> float:
            return len(self.domset)
