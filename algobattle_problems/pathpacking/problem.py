"""The PathPacking problem class."""
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel, ValidationError, Scored


class Pathpacking(UndirectedGraph):
    """The Path Packing problem class."""

    name: ClassVar[str] = "P_3 Path Packing"
    min_size: ClassVar[int] = 3

    class Solution(SolutionModel, Scored):
        """A solution to a Path Packing problem."""

        direction: ClassVar = "maximize"

        paths: set[tuple[int, int, int]] = Field(ge=0)

        def validate_solution(self, instance: "Pathpacking") -> None:
            if not self.all_paths_disjoint(self.paths):
                raise ValidationError("Not all paths in the solution are node-disjoint.")
            for path in self.paths:
                if any(entry >= instance.num_vertices for entry in path):
                    raise ValidationError("Solution contains index that is not a valid vertex.")
                if not self.path_in_instance(path, instance):
                    raise ValidationError("Solution contains path that is not part of the instance.")

        def all_paths_disjoint(self, paths: set[tuple[int, int, int]]):
            """Check if all paths of the instance are node-disjoint."""
            used_nodes = set()
            for sol_path in paths:
                for sol_node in sol_path:
                    if sol_node in used_nodes:
                        return False
                    used_nodes.add(sol_node)
            return True

        def path_in_instance(self, path: tuple[int, int, int], instance: "Pathpacking") -> bool:
            """Check if a given path is part of the given instance."""
            edge_set = set(instance.edges)
            edge_set.update((v, u) for u, v in edge_set)
            u, v, w = path
            return (u, v) in edge_set and (v, w) in edge_set

        def score(self, instance: "Pathpacking") -> float:
            return len(self.paths)
