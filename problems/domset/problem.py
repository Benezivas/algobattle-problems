"""The Clusterediting problem class."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel

logger = logging.getLogger('algobattle.problems.domset')


class Domset(UndirectedGraph):
    """The DomSet problem class."""

    name: ClassVar[str] = "Dominating Set"
    min_size: ClassVar[int] = 2

    class Solution(SolutionModel):
        """A solution to a Dominating Set problem"""

        direction: ClassVar = "minimize"
        domset: tuple[int, ...] = Field(ge=0)

        def is_valid(self, instance: "Domset", size: int) -> bool:
            edge_set = set(instance.edges)
            all_nodes = set()
            closed_neighborhood = {}
            for edge in edge_set:
                closed_neighborhood[edge[0]] = closed_neighborhood.get(edge[0], set())
                closed_neighborhood[edge[1]] = closed_neighborhood.get(edge[1], set())
                closed_neighborhood[edge[0]].add(edge[0])
                closed_neighborhood[edge[0]].add(edge[1])
                closed_neighborhood[edge[1]].add(edge[0])
                closed_neighborhood[edge[1]].add(edge[1])
                all_nodes.add(edge[0])
                all_nodes.add(edge[1])

            dominated_nodes = set()
            for node in self.domset:
                dominated_nodes.update(closed_neighborhood[node])

            if all_nodes != dominated_nodes:
                logger.error('The solution set does not dominate all nodes!')
                return False

            return True

        def score(self, size: int, instance: "Domset") -> float:
            return len(self.domset)
