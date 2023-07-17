"""The PathPacking problem class."""

from algobattle.problem import Problem, UndirectedGraph, SolutionModel, ValidationError, Scored, maximize
from algobattle.util import Role
from algobattle.types import u64


class Solution(SolutionModel[UndirectedGraph], Scored[UndirectedGraph]):
    """A solution to a Path Packing problem."""

    paths: set[tuple[u64, u64, u64]]

    def validate_solution(self, instance: UndirectedGraph, role: Role) -> None:
        if not self.all_paths_disjoint(self.paths):
            raise ValidationError("Not all paths in the solution are node-disjoint.")
        for path in self.paths:
            if any(entry >= instance.num_vertices for entry in path):
                raise ValidationError("Solution contains index that is not a valid vertex.")
            if not self.path_in_instance(path, instance):
                raise ValidationError("Solution contains path that is not part of the instance.")

    def all_paths_disjoint(self, paths: set[tuple[int, int, int]]):
        """Check if all paths of the instance are node-disjoint."""
        used_nodes = {u for path in paths for u in path}
        return len(paths) * 3 == len(used_nodes)

    def path_in_instance(self, path: tuple[int, int, int], instance: UndirectedGraph) -> bool:
        """Check if a given path is part of the given instance."""
        edge_set = set(instance.edges)
        edge_set |= {(v, u) for u, v in edge_set}
        u, v, w = path
        return (u, v) in edge_set and (v, w) in edge_set

    @maximize
    def score(self, instance: UndirectedGraph) -> float:
        return len(self.paths)

Pathpacking = Problem(
    name="P_3 Path Packing",
    min_size=3,
    instance_cls=UndirectedGraph,
    solution_cls=Solution,
)
