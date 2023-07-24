"""The OSCM3 problem class."""
from algobattle.problem import Problem, InstanceModel, SolutionModel, ValidationError, minimize
from algobattle.util import u64, Role


class Instance(InstanceModel):
    """The OSCM3 problem class."""

    neighbors: dict[u64, set[u64]]

    @property
    def size(self) -> int:
        return max(self.neighbors.keys()) + 1

    def validate_instance(self) -> None:
        super().validate_instance()
        size = self.size
        if any(not 0 <= v < size for v in self.neighbors):
            raise ValidationError("Instance contains element of V_1 out of the permitted range.")
        if any(not 0 <= v < size for neighbors in self.neighbors.values() for v in neighbors):
            raise ValidationError("Instance contains element of V_2 out of the permitted range.")
        if any(len(neighbors) > 3 for neighbors in self.neighbors.values()):
            raise ValidationError("A vertex of V_1 has more than 3 neighbors.")
        for u in range(size):
            self.neighbors.setdefault(u, set())


class Solution(SolutionModel[Instance]):
    """A solution to a One-Sided Crossing Minimization-3 problem."""

    vertex_order: list[u64]

    def validate_solution(self, instance: Instance, role: Role) -> None:
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
