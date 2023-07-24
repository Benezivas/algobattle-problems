"""The OSCM3 problem class."""
from typing import Annotated
from algobattle.problem import Problem, InstanceModel, SolutionModel, minimize
from algobattle.util import Role, ValidationError
from algobattle.types import u64, Vertex, MaxLen


class Instance(InstanceModel):
    """The OSCM3 problem class."""

    neighbors: dict[Vertex, Annotated[set[Vertex], MaxLen(3)]]

    @property
    def size(self) -> int:
        return max(self.neighbors.keys()) + 1

    def validate_instance(self) -> None:
        super().validate_instance()
        for u in range(self.size):
            self.neighbors.setdefault(u, set())


class Solution(SolutionModel[Instance]):
    """A solution to a One-Sided Crossing Minimization-3 problem."""

    vertex_order: list[u64]

    def validate_solution(self, instance: Instance, role: Role) -> None:
        super().validate_solution(instance, role)
        if any(not 0 <= i < instance.size for i in self.vertex_order):
            raise ValidationError("An element of the solution is not in the permitted range.")
        if len(self.vertex_order) != len(set(self.vertex_order)):
            raise ValidationError("The solution contains duplicate numbers.")
        if len(self.vertex_order) != instance.size:
            raise ValidationError("The solution does not order the whole instance.")

    @minimize
    def score(self, instance: Instance, role: Role) -> float:
        score = 0
        for position, vertex in enumerate(self.vertex_order):
            for i in instance.neighbors[vertex]:
                score += sum(j < i for other in self.vertex_order[position:] for j in instance.neighbors[other])
        return score


OSCM3 = Problem(
    name="One-Sided Crossing Minimization-3",
    min_size=1,
    instance_cls=Instance,
    solution_cls=Solution,
)
