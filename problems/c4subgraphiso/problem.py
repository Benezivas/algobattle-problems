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

        def is_valid(self, instance: "C4subgraphiso", size: int) -> bool:
            return (
                self._all_entries_bounded_in_size(size)
                and self._all_squares_in_instance(instance)
                and self._all_squares_node_disjoint()
                and self._all_squares_induced(instance)
            )

        def _all_entries_bounded_in_size(self, size) -> bool:
            for square in self.squares:
                if any(node >= size for node in square):
                    logger.error(f"Square {square} has entries larger than the allowed size of {size}!")
            return True

        def _all_squares_node_disjoint(self) -> bool:
            used_nodes = set()
            for square in self.squares:
                for node in square:
                    if node in used_nodes:
                        logger.error(f"Node {node} of square {square} is not node-disjoint to at least one other square!")
                        return False
                    used_nodes.add(node)
            return True

        def _all_squares_induced(self, instance: "C4subgraphiso") -> bool:
            edge_set = set(instance.edges)
            for square in self.squares:
                # Edges between opposing nodes of a square would mean the square is not induced by its nodes
                unwanted_edges = [(square[0], square[2]),
                                  (square[2], square[0]),
                                  (square[1], square[3]),
                                  (square[3], square[1])]
                if any(edge in edge_set for edge in unwanted_edges):
                    logger.error(f"Square {square} is not induced in the instance!")
                    return False
            return True

        def _all_squares_in_instance(self, instance: "C4subgraphiso") -> bool:
            edge_set = set(instance.edges)
            for square in self.squares:
                if (not ((square[0], square[1]) in edge_set or (square[1], square[0]) in edge_set)
                        or not ((square[1], square[2]) in edge_set or (square[2], square[1]) in edge_set)
                        or not ((square[2], square[3]) in edge_set or (square[3], square[2]) in edge_set)
                        or not ((square[3], square[0]) in edge_set or (square[0], square[3]) in edge_set)):
                    logger.error(f"Square {square} is not part of the instance!")
                    return False
            return True

        def score(self, size: int, instance: "C4subgraphiso") -> float:
            return len(self.squares)
