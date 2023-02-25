"""The PathPacking problem class."""
import logging

from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel

logger = logging.getLogger('algobattle.problems.pathpacking')


class Pathpacking(UndirectedGraph):
    """The C4subgraphiso problem class."""

    name: ClassVar[str] = "P_2 Path Packing"
    min_size: ClassVar[int] = 3

    class Solution(SolutionModel):
        """A solution to a P_2 Path Packing problem."""

        direction: ClassVar = "maximize"

        paths: set[tuple[int, int, int]] = Field(ge=0)

        def check_semantics(self, instance: "Pathpacking", size: int) -> bool:
            if not self.all_paths_disjoint(self.paths):
                return False

            for path in self.paths:
                if any(entry >= size for entry in path):
                    return False
                if (not self.path_in_instance(path, instance)):
                    logger.error(f"Path {path} is not part of the instance graph.")
                    return False
            return True

        def all_paths_disjoint(self, paths: set[list[int]]):
            """Check if all paths of the instance are node-disjoint."""
            used_nodes = set()
            for sol_path in paths:
                for sol_node in sol_path:
                    if sol_node in used_nodes:
                        logger.error('Not all paths of the solution are node-disjoint!')
                        return False
                    used_nodes.add(sol_node)
            return True

        def path_in_instance(self, path, instance):
            """Check if a given path is part of the given instance.

            Parameters
            ----------
            path : tuple
                A tuple of the form (i, j, k) which are sequentially connected to form a path.
            instance : list
                A set of edges of the form (i, j).

            Returns
            -------
            bool
                True if the path is part of the instance, False otherwise.
            """
            edge_set = set(instance.edges)
            if (not ((path[0], path[1]) in edge_set or (path[1], path[0]) in edge_set)
                    or not ((path[1], path[2]) in edge_set or (path[2], path[1]) in edge_set)):
                return False
            return True

        def score(self, size: int, instance: "Pathpacking") -> float:
            return len(self.paths)
