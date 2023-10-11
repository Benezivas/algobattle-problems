"""The Hikers problem class."""
from collections import Counter
from algobattle.problem import Problem, InstanceModel, SolutionModel, maximize
from algobattle.util import Role, ValidationError
from algobattle.types import u64, SizeIndex


Hiker = SizeIndex


class HikersInstance(InstanceModel):
    """The Hikers instance class."""

    hikers: list[tuple[u64, u64]]

    @property
    def size(self) -> int:
        """The instance size is the number of hikers."""
        return len(self.hikers)

    def validate_instance(self) -> None:
        super().validate_instance()
        if any(min_size > max_size for min_size, max_size in self.hikers):
            raise ValidationError("One hiker's minimum group size is larger than their maximum group size.")


class Solution(SolutionModel[HikersInstance]):
    """A solution to a Hikers problem."""

    assignments: dict[Hiker, u64]

    def validate_solution(self, instance: HikersInstance, role: Role) -> None:
        super().validate_solution(instance, role)
        group_sizes = Counter(self.assignments.values())

        for hiker, group in self.assignments.items():
            min_size, max_size = instance.hikers[hiker]
            if not (min_size <= group_sizes[group] <= max_size):
                raise ValidationError("A Hiker is not happy with their assignment!")

    @maximize
    def score(self, instance: HikersInstance, role: Role) -> float:
        return len(self.assignments)


Hikers = Problem(
    name="Hikers",
    min_size=5,
    instance_cls=HikersInstance,
    solution_cls=Solution,
)
