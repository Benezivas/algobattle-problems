"""The Hikers problem class."""
import logging
from typing import ClassVar
from pydantic import Field

from algobattle.problem import ProblemModel, SolutionModel

logger = logging.getLogger('algobattle.problems.hikers')


class Hikers(ProblemModel):
    """The Tsptimewindows problem class."""

    name: ClassVar[str] = "Hikers"
    min_size: ClassVar[int] = 5

    hikers: list[tuple[int, int]] = Field(ge=0)

    def is_valid(self, size: int) -> bool:
        return (
            all(min_size <= max_size for (min_size, max_size) in self.hikers)
            and len(self.hikers) <= size
            and len(self.hikers) == len(set(self.hikers))
        )

    class Solution(SolutionModel):
        """A solution to a Hikers problem."""

        direction: ClassVar = "maximize"
        assignments: list[tuple[int, int]] = Field(ge=0)

        def is_valid(self, instance: "Hikers", size: int) -> bool:
            group_sizes = dict()
            if (
                not all(hiker_index < size for (hiker_index, _) in self.assignments)
                or not len(self.assignments) == len(set(self.assignments))
            ):
                return False

            for (_, group) in self.assignments:
                group_sizes[group] = group_sizes.get(group, 0)
                group_sizes[group] += 1

            for (hiker, group) in self.assignments:
                (min_size, max_size) = instance.hikers[hiker]
                if not (min_size <= group_sizes[group]
                        and max_size >= group_sizes[group]):
                    logger.error(f"Hiker {hiker} is not happy with their assignment!")
                    return False

            return True

        def score(self, size: int, instance: "Hikers") -> float:
            return len(self.assignments)
