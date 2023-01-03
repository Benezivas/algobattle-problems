"""Shared data used for other problems."""
import logging
from typing import Generic, TypeVar
from pydantic import Field
from pydantic.generics import GenericModel

from algobattle.problem import ProblemModel, Problem

logger = logging.getLogger('algobattle.problems.pairsum')


class DirectedGraph(ProblemModel):
    """Base class for problems on directed graphs."""

    num_vertices: int = Field(ge=0, le=2**63-1)
    edges: list[tuple[int, int]] = Field(ge=0, le=2**63-1)

    def check_semantics(self, size: int) -> bool:
        return (
            self.num_vertices <= size
            and all(u < self.num_vertices and v < self.num_vertices for u, v in self.edges)
            and len(self.edges) == len(set(self.edges))
        )


class UndirectedGraph(DirectedGraph):
    """Base class for problems on undirected graphs."""

    def check_semantics(self, size: int) -> bool:
        if not super().check_semantics(size):
            return False
        edges = set(self.edges)
        return (
            all(u != v for u, v in edges)
            and all((v, u) not in edges for u, v in edges)
        )


Weight = TypeVar("Weight")


class EdgeWeights(GenericModel, Generic[Weight]):
    """Mixin for graphs with weighted edges."""

    edge_weights: list[Weight]

    def check_semantics(self, size: int) -> bool:
        assert isinstance(self, DirectedGraph)
        as_parent = super()
        if isinstance(as_parent, Problem):
            if not as_parent.check_semantics(size):
                return False

        return len(self.edge_weights) == len(self.edges)


class VertexWeights(GenericModel, Generic[Weight]):
    """Mixin for graphs with weighted vertices."""

    vertex_weights: list[Weight]

    def check_semantics(self, size: int) -> bool:
        assert isinstance(self, DirectedGraph)
        as_parent = super()
        if isinstance(as_parent, Problem):
            if not as_parent.check_semantics(size):
                return False

        return len(self.vertex_weights) == self.num_vertices
