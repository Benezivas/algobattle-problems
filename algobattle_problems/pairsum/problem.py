"""Main module of the Pairsum problem."""
from typing import ClassVar
from pydantic import Field

from algobattle.problem import ProblemModel, SolutionModel, ValidationError
from algobattle.util import u64


class Pairsum(ProblemModel):
    """The Pairsum problem class."""

    name: ClassVar[str] = "Pairsum"
    min_size: ClassVar[int] = 4

    numbers: list[int] = Field(min_items=min_size, ge=0, le=2**63-1)

    @property
    def size(self) -> int:
        return len(self.numbers)

    class Solution(SolutionModel):
        """A solution to a Pairsum problem"""

        indices: tuple[u64, u64, u64, u64]

        def validate_solution(self, instance: "Pairsum") -> None:
            super().validate_solution(instance)
            if any(i >= len(instance.numbers) for i in self.indices):
                raise ValidationError("Solution index is out of range.")
            if len(self.indices) != len(set(self.indices)):
                raise ValidationError("Solution contains duplicate indices.")
            first = instance.numbers[self.indices[0]] + instance.numbers[self.indices[1]]
            second = instance.numbers[self.indices[2]] + instance.numbers[self.indices[3]]
            if first != second:
                raise ValidationError("Solution elements don't have the same sum.")
