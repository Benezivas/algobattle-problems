"""The C4subgraphiso problem class."""
from typing import ClassVar
from pydantic import Field

from algobattle.problem import UndirectedGraph, SolutionModel, ValidationError


class C4subgraphiso(UndirectedGraph):
    """The C4subgraphiso problem class."""

    name: ClassVar[str] = "Square Subgraph Isomorphism"
    min_size: ClassVar[int] = 4

    class Solution(SolutionModel):
        """A solution to a Square Subgraph Isomorphism problem."""

        direction: ClassVar = "maximize"

        squares: set[tuple[int, int, int, int]] = Field(ge=0)

        def validate_solution(self, instance: "C4subgraphiso", size: int) -> None:
            super().validate_solution(instance, size)
            self._all_entries_bounded_in_size(size)
            self._all_squares_in_instance(instance)
            self._all_squares_node_disjoint()
            self._all_squares_induced(instance)

        def _all_entries_bounded_in_size(self, size) -> None:
            for square in self.squares:
                if any(node >= size for node in square):
                    raise ValidationError(f"Square {square} has entries larger than the allowed size of {size}!")

        def _all_squares_node_disjoint(self) -> None:
            used_nodes = set()
            for square in self.squares:
                for node in square:
                    if node in used_nodes:
                        raise ValidationError(f"Node {node} of square {square} is not node-disjoint to at least one other square!")
                    used_nodes.add(node)

        def _all_squares_induced(self, instance: "C4subgraphiso") -> None:
            edge_set = set(instance.edges)
            for square in self.squares:
                # Edges between opposing nodes of a square would mean the square is not induced by its nodes
                unwanted_edges = [(square[0], square[2]),
                                  (square[2], square[0]),
                                  (square[1], square[3]),
                                  (square[3], square[1])]
                if any(edge in edge_set for edge in unwanted_edges):
                    raise ValidationError(f"Square {square} is not induced in the instance!")

        def _all_squares_in_instance(self, instance: "C4subgraphiso") -> None:
            edge_set = set(instance.edges)
            for square in self.squares:
                if (not ((square[0], square[1]) in edge_set or (square[1], square[0]) in edge_set)
                        or not ((square[1], square[2]) in edge_set or (square[2], square[1]) in edge_set)
                        or not ((square[2], square[3]) in edge_set or (square[3], square[2]) in edge_set)
                        or not ((square[3], square[0]) in edge_set or (square[0], square[3]) in edge_set)):
                    raise ValidationError(f"Square {square} is not part of the instance!")

        def score(self, size: int, instance: "C4subgraphiso") -> float:
            return len(self.squares)
