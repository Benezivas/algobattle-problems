"""The C4subgraphiso problem class."""
from typing import ClassVar

from algobattle.problem import UndirectedGraph, SolutionModel, ValidationError
from algobattle.util import u64


class C4subgraphiso(UndirectedGraph):
    """The C4subgraphiso problem class."""

    name: ClassVar[str] = "Square Subgraph Isomorphism"
    min_size: ClassVar[int] = 4

    class Solution(SolutionModel):
        """A solution to a Square Subgraph Isomorphism problem."""

        direction: ClassVar = "maximize"

        squares: set[tuple[u64, u64, u64, u64]]

        def validate_solution(self, instance: "C4subgraphiso") -> None:
            super().validate_solution(instance)
            self._all_entries_bounded_in_size(instance)
            self._all_squares_in_instance(instance)
            self._all_squares_node_disjoint()
            self._all_squares_induced(instance)

        def _all_entries_bounded_in_size(self, instance: "C4subgraphiso") -> None:
            for square in self.squares:
                if any(node >= instance.num_vertices for node in square):
                    raise ValidationError("An element of the solution doesn't index an instance vertex.")

        def _all_squares_node_disjoint(self) -> None:
            used_nodes = set()
            for square in self.squares:
                for node in square:
                    if node in used_nodes:
                        raise ValidationError(
                            "A square in the solution is not node-disjoint to at least one other square."
                        )
                    used_nodes.add(node)

        def _all_squares_induced(self, instance: "C4subgraphiso") -> None:
            edge_set = set(instance.edges)
            for square in self.squares:
                # Edges between opposing nodes of a square would mean the square is not induced by its nodes
                unwanted_edges = [
                    (square[0], square[2]),
                    (square[2], square[0]),
                    (square[1], square[3]),
                    (square[3], square[1]),
                ]
                if any(edge in edge_set for edge in unwanted_edges):
                    raise ValidationError("A square in the solution is not induced in the instance.")

        def _all_squares_in_instance(self, instance: "C4subgraphiso") -> None:
            edge_set = set(instance.edges)
            for square in self.squares:
                if (
                    not ((square[0], square[1]) in edge_set or (square[1], square[0]) in edge_set)
                    or not ((square[1], square[2]) in edge_set or (square[2], square[1]) in edge_set)
                    or not ((square[2], square[3]) in edge_set or (square[3], square[2]) in edge_set)
                    or not ((square[3], square[0]) in edge_set or (square[0], square[3]) in edge_set)
                ):
                    raise ValidationError("A square is not part of the instance.")

        def score(self, instance: "C4subgraphiso") -> float:
            return len(self.squares)
