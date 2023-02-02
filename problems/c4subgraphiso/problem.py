"""The C4subgraphiso problem class."""
import logging

from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel

logger = logging.getLogger('algobattle.problems.c4subgraphiso')


class C4subgraphiso(UndirectedGraph):
    """The C4subgraphiso problem class."""

    name: ClassVar[str] = "Square Subgraph Isomorphism"
    min_size: ClassVar[int] = 4

    class Solution(SolutionModel):
        """A solution to a Square Subgraph Isomorphism problem."""

        direction: ClassVar = "maximize"

        squares: set[tuple[int, int, int, int]] = Field(ge=0)

        def check_semantics(self, instance: "C4subgraphiso", size: int) -> bool:
            edge_set = set(instance.edges)
            if not self.all_squares_disjoint(self.squares):
                return False

            for square in self.squares:
                if any(entry >= size for entry in square):
                    return False
                # Edges between opposing nodes of a square would mean the square is not induced by its nodes
                unwanted_edges = [(square[0], square[2]),
                                  (square[2], square[0]),
                                  (square[1], square[3]),
                                  (square[3], square[1])]
                if (not self.square_in_instance(square, instance) or any(edge in edge_set for edge in unwanted_edges)):
                    logger.error('At least one element of the solution is not an induced square in the input graph!')
                    return False
            return True


        def all_squares_disjoint(self, squares: set[list[int]]):
            """Check if all squares of the instance are node-disjoint."""
            used_nodes = set()
            for sol_square in squares:
                for sol_node in sol_square:
                    if sol_node in used_nodes:
                        logger.error('Not all squares of the solution are node-disjoint!')
                        return False
                    used_nodes.add(sol_node)
            return True

        def square_in_instance(self, square, instance):
            """Check if a given square is part of the given instance.

            Parameters
            ----------
            square : tuple
                A tuple of the form (i, j, k, l) which are sequentially connected to form a square.
            instance : list
                A set of edges of the form (i, j).

            Returns
            -------
            bool
                True if the square is part of the instance, False otherwise.
            """
            edge_set = set(instance.edges)
            if (not ((square[0], square[1]) in edge_set or (square[1], square[0]) in edge_set)
                    or not ((square[1], square[2]) in edge_set or (square[2], square[1]) in edge_set)
                    or not ((square[2], square[3]) in edge_set or (square[3], square[2]) in edge_set)
                    or not ((square[3], square[0]) in edge_set or (square[0], square[3]) in edge_set)):
                return False
            return True

        def score(self, size: int, instance: "C4subgraphiso") -> float:
            return len(self.squares)
