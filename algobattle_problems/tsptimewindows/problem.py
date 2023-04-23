"""The Tsptimewindows problem class."""
import logging
import sys

from typing import ClassVar, TypeAlias, Any, SupportsFloat
from pydantic import Field

from algobattle.problem import ProblemModel, SolutionModel

logger = logging.getLogger('algobattle.problems.tsptimewindows')

_Solution: TypeAlias = Any

class Tsptimewindows(ProblemModel):
    """The Tsptimewindows problem class."""

    name: ClassVar[str] = "Traveling Salesman with Time Windows"
    min_size: ClassVar[int] = 5

    num_vertices: int = Field(ge=0, le=2 ** 63 - 1)
    positions: list[tuple[float, float]] = Field(ge=0, le=100)
    time_windows: list[tuple[float, float]] = Field(ge=0, le=10000)

    def check_semantics(self, size: int) -> bool:
        return (
            self.num_vertices <= size
            and len(self.positions) == len(self.time_windows)
            and all(u <= v for (u, v) in self.time_windows)
        )

    def _distance(self, a: int, b: int) -> float:
        return (
            (self.positions[a][0] - self.positions[b][0]) ** 2
            + (self.positions[a][1] - self.positions[b][1]) ** 2
        ) ** 0.5

    class Solution(SolutionModel):
        """A solution to a Traveling Salesman with Time Windows problem."""

        direction: ClassVar = "minimize"
        tour: tuple[int, ...] = Field(ge=0, le=2 ** 63 - 1)

        def check_semantics(self, instance: "Tsptimewindows", size: int) -> bool:
            return (
                len(self.tour) == len(instance.positions)
                and len(self.tour) == len(set(self.tour))
                and all(i < instance.num_vertices for i in self.tour)
            )

        def _length_of_tour(self, solving_team: bool, instance: "Tsptimewindows") -> float:
            start_node = self.tour[0]
            mult = 0.9 if solving_team else 1.0
            total_time = instance.time_windows[start_node][0] * mult

            last_node = self.tour[0]
            for i in range(1, len(self.tour) - 1):
                current_node = self.tour[i]
                travel_time = mult * instance._distance(last_node, current_node)
                # Do we arrive in time?
                if total_time + travel_time > instance.time_windows[current_node][1]:
                    return sys.float_info.max
                # We may have to wait at the node until it is available
                total_time = max(total_time + travel_time, instance.time_windows[current_node][0])
                last_node = current_node

            travel_time = mult * instance._distance(last_node, start_node)
            if total_time + travel_time > instance.time_windows[start_node][1]:
                return sys.float_info.max
            # We may have to wait at the node until it is available
            total_time = max(total_time + travel_time, instance.time_windows[start_node][0])

            return total_time

    def calculate_score(self, solution: _Solution, generator_solution: _Solution | None, size: int) -> SupportsFloat:
        gen_score = generator_solution._length_of_tour(solving_team=False, instance=self)
        sol_score = solution._length_of_tour(solving_team=True, instance=self)

        if gen_score == 0:
            return 1
        if sol_score == 0:
            return 0

        return gen_score / sol_score
