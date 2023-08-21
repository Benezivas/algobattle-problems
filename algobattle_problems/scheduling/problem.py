"""The Scheduling problem class."""
from pydantic import Field

from algobattle.problem import Problem, InstanceModel, SolutionModel, ValidationError, minimize
from algobattle.util import Role


class Instance(InstanceModel):
    """The Scheduling problem class."""

    job_lengths: list[int] = Field(ge=0, le=(2**64 - 1) / 5)

    @property
    def size(self) -> int:
        return len(self.job_lengths)


class Solution(SolutionModel[Instance]):
    """A solution to a Job Shop Scheduling problem."""

    assignments: list[int] = Field(ge=1, le=5)

    def validate_solution(self, instance: Instance, role: Role) -> None:
        if len(self.assignments) != len(instance.job_lengths):
            raise ValidationError("The number of assigned jobs doesn't match the number of jobs.")

    @minimize
    def score(self, instance: Instance, role: Role) -> float:
        finish_time = [0] * 5
        for duration, machine in zip(instance.job_lengths, self.assignments):
            finish_time[machine - 1] += duration * machine
        return max(finish_time)


Scheduling = Problem(
    name="Job Shop Scheduling",
    min_size=5,
    instance_cls=Instance,
    solution_cls=Solution,
)
