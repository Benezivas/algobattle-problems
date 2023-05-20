"""The Scheduling problem class."""
from typing import ClassVar

from pydantic import Field

from algobattle.problem import ProblemModel, SolutionModel, ValidationError


class Scheduling(ProblemModel):
    """The Scheduling problem class."""

    name: ClassVar[str] = "Job Shop Scheduling"
    min_size: ClassVar[int] = 5

    job_lengths: list[int] = Field(ge=0, le=(2 ** 64 - 1) / 5)

    @property
    def size(self) -> int:
        return len(self.job_lengths)

    class Solution(SolutionModel):
        """A solution to a Job Shop Scheduling problem"""

        direction: ClassVar = "minimize"

        assignments: list[int] = Field(ge=1, le=5)

        def validate_solution(self, instance: "Scheduling") -> None:
            if len(self.assignments) != len(instance.job_lengths):
                raise ValidationError("The number of assigned jobs doesn't match the number of jobs.")

        def score(self, instance: "Scheduling") -> float:
            finish_time = [0] * 5
            for duration, machine in zip(instance.job_lengths, self.assignments):
                finish_time[machine - 1] += duration * machine
            return max(finish_time)
