"""Main module of the Pairsum problem."""
from pydantic import Field

from algobattle.problem import Problem, InstanceModel, SolutionModel, ValidationError
from algobattle.util import u64, Role


class Instance(InstanceModel):

    numbers: list[int] = Field(min_items=4, ge=0, le=2**63 - 1)

    @property
    def size(self) -> int:
        return len(self.numbers)


class Solution(SolutionModel[Instance]):
    """A solution to a Pairsum problem."""

    indices: tuple[u64, u64, u64, u64]

    def validate_solution(self, instance: Instance, role: Role) -> None:
        super().validate_solution(instance, role)
        if any(i >= len(instance.numbers) for i in self.indices):
            raise ValidationError("Solution index is out of range.")
        if len(self.indices) != len(set(self.indices)):
            raise ValidationError("Solution contains duplicate indices.")
        first = instance.numbers[self.indices[0]] + instance.numbers[self.indices[1]]
        second = instance.numbers[self.indices[2]] + instance.numbers[self.indices[3]]
        if first != second:
            raise ValidationError("Solution elements don't have the same sum.")


Pairsum = Problem(
    name="Pairsum",
    min_size=4,
    instance_cls=Instance,
    solution_cls=Solution,
)
