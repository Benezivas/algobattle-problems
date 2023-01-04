"""Main module of the Pairsum problem."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import Optimization, OptimiztionSolution

logger = logging.getLogger('algobattle.problems.pairsum')


class Pairsum(Optimization):
    """The pairsum problem."""

    name: ClassVar[str] = "Pairsum"
    min_size: ClassVar[int] = 4

    numbers: list[int] = Field(min_items=min_size, ge=0, le=2**63-1)

    def check_semantics(self, size: int) -> bool:
        return len(self.numbers) <= size and super().check_semantics(size)

    class Solution(OptimiztionSolution):
        """A solution to a Pairsum problem"""
        indices: list[int] = Field(min_items=4, max_items=4, ge=0)

        def check_semantics(self, size: int, instance: "Pairsum") -> bool:
            return all(i < len(instance.numbers) for i in self.indices) and len(self.indices) == len(set(self.indices))

        def score(self, size: int, instance: "Pairsum") -> float:
            first = instance.numbers[self.indices[0]] + instance.numbers[self.indices[1]]
            second = instance.numbers[self.indices[2]] + instance.numbers[self.indices[3]]
            return first == second
