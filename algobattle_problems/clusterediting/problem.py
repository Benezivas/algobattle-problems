"""The Clusterediting problem class."""
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel, ValidationError


class Clusterediting(UndirectedGraph):
    """The Clusterediting problem class."""

    name: ClassVar[str] = "Cluster Editing"
    min_size: ClassVar[int] = 4

    class Solution(SolutionModel):
        """A solution to a Cluster Editing problem"""

        direction: ClassVar = "minimize"

        add: set[tuple[int, int]] = Field(ge=0, le=2 ** 63 - 1)
        delete: set[tuple[int, int]] = Field(ge=0, le=2 ** 63 - 1)

        def validate_solution(self, instance: "Clusterediting") -> None:
            edge_set = set(instance.edges)

            # Apply modifications to graph
            for edge in self.add:
                if edge[::-1] not in edge_set:
                    edge_set.add(edge)
            for edge in self.delete:
                if edge in edge_set:
                    edge_set.remove(edge)
                elif (edge[1], edge[0]) in edge_set:
                    edge_set.remove((edge[1], edge[0]))
                else:
                    raise ValidationError("Solution contains edge not found in instance.")

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
                            raise ValidationError("The solution does not triangulate the graph!")

        def score(self, instance: "Clusterediting") -> float:
            return len(self.add) + len(self.delete)
