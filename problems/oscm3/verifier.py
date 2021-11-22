"""Verifier for solutions of the OSCM3 Problem."""

import logging
import copy
import sys

from algobattle.verifier import Verifier

logger = logging.getLogger('algobattle.problems.oscm3.verifier')


class OSCM3Verifier(Verifier):
    """Verifier for solutions of the OSCM3 Problem."""

    class Graph:
        """Helper graph class to verify solutions."""

        def __init__(self, size):
            self.size = size
            self.upper_nodes = [None for i in range(size)]
            self.lower_nodes = [[] for i in range(size)]
            self.edges = [[] for i in range(size)]

        def insert_node(self, name, slot, neighbors):
            """Insert a node into a slot of the graph.

            Parameters
            ----------
            name : str
                Internal name of the node.
            slot : int
                The slot number into which the node is to be inserted into.
            neighbors : list
                The list of adjacent nodes to the given node.
            """
            neighbors = sorted(neighbors)
            self.upper_nodes[slot] = str(name)
            i = 1
            for neighbor in neighbors:
                self.lower_nodes[neighbor].append(str(name) + "_" + str(i))
                i += 1
                self.edges[slot].append(neighbor)

        def calculate_number_crossings(self):
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

        def reorder_upper_nodes(self, permutation):
            """Reorder the nodes currently placed in the slots according to a given permutation.

            Parameters
            ----------
            permutation : tuple
                A permutation as a tuple of ints, assumed to be encoded as strings, e.g. ('2', '3', '1').
            """
            old_nodes = copy.deepcopy(self.upper_nodes)
            old_edges = copy.deepcopy(self.edges)

            for i in range(self.size):
                self.upper_nodes[i] = old_nodes[int(permutation[i])]
                self.edges[i] = old_edges[int(permutation[i])]

    def verify_solution_against_instance(self, instance, solution, instance_size, solution_type):
        # For this problem, no further verification is needed: If the Syntax is
        # correct, a solution string is automatically a valid solution.

        return True

    def calculate_approximation_ratio(self, instance, instance_size, generator_solution, solver_solution):
        g = self.Graph(instance_size)

        for element in instance:
            g.insert_node(element[1], int(element[1]), [int(entry) for entry in element[2:]])

        h = copy.deepcopy(g)
        g.reorder_upper_nodes(generator_solution[1:])
        h.reorder_upper_nodes(solver_solution[1:])
        generator_crossings = g.calculate_number_crossings()
        solver_crossings = h.calculate_number_crossings()

        if generator_crossings == solver_crossings:
            return 1.0
        elif generator_crossings == 0:
            return sys.maxsize

        return solver_crossings / generator_crossings
