"""The Tsptimewindows problem class."""
from itertools import pairwise
from math import sqrt

from typing import Iterator, Self
from pydantic import Field

from algobattle.problem import Problem, InstanceModel, SolutionModel, ValidationError
from algobattle.util import BaseModel, Role
from algobattle.util import u64, Role


class Location(BaseModel):
    """A location the salesman needs to visit."""

    x: float = Field(ge=0, le=100)
    y: float = Field(ge=0, le=100)
    min_time: float = Field(ge=0, le=10_000)
    max_time: float = Field(ge=0, le=10_000)

    def distance(self, other: Self) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Instance(InstanceModel):
    """The Tsptimewindows problem class."""

    locations: list[Location]

    @property
    def size(self) -> int:
        return len(self.locations)

    def validate_instance(self) -> None:
        super().validate_instance()
        if any(location.min_time > location.max_time for location in self.locations):
            raise ValidationError("An instance location has an invalid time window.")


class Solution(SolutionModel[Instance]):
    """A solution to a Traveling Salesman with Time Windows problem."""

    tour: list[u64]

    def location_tour(self, instance: Instance) -> Iterator[Location]:
        """Iterates over all locations in the tour in order, looping back around to the first."""
        yield from (instance.locations[i] for i in self.tour)
        yield instance.locations[self.tour[0]]

    def validate_solution(self, instance: Instance, role: Role) -> None:
        if len(self.tour) != len(instance.locations):
            raise ValidationError("The solution doesn't visit every location exactly once.")
        if len(self.tour) != len(set(self.tour)):
            raise ValidationError("The solution contains duplicate locations.")
        if any(i >= len(instance.locations) for i in self.tour):
            raise ValidationError("The solution contains invalid location indices.")

        self.score(instance, role)

    def score(self, instance: Instance, team: Role) -> float:
        speed = 1.1 if team == Role.solver else 1  # the solving team is faster than the generating
        time = instance.locations[self.tour[0]].min_time  # wait at the first location until it becomes available
        for curr, next in pairwise(self.location_tour(instance)):
            arrival_time = time + curr.distance(next) / speed
            if arrival_time > next.max_time:
                raise ValidationError("The tour visits a location too late.")
            time = max(arrival_time, next.min_time)  # wait until the next location becomes available
        return time


def score(instance: Instance, solver_solution: Solution, generator_solution: Solution | None) -> float:
    assert generator_solution is not None
    try:
        gen_score = generator_solution.score(instance, Role.generator)
    except ValidationError:
        return 0
    sol_score = solver_solution.score(instance, Role.solver)
    if sol_score == 0:
        return 0
    else:
        return max(min(gen_score / sol_score, 1), 0)


Tsptimewindows = Problem(
    name="Traveling Salesman with Time Windows",
    min_size=5,
    instance_cls=Instance,
    solution_cls=Solution,
    score=score,
)
