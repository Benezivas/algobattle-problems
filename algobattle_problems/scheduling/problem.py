"""The Scheduling problem class."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import ProblemModel, SolutionModel

logger = logging.getLogger('algobattle.problems.scheduling')


class Scheduling(ProblemModel):
    """The Scheduling problem class."""

    name: ClassVar[str] = "Job Shop Scheduling"
    min_size: ClassVar[int] = 5

    job_lengths: tuple[int, ...] = Field(ge=0, le=(2 ** 64) / 5)

    def is_valid(self, size: int) -> bool:
        return (
            len(self.job_lengths) <= size
        )

    class Solution(SolutionModel):
        """A solution to a Job Shop Scheduling problem"""

        direction: ClassVar = "minimize"

        assignments: list[tuple[int, int]] = Field(ge=0)

        def is_valid(self, instance: "Scheduling", size: int) -> bool:
            assigned_jobs = [job for job, _ in self.assignments]
            return (
                all(machine < 5 and job < len(instance.job_lengths) for job, machine in self.assignments)
                and len(assigned_jobs) == len(set(assigned_jobs))
                and len(self.assignments) == len(instance.job_lengths)
            )

        def score(self, instance: "Scheduling", size: int) -> float:
            finish_time = [0 for i in range(5)]

            for assignment in self.assignments:
                job, machine = assignment
                finish_time[machine] += (machine + 1) * instance.job_lengths[job]

            return max(finish_time)
