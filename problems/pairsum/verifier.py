"""Verifier for solutions of the Pairsum Problem."""
import logging

from algobattle.verifier import Verifier

logger = logging.getLogger('algobattle.problems.pairsum..verifier')


class PairsumVerifier(Verifier):
    """Verifier for solutions of the Pairsum Problem."""

    def verify_semantics_of_solution(self, solution, instance_size: int, solution_type: bool):
        # Solutions for this problem are semantically valid if they are syntactically valid.
        # We only check if the solution is empty.
        if not solution:
            logger.error('The solution is empty!')
            return False
        if len(solution) != 4:
            logger.warning('The solution is not of size 4!')
            return False
        if len(set(solution)) != 4:
            logger.warning('The solution contains duplicate entries!')
            return False
        return True

    def verify_solution_against_instance(self, instance, solution, instance_size, solution_type):
        if not instance[solution[0]] + instance[solution[1]] == instance[solution[2]] + instance[solution[3]]:
            logger.error('The given solution is not valid!')
            return False

        return True

    def calculate_approximation_ratio(self, instance, instance_size, generator_solution, solver_solution):
        return 1.0
