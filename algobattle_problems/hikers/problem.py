"""The Hikers problem class."""
from algobattle.problem import Problem, InstanceModel, SolutionModel, ValidationError, maximize, Scored
from algobattle.util import u64, Role


class HikersInstance(InstanceModel):
    """The Tsptimewindows problem class."""

    hikers: list[tuple[u64, u64]]

    @property
    def size(self) -> int:
        """The instance size is the number of hikers."""
        return len(self.hikers)

    def validate_instance(self) -> None:
        if any(min_size > max_size for min_size, max_size in self.hikers):
            raise ValidationError("One hiker's minimum group size is larger than their maximum group size.")


class Solution(SolutionModel[HikersInstance], Scored[HikersInstance]):
    """A solution to a Hikers problem."""

    assignments: dict[u64, u64]

    def validate_solution(self, instance: HikersInstance, role: Role) -> None:
        if any(hiker >= len(instance.hikers) for hiker in self.assignments):
            raise ValidationError("Solution contains hiker that is not in the instance.")

        group_sizes: dict[int, int] = {}
        for group in self.assignments.values():
            group_sizes[group] = group_sizes.get(group, 0) + 1

        for hiker, group in self.assignments.items():
            min_size, max_size = instance.hikers[hiker]
            if not (min_size <= group_sizes[group] <= max_size):
                raise ValidationError("A Hiker is not happy with their assignment!")

    @maximize
    def score(self, instance: HikersInstance) -> float:
        return len(self.assignments)


Hikers = Problem(
    name="Hikers",
    min_size=5,
    instance_cls=HikersInstance,
    solution_cls=Solution,
)
