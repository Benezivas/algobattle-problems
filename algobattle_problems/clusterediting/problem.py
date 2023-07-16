"""The Clusterediting problem class."""
from collections import defaultdict
from itertools import combinations
from typing import ClassVar

from algobattle.problem import Problem, UndirectedGraph, SolutionModel, ValidationError
from algobattle.util import u64


class Solution(SolutionModel[UndirectedGraph]):
    """A solution to a Cluster Editing problem."""

    direction: ClassVar = "minimize"

    add: set[tuple[u64, u64]]
    delete: set[tuple[u64, u64]]

    def validate_solution(self, instance: UndirectedGraph) -> None:
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

    def score(self, instance: UndirectedGraph) -> float:
        return len(self.add) + len(self.delete)


Clusterediting = Problem(
    name="Cluster Editing",
    min_size=4,
    instance_cls=UndirectedGraph,
    solution_cls=Solution,
)
