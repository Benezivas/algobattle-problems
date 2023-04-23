"""Tests for the scheduling problem."""
import unittest
import logging

from algobattle_problems.scheduling import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the scheduling parser."""

    def setUp(self) -> None:
        self.parser = parser.SchedulingParser()

    def test_split_into_instance_and_solution(self):
        raw_input = [('j', '1', '30'), ('j', '2', '120'), ('j', '3', '24'), ('j', '4', '40'), ('j', '5', '60'),
                     ('a', '1', '4'), ('a', '2', '1'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '2'), ('foo', 'bar')]
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ([('j', '1', '30'), ('j', '2', '120'), ('j', '3', '24'), ('j', '4', '40'), ('j', '5', '60')],
                          [('a', '1', '4'), ('a', '2', '1'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '2')]))

    def test_split_into_instance_and_solution_empty(self):
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ([], []))

    def test_parse_instance_too_many_entries(self):
        raw_instance = [('j', '1', '30', '20'), ('j', '2', '120')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('j', '2', '120')])

    def test_parse_instance_too_few_entries(self):
        raw_instance = [('j', '1'), ('j', '2', '120')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [('j', '2', '120')])

    def test_parse_instance_too_large_labels(self):
        raw_instance = [('j', '1', '30'), ('j', '2', '120')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=1), [('j', '1', '30')])

    def test_parse_instance_duplicate_entry(self):
        raw_instance = [('j', '1', '30'), ('j', '1', '30')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('j', '1', '30')])

    def test_parse_instance_letter_labels(self):
        raw_instance = [('j', 'a', '30'), ('j', '2', 'a')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_zero_label(self):
        raw_instance = [('j', '0', '30'), ('j', '2', '120')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('j', '2', '120')])

    def test_parse_instance_duplicate_job(self):
        raw_instance = [('j', '1', '30'), ('j', '1', '120')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('j', '1', '30')])

    def test_parse_instance_empty(self):
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [])

    def test_parse_solution_too_many_entries(self):
        raw_solution = [('a', '1', '4', '2'), ('a', '2', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('a', '2', '1')])

    def test_parse_solution_too_few_entries(self):
        raw_solution = [('a', '1'), ('a', '2', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('a', '2', '1')])

    def test_parse_solution_too_large_job_labels(self):
        raw_solution = [('a', '1', '4'), ('a', '2', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=1), [('a', '1', '4')])

    def test_parse_solution_too_large_machine_labels(self):
        raw_solution = [('a', '1', '4'), ('a', '2', '6')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=2), [('a', '1', '4')])

    def test_parse_solution_letter_label(self):
        raw_solution = [('a', '1', 'a'), ('a', '2', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('a', '2', '1')])

    def test_parse_solution_zero_label(self):
        raw_solution = [('a', '0', '4'), ('a', '2', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('a', '2', '1')])

    def test_parse_solution_multiple_job_schedule(self):
        raw_solution = [('a', '1', '4'), ('a', '1', '1')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('a', '1', '4')])

    def test_parse_solution_empty(self):
        self.assertEqual(self.parser.parse_solution([], instance_size=2), [])

    def test_encode(self):
        self.assertEqual(self.parser.encode([('j', '1', '30'), ('j', '2', '120'), ('a', '4', '3'), ('a', '5', '2')]),
                         """j 1 30\nj 2 120\na 4 3\na 5 2""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode("""j 1 30\nj 2 120\na 4 3\na 5 2\n""".encode()),
                         [('j', '1', '30'), ('j', '2', '120'), ('a', '4', '3'), ('a', '5', '2')])


class Verifiertests(unittest.TestCase):
    """Tests for the scheduling verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.SchedulingVerifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([('j', '1', '30')], instance_size=10))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=10))

    def test_verify_semantics_of_instance_exceeding_job_size(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance(
            [('j', '1', '{}'.format(2**64)), ('j', '2', '120')], instance_size=10))

    def test_verify_semantics_of_solution_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 10, solution_type=False))

    def test_verify_semantics_of_solution(self):
        self.assertTrue(self.verifier.verify_semantics_of_solution([('a', '1', '3')], 10, solution_type=False))

    def test_verify_solution_against_instance_valid(self):
        instance = [('j', '1', '30'), ('j', '2', '120'), ('j', '3', '24'), ('j', '4', '40'), ('j', '5', '60')]
        solution = [('a', '1', '4'), ('a', '2', '1'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '2')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance, solution,
                        instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_assign_to_nonexistent(self):
        instance = [('j', '1', '30')]
        solution = [('a', '4', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance, solution,
                         instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_job_not_scheduled(self):
        instance = [('j', '1', '30'), ('j', '2', '120'), ('j', '3', '24'), ('j', '4', '40'), ('j', '5', '60')]
        solution = [('a', '1', '4'), ('a', '2', '1'), ('a', '3', '5'), ('a', '4', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance, solution,
                                                                        instance_size=10, solution_type=False))

    def test_calculate_approximation_ratio(self):
        instance = [('j', '1', '30'), ('j', '2', '120'), ('j', '3', '24'), ('j', '4', '40'), ('j', '5', '60')]
        solution_sufficient = [('a', '1', '4'), ('a', '2', '1'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '2')]
        solution_too_much = [('a', '1', '4'), ('a', '2', '2'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '1')]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance, 10, solution_sufficient,
                                                                     solution_too_much), 2.0)
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance, 10, solution_sufficient,
                                                                     solution_sufficient), 1.0)

    def test_calculate_makespan(self):
        instance = [('j', '1', '30'), ('j', '2', '120'), ('j', '3', '24'), ('j', '4', '40'), ('j', '5', '60')]
        solution_sufficient = [('a', '1', '4'), ('a', '2', '1'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '2')]
        solution_too_much = [('a', '1', '4'), ('a', '2', '2'), ('a', '3', '5'), ('a', '4', '3'), ('a', '5', '1')]
        self.assertEqual(self.verifier.calculate_makespan(instance, solution_sufficient), 120)
        self.assertEqual(self.verifier.calculate_makespan(instance, solution_too_much), 240)


if __name__ == '__main__':
    unittest.main()
