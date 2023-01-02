"""Main module of the Pairsum problem."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import ProblemModel, SolutionModel

logger = logging.getLogger('algobattle.problems.pairsum')


class Pairsum(ProblemModel):
    """The pairsum problem."""

    name: ClassVar[str] = "Pairsum"
    min_size: ClassVar[int] = 4

    numbers: list[int] = Field(min_items=min_size, ge=0, le=2**63-1)
    solution: "Solution" = Field(hidden=True)

    def check_semantics(self, size: int) -> bool:
        return len(self.numbers) <= size and self.calculate_score(self.solution, size)

    def calculate_score(self, solution: "Solution", size: int) -> bool:
        first = self.numbers[solution.indices[0]] + self.numbers[solution.indices[1]]
        second = self.numbers[solution.indices[2]] + self.numbers[solution.indices[3]]
        return first == second

    class Solution(SolutionModel):
        """A solution to a Pairsum problem"""
        indices: list[int] = Field(min_items=4, max_items=4, ge=0)

        def check_semantics(self, size: int, instance: "Pairsum") -> bool:
            return all(i < len(instance.numbers) for i in self.indices) and len(self.indices) == len(set(self.indices))
