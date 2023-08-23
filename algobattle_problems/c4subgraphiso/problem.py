"""The C4subgraphiso problem class."""

from itertools import combinations, cycle, islice
from typing import Annotated, Iterator
from pydantic import field_validator

from algobattle.problem import Problem, SolutionModel, maximize
from algobattle.util import Role, ValidationError
from algobattle.types import UndirectedGraph, Vertex, UniqueItems

Square = Annotated[tuple[Vertex, Vertex, Vertex, Vertex], UniqueItems()]
def edges(square: Square) -> Iterator[tuple[Vertex, Vertex]]:
    """Returns all edges of a square."""
    return zip(square, islice(cycle(square), 1, None))
def diagonals(square: Square) -> Iterator[tuple[Vertex, Vertex]]:
    """Returns the diagonals of a square."""
    yield square[0], square[2]
    yield square[1], square[3]

class Solution(SolutionModel[UndirectedGraph]):
    """A solution to a Square Subgraph Isomorphism problem."""

    squares: set[Square]

    @field_validator("squares", mode="after")
    @classmethod
    def check_squares(cls, value: set[Square]) -> set[Square]:
        if any(set(a) & set(b) for a, b in combinations(value, 2)):
            raise ValueError("A square in the solution is not node-disjoint to at least one other square")
        return value

    def validate_solution(self, instance: UndirectedGraph, role: Role) -> None:
        super().validate_solution(instance, role)
        edge_set = set(instance.edges) | {(v, u) for u, v in instance.edges}
        if any(edge not in edge_set for square in self.squares for edge in edges(square)):
            raise ValidationError("A square is not part of the instance.")
        if any(edge in edge_set for square in self.squares for edge in diagonals(square)):
            raise ValidationError("A square in the solution is not induced in the instance.")

    @maximize
    def score(self, instance: UndirectedGraph, role: Role) -> float:
        return len(self.squares)


C4subgraphiso = Problem(
    name="Square Subgraph Isomorphism",
    instance_cls=UndirectedGraph,
    solution_cls=Solution,
    min_size=4,
)
