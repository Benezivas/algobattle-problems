"""The OSCM3 problem class."""
import logging
from typing import ClassVar
from pydantic import Field
import copy

from algobattle.problem import ProblemModel, SolutionModel

logger = logging.getLogger('algobattle.problems.oscm3')


class OSCM3(ProblemModel):
    """The OSCM3 problem class."""

    name: ClassVar[str] = "One-Sided Crossing Minimization-3"
    min_size: ClassVar[int] = 1

    adjacent_edges: list[tuple[int, ...]] = Field(ge=0)

    def is_valid(self, size: int) -> bool:
        return (
            all(all(i < size for i in entry) for entry in self.adjacent_edges)
            and all(len(entry) == len(set(entry)) for entry in self.adjacent_edges)
            and len(self.adjacent_edges) == size
        )

    class Solution(SolutionModel):
        """A solution to a One-Sided Crossing Minimization-3 problem"""

        direction: ClassVar = "minimize"

        permutation: tuple[int, ...] = Field(ge=0)

        def is_valid(self, instance: "OSCM3", size: int) -> bool:
            return (
                all(i < size for i in self.permutation)
                and len(self.permutation) == len(set(self.permutation))
                and len(self.permutation) == size
            )

        def score(self, instance: "OSCM3", size: int) -> float:
            g = self.Graph(size)
            i = 0
            for element in instance.adjacent_edges:
                g.insert_node(str(i), i, element)
                i += 1
            g.reorder_upper_nodes(self.permutation)
            return g.calculate_number_crossings()

        class Graph:
            """Helper graph class to calculate solution sizes."""

            def __init__(self, size: int) -> None:
                self.size = size
                self.upper_nodes = [None for i in range(size)]
                self.lower_nodes = [[] for i in range(size)]
                self.edges = [[] for i in range(size)]

            def insert_node(self, name: str, slot: int, neighbors: tuple) -> None:
                """Insert a node into a slot of the graph.

                Parameters
                ----------
                name : str
                    Internal name of the node.
                slot : int
                    The slot number into which the node is to be inserted into.
                neighbors : tuple
                    The tuple of adjacent nodes to the given node.
                """
                neighbors = sorted(neighbors)
                self.upper_nodes[slot] = str(name)
                i = 0
                for neighbor in neighbors:
                    self.lower_nodes[neighbor].append(str(name) + "_" + str(i))
                    i += 1
                    self.edges[slot].append(neighbor)

            def calculate_number_crossings(self) -> int:
                """Calculate and return the number of crossings currently in the graph.

                Returns
                -------
                int
                    The number of crossings in the graph.
                """
                crossings = 0
                for i in range(self.size):
                    if self.upper_nodes[i]:
                        for j in range(i + 1, self.size):
                            if self.upper_nodes[j]:
                                for lower_node_i in self.edges[i]:
                                    for lower_node_j in self.edges[j]:
                                        if lower_node_i > lower_node_j:
                                            crossings += 1
                return crossings

            def reorder_upper_nodes(self, permutation: tuple) -> None:
                """Reorder the nodes currently placed in the slots according to a given permutation.

                Parameters
                ----------
                permutation : tuple
                    A permutation as a tuple of ints.
                """
                old_nodes = copy.deepcopy(self.upper_nodes)
                old_edges = copy.deepcopy(self.edges)

                for i in range(self.size):
                    self.upper_nodes[i] = old_nodes[permutation[i]]
                    self.edges[i] = old_edges[permutation[i]]
