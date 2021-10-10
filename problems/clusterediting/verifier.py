"""Verifier for solutions of the ClusterEditing Problem."""
import logging

from algobattle.verifier import Verifier

logger = logging.getLogger('algobattle.problems.clusterediting.verifier')


class ClustereditingVerifier(Verifier):
    """Verifier for solutions of the ClusterEditing Problem."""

    def verify_solution_against_instance(self, instance, solution, instance_size, solution_type):
        solution_add = [line for line in solution if (line[0] == 's' and line[1] == 'add')]
        solution_del = [line for line in solution if (line[0] == 's' and line[1] == 'del')]

        if any(('e', edge[2], edge[3]) not in instance and ('e', edge[3], edge[2]) not in instance for edge in solution_del):
            logger.error('The solution tries to delete an edge that is not part of the instance!')
            return False

        all_edges = set()
        for edge in instance:
            all_edges.add(edge)
            all_edges.add(('e', edge[2], edge[1]))
        for edge in solution_add:
            all_edges.add(('e', edge[2], edge[3]))
            all_edges.add(('e', edge[3], edge[2]))
        for edge in solution_del:
            all_edges.remove(('e', edge[2], edge[3]))
            all_edges.remove(('e', edge[3], edge[2]))

        # Check if the graph is triangulated: For every two adjacent edges their endpoints have to be connected.
        for edge1 in all_edges:
            for edge2 in all_edges:
                if edge1 != edge2:
                    # We inserted every edge bidirectional, so only the first neighbor needs to be compared:
                    if edge1[1] == edge2[1]:
                        if not ('e', edge1[2], edge2[2]) in all_edges:
                            logger.error('The given solution is not valid!')
                            return False
        return True

    def calculate_approximation_ratio(self, instance, instance_size, generator_solution, solver_solution):
        return float(len(solver_solution)) / float(len(generator_solution))
