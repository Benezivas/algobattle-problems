"""The Biclique problem class."""
from algobattle.problem import Problem, SolutionModel, Scored, maximize
from algobattle.util import Role, ValidationError
from algobattle.types import UndirectedGraph, Vertex


class Solution(SolutionModel[UndirectedGraph], Scored[UndirectedGraph]):
    """A solution to a bipartite clique problem."""

    s_1: set[Vertex]
    s_2: set[Vertex]

    def validate_solution(self, instance: UndirectedGraph, role: Role) -> None:
        super().validate_solution(instance, role)
        edge_set = set(instance.edges) | set(edge[::-1] for edge in instance.edges)
        if len(self.s_1.intersection(self.s_2)) != 0:
            raise ValidationError("Solution contains vertex sets that aren't disjoint.")
        if any((u, v) not in edge_set for u in self.s_1 for v in self.s_2):
            raise ValidationError("The instance graph is missing an edge between the solution vertex sets.")
        if any((u, v) in edge_set for u in self.s_1 for v in self.s_1) or any(
            (u, v) in edge_set for u in self.s_2 for v in self.s_2
        ):
            raise ValidationError("The solution is not a bipartite graph.")

    @maximize
    def score(self, instance: UndirectedGraph) -> float:
        return len(self.s_1) + len(self.s_2)


Biclique = Problem(
    name="Bipartite Clique",
    instance_cls=UndirectedGraph,
    solution_cls=Solution,
    min_size=5,
)
