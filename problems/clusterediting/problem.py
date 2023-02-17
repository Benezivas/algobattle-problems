"""The Clusterediting problem class."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel

logger = logging.getLogger('algobattle.problems.clusterediting')


class Clusterediting(UndirectedGraph):
    """The Clusterediting problem class."""

    name: ClassVar[str] = "Cluster Editing"
    min_size: ClassVar[int] = 4

    class Solution(SolutionModel):
        """A solution to a Cluster Editing problem"""

        direction: ClassVar = "minimize"

        add: set[tuple[int, int]] = Field(ge=0)
        delete: set[tuple[int, int]] = Field(ge=0)

        def check_semantics(self, instance: "Clusterediting", size: int) -> bool:
            edge_set = set(instance.edges)

            # Apply modifications to graph
            for edge in self.add:
                edge_set.add(edge)
            for edge in self.delete:
                if edge in edge_set:
                    edge_set.remove(edge)
                elif (edge[1], edge[0]) in edge_set:
                    edge_set.remove((edge[1], edge[0]))

            if not self._is_triangulated(edge_set):
                logger.error('The solution does not triangulate the graph!')
                return False

            return True

        def _is_triangulated(self, edge_set) -> bool:
            for edge1 in edge_set:
                for edge2 in edge_set:
                    if edge1 != edge2:
                        check_edge = None
                        if edge1[0] == edge2[0]:
                            check_edge = (edge1[1], edge2[1])
                        elif edge1[0] == edge2[1]:
                            check_edge = (edge1[1], edge2[0])
                        elif edge1[1] == edge2[0]:
                            check_edge = (edge1[0], edge2[1])
                        elif edge1[1] == edge2[1]:
                            check_edge = (edge1[0], edge2[0])

                        if (check_edge
                            and check_edge not in edge_set
                            and (check_edge[1], check_edge[0]) not in edge_set):
                            logger.error(f'{check_edge}, {edge_set}')
                            return False
            return True

        def score(self, size: int, instance: "Clusterediting") -> float:
            return len(self.add) + len(self.delete)
