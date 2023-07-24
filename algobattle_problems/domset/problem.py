"""The Clusterediting problem class."""
from algobattle.problem import Problem, SolutionModel, minimize, Scored
from algobattle.util import Role, ValidationError
from algobattle.types import Vertex, UndirectedGraph


class Solution(SolutionModel[UndirectedGraph], Scored[UndirectedGraph]):
    """A solution to a Dominating Set problem."""

    domset: set[Vertex]

    def validate_solution(self, instance: UndirectedGraph, role: Role) -> None:
        dominated = set(self.domset)
        for u, v in instance.edges:
            if u in self.domset:
                dominated.add(v)
            elif v in self.domset:
                dominated.add(u)
        if len(dominated) != instance.num_vertices:
            raise ValidationError(
                "Not every vertex is dominated.",
                detail=f"{instance.num_vertices - len(dominated)} vertices are not dominated",
            )

    @minimize
    def score(self, instance: UndirectedGraph) -> float:
        return len(self.domset)


Domset = Problem(
    name="Dominating Set",
    min_size=2,
    instance_cls=UndirectedGraph,
    solution_cls=Solution,
)
