"""Verifier for solutions of the Scheduling Problem."""
import logging

from algobattle.verifier import Verifier

logger = logging.getLogger('algobattle.problems.scheduling.verifier')


class SchedulingVerifier(Verifier):
    """Verifier for solutions of the Scheduling Problem."""

    def verify_semantics_of_instance(self, instance, instance_size: int):
        if not instance:
            logger.error('The instance is empty!')
            return False

        if sum(int(job[2]) for job in instance) * 5 >= 2 ** 64:
            logger.error('The cumulated job sizes exceed the given limit!')
            return False

        return True

    def verify_solution_against_instance(self, instance, solution, instance_size, solution_type):
        if len(solution) < len(instance):
            logger.error('The solution does not schedule all jobs!')
            return False

        all_jobs = set()
        for job in instance:
            all_jobs.add(job[1])

        all_assigned_jobs = set()
        for assignment in solution:
            all_assigned_jobs.add(assignment[1])

        if all_jobs != all_assigned_jobs:
            logger.error('The set of jobs of the instance and the set of jobs of the solution differ!')
            return False
        return True

    def calculate_approximation_ratio(self, instance, instance_size, generator_solution, solver_solution):
        jobs_to_be_scheduled = [job[1] for job in instance]
        # As the instance may have lost some jobs during parsing that were
        # assumed to be present, we may need to cut down the generator solution
        generator_solution = [assignment for assignment in generator_solution if assignment[1] in jobs_to_be_scheduled]

        generator_makespan = self.calculate_makespan(instance, generator_solution)
        solver_makespan = self.calculate_makespan(instance, solver_solution)

        return float(solver_makespan) / float(generator_makespan)

    def calculate_makespan(self, jobs, assignments):
        makespans = [0 for i in range(5)]

        for assignment in assignments:
            job_number = assignment[1]
            machine = int(assignment[2])
            base_running_time = 0
            for job in jobs:
                if job[1] == job_number:
                    base_running_time = int(job[2])
            makespans[machine - 1] += base_running_time * machine

        return max(makespans)
