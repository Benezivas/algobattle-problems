"""The Circle Cover problem class."""
from math import sqrt
from typing import Annotated, Literal
from algobattle.problem import Problem, InstanceModel, SolutionModel, maximize
from algobattle.util import Role
from algobattle.types import LaxComp, Interval


Coordinate = Annotated[float, Interval(ge=0, le=100)]
Point = tuple[Coordinate, Coordinate]


def distance(a: Point, b: Point) -> float:
    """Calculates the distance between two points."""
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


class Instance(InstanceModel):
    """An Instance of the Circle Cover Problem."""

    points: set[Point]

    @property
    def size(self) -> int:
        return len(self.points)


class Solution(SolutionModel[Instance]):
    """A solution of the Circle Cover problem."""

    circles: dict[Literal[10, 20, 30], Point]

    @maximize
    def score(self, instance: Instance, role: Role) -> float:
        covered = 0
        for size, center in self.circles.items():
            covered += sum(distance(center, point) <= LaxComp(size, role) for point in instance.points)
        return covered


CircleCover = Problem(
    name="Circle Cover",
    instance_cls=Instance,
    solution_cls=Solution,
    min_size=1,
    test_instance=Instance(points={(0, 1), (50, 50), (100, 17)}),
)
