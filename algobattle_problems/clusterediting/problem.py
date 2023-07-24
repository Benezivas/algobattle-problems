"""The Clusterediting problem class."""
from collections import defaultdict
from itertools import combinations

from algobattle.problem import Problem, SolutionModel, minimize, Scored
from algobattle.util import Role, ValidationError
from algobattle.types import Vertex, UndirectedGraph


class Solution(SolutionModel[UndirectedGraph], Scored[UndirectedGraph]):
    """A solution to a Cluster Editing problem."""

    add: set[tuple[Vertex, Vertex]]
    delete: set[tuple[Vertex, Vertex]]

    def validate_solution(self, instance: UndirectedGraph, role: Role) -> None:
        super().validate_solution(instance, role)
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

        neighbors: defaultdict[int, set[int]] = defaultdict(set)
        for u, v in edge_set:
            neighbors[u].add(v)
            neighbors[v].add(u)

        for u in range(instance.num_vertices):
            for v, w in combinations(neighbors[u], 2):
                if not (v, w) in edge_set and not (w, v) in edge_set:
                    raise ValidationError("The solution does not transform the graph into a cluster.")

    @minimize
    def score(self, instance: UndirectedGraph) -> float:
        return len(self.add) + len(self.delete)


Clusterediting = Problem(
    name="Cluster Editing",
    min_size=4,
    instance_cls=UndirectedGraph,
    solution_cls=Solution,
)
