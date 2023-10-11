"""The Longestpathboundedfvs problem class."""
from math import sqrt

from pydantic import Field
from networkx import Graph
from networkx.algorithms.tree.recognition import is_forest
from networkx.classes.function import is_empty

from algobattle.problem import Problem, SolutionModel, maximize
from algobattle.util import Role, ValidationError
from algobattle.types import Vertex, UndirectedGraph


class Instance(UndirectedGraph):
    """The Longestpathboundedfvs problem class."""

    fvs: set[Vertex] = Field(exclude=True)

    def validate_instance(self) -> None:
        super().validate_instance()
        if len(self.fvs) > sqrt(self.size):
            raise ValidationError(
                "The given feedback vertex set does not fit the size bound.",
                detail=f"Given fvs has size {len(self.fvs)}, bound is {sqrt(self.size)}.",
            )
        if not self.valid_fvs_on_input():
            raise ValidationError("The given feedback vertex set is not valid.")

    def valid_fvs_on_input(self) -> bool:
        g = Graph()
        for edge in self.edges:
            g.add_edge(*edge)
        for node in self.fvs:
            if g.has_node(node):
                g.remove_node(node)
        return is_empty(g) or is_forest(g)


class Solution(SolutionModel[Instance]):
    """A solution to a Longest Path with Bounded Feedback Vertex Set problem."""

    path: list[Vertex]

    def validate_solution(self, instance: Instance, role: Role) -> None:
        super().validate_solution(instance, role)
        if not self._nodes_are_walk(instance):
            raise ValidationError("The given path is not a walk in the instance graph.")
        if not self._no_revisited_nodes():
            raise ValidationError("The given path contains repeated nodes.")

    def _nodes_are_walk(self, instance: Instance) -> bool:
        edge_set = set(instance.edges)
        g = Graph()
        for edge in edge_set:
            g.add_edge(edge[0], edge[1])
        for i in range(len(self.path) - 1):
            if not g.has_edge(self.path[i], self.path[i + 1]):
                return False
        return True

    def _no_revisited_nodes(self) -> bool:
        return len(self.path) == len(set(self.path))

    @maximize
    def score(self, instance: Instance, role: Role) -> float:
        return len(self.path)


Longestpathboundedfvs = Problem(
    name="Longest Path with Bounded Feedback Vertex Set",
    min_size=3,
    instance_cls=Instance,
    solution_cls=Solution,
)
