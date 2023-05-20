"""The Longestpathboundedfvs problem class."""
from math import sqrt
from typing import ClassVar
from pydantic import Field
import networkx as nx

from algobattle.problem import UndirectedGraph, SolutionModel, Scored, ValidationError


class Longestpathboundedfvs(UndirectedGraph):
    """The Longestpathboundedfvs problem class."""

    name: ClassVar[str] = "Longest Path with Bounded Feedback Vertex Set"
    min_size: ClassVar[int] = 3
    fvs: set[int] = Field(ge=0, hidden="solver")

    def validate_instance(self, max_size: int) -> None:
        super().validate_instance(max_size)
        if len(self.fvs) > sqrt(max_size):
            raise ValidationError(
                "The given feedback vertex set does not fit the size bound.",
                detail=f"Given fvs has size {len(self.fvs)}, bound is {sqrt(max_size)}."
            )
        if not self.valid_fvs_on_input():
            raise ValidationError("The given feedback vertex set is not valid.")

    def valid_fvs_on_input(self) -> bool:
        g = nx.Graph()
        for edge in self.edges:
            g.add_edge(*edge)
        for node in self.fvs:
            if g.has_node(node):
                g.remove_node(node)
        return nx.is_empty(g) or nx.algorithms.tree.recognition.is_forest(g)

    class Solution(SolutionModel, Scored):
        """A solution to a Longest Path with Bounded Feedback Vertex Set problem."""

        path: list[int] = Field(ge=0)

        direction: ClassVar = "maximize"

        def validate_solution(self, instance: "Longestpathboundedfvs") -> None:
            if not self._nodes_are_walk(instance):
                raise ValidationError("The given path is not a walk in the instance graph.")
            if not self._no_revisited_nodes():
                raise ValidationError("The given path contains repeated nodes.")

        def _nodes_are_walk(self, instance) -> bool:
            edge_set = set(instance.edges)
            g = nx.Graph()
            for edge in edge_set:
                g.add_edge(edge[0], edge[1])
            for i in range(len(self.path) - 1):
                if not g.has_edge(self.path[i], self.path[i+1]):
                    return False
            return True

        def _no_revisited_nodes(self) -> bool:
            return len(self.path) == len(set(self.path))

        def score(self, instance: "Longestpathboundedfvs") -> float:
            return len(self.path)
