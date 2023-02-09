"""The Longestpathboundedfvs problem class."""
import logging

from typing import ClassVar
from pydantic import Field
import networkx as nx

from algobattle.problem import UndirectedGraph, SolutionModel

logger = logging.getLogger('algobattle.problems.longestpathboundedfvs')


class Longestpathboundedfvs(UndirectedGraph):
    """The Longestpathboundedfvs problem class."""

    name: ClassVar[str] = "Longest Path with Bounded Feedback Vertex Set"
    min_size: ClassVar[int] = 3
    fvs: tuple[int, ...] = Field(ge=0, hidden="solver")

    def check_semantics(self, size: int) -> bool:
        return (super().check_semantics(size)
                and len(self.fvs) <= size ** 0.5
                and self.valid_fvs_on_input()
                )

    def valid_fvs_on_input(self) -> bool:
        g = nx.Graph()
        for edge in self.edges:
            g.add_edge(edge[0], edge[1])
        for node in self.fvs:
            if g.has_node(node):
                g.remove_node(node)
        if not nx.is_empty(g):
            if not nx.algorithms.tree.recognition.is_forest(g):
                return False
        return True

    class Solution(SolutionModel):
        """A solution to a Longest Path with Bounded Feedback Vertex Set problem."""

        direction: ClassVar = "maximize"
        path: set[tuple[int, ...]] = Field(ge=0)

        def check_semantics(self, instance: "Longestpathboundedfvs", size: int) -> bool:
            return self._nodes_are_walk(instance) and self._no_revisited_nodes()

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

        def score(self, size: int, instance: "Longestpathboundedfvs") -> float:
            return len(self.path)
