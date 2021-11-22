"""Tests for the c4subgraphiso problem."""
import unittest
import logging

from problems.c4subgraphiso import parser, verifier

logging.disable(logging.CRITICAL)


class Parsertests(unittest.TestCase):
    """Tests for the c4subgraphiso parser."""

    def setUp(self) -> None:
        self.parser = parser.C4subgraphisoParser()

    def test_split_into_instance_and_solution(self):
        raw_input = [('e', '1', '2'), ('s', '5', '6', '7', '8'), ('s', '2'), ('foo', 'bar')]
        self.assertEqual(self.parser.split_into_instance_and_solution(raw_input),
                         ([('e', '1', '2')], [('s', '5', '6', '7', '8'), ('s', '2')]))

    def test_split_into_instance_and_solution_empty(self):
        self.assertEqual(self.parser.split_into_instance_and_solution([]), ([], []))

    def test_parse_instance_too_many_entries(self):
        raw_instance = [('e', '1', '2', '1'), ('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('e', '3', '2')])

    def test_parse_instance_too_few_entries(self):
        raw_instance = [('e', '1'), ('e')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [])

    def test_parse_instance_high_labels(self):
        raw_instance = [('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=2), [])

    def test_parse_instance_duplicate_edge(self):
        raw_instance = [('e', '3', '2'), ('e', '3', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [('e', '3', '2')])

    def test_parse_instance_letters_in_labels(self):
        raw_instance = [('e', '3', 'a'), ('e', 'b', '2')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_zero_labels(self):
        raw_instance = [('e', '1', '0'), ('e', '0', '1')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_selfloop(self):
        raw_instance = [('e', '1', '1')]
        self.assertEqual(self.parser.parse_instance(raw_instance, instance_size=3), [])

    def test_parse_instance_empty(self):
        self.assertEqual(self.parser.parse_instance([], instance_size=3), [])

    def test_parse_solution_too_many_entries(self):
        raw_solution = [('s', '1', '2', '9', '10', '1'), ('s', '5', '6', '7', '8')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [('s', '5', '6', '7', '8')])

    def test_parse_solution_too_few_entries(self):
        raw_solution = [('s', '1', '2', '9')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_high_labels(self):
        raw_solution = [('s', '1', '2', '9', '10')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=9), [])

    def test_parse_solution_letters_in_labels(self):
        raw_solution = [('s', '1', 'foo', '9', '10')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_zero_label(self):
        raw_solution = [('s', '1', '0', '9', '10')]
        self.assertEqual(self.parser.parse_solution(raw_solution, instance_size=10), [])

    def test_parse_solution_empty(self):
        self.assertEqual(self.parser.parse_solution([], instance_size=2), [])

    def test_encode(self):
        self.assertEqual(self.parser.encode([('s', '1', '2', '9', '10'), ('s', '5', '6', '7', '8'), ('e', '1', '2'),
                                             ('e', '2', '3'), ('e', '3', '4'), ('e', '3', '5'), ('e', '5', '6')]),
                         """s 1 2 9 10\ns 5 6 7 8\ne 1 2\ne 2 3\ne 3 4\ne 3 5\ne 5 6""".encode())

    def test_decode(self):
        self.assertEqual(self.parser.decode("""s 1 2 9 10\ns 5 6 7 8\ne 1 2\ne 2 3\ne 3 4\ne 3 5\ne 5 6""".encode()),
                         [('s', '1', '2', '9', '10'), ('s', '5', '6', '7', '8'), ('e', '1', '2'), ('e', '2', '3'),
                          ('e', '3', '4'), ('e', '3', '5'), ('e', '5', '6')])


class Verifiertests(unittest.TestCase):
    """Tests for the c4subgraphiso verifier."""

    def setUp(self) -> None:
        self.verifier = verifier.C4subgraphisoVerifier()

    def test_verify_semantics_of_instance(self):
        self.assertTrue(self.verifier.verify_semantics_of_instance([('e', '1', '2')], instance_size=10))

    def test_verify_semantics_of_instance_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_instance([], instance_size=10))

    def test_verify_semantics_of_solution_empty(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([], 10, solution_type=False))

    def test_verify_semantics_of_solution_no_circle(self):
        self.assertFalse(self.verifier.verify_semantics_of_solution([('s', '5', '6', '7', '8'),
                                                                    ('s', '5', '2', '9', '10')],
                                                                    instance_size=10, solution_type=False))

    def test_verify_solution_against_instance(self):
        instance = [('e', '1', '2'), ('e', '2', '3'), ('e', '3', '4'), ('e', '3', '5'), ('e', '5', '6'),
                    ('e', '6', '7'), ('e', '7', '8'), ('e', '8', '9'), ('e', '9', '10'), ('e', '10', '1'),
                    ('e', '2', '9'), ('e', '5', '9'), ('e', '5', '8')]
        solution = [('s', '1', '2', '9', '10'), ('s', '5', '6', '7', '8')]
        self.assertTrue(self.verifier.verify_solution_against_instance(instance,
                                                                       solution, instance_size=10, solution_type=False))

    def test_verify_solution_against_instance_incorrect_cycles(self):
        instance = [('e', '1', '2'), ('e', '2', '3'), ('e', '3', '4'), ('e', '3', '5'), ('e', '5', '6'),
                    ('e', '6', '7'), ('e', '7', '8'), ('e', '8', '9'), ('e', '9', '10'), ('e', '10', '1'),
                    ('e', '2', '9'), ('e', '5', '9'), ('e', '5', '8')]
        solution = [('s', '1', '2', '9', '10'), ('s', '5', '6', '7', '3')]
        self.assertFalse(self.verifier.verify_solution_against_instance(instance,
                                                                        solution, instance_size=10, solution_type=False))

    def test_calculate_approximation_ratio_suboptimal(self):
        instance = [('e', '1', '2'), ('e', '2', '3'), ('e', '3', '4'), ('e', '3', '5'), ('e', '5', '6'),
                    ('e', '6', '7'), ('e', '7', '8'), ('e', '8', '9'), ('e', '9', '10'), ('e', '10', '1'),
                    ('e', '2', '9'), ('e', '5', '9'), ('e', '5', '8')]
        solution_full = [('s', '1', '2', '9', '10'), ('s', '5', '6', '7', '8')]
        solution_small = [('s', '1', '2', '9', '10')]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance, 10, solution_full, solution_small), 2.0)

    def test_calculate_approximation_ratio_optimal(self):
        instance = [('e', '1', '2'), ('e', '2', '3'), ('e', '3', '4'), ('e', '3', '5'), ('e', '5', '6'),
                    ('e', '6', '7'), ('e', '7', '8'), ('e', '8', '9'), ('e', '9', '10'), ('e', '10', '1'),
                    ('e', '2', '9'), ('e', '5', '9'), ('e', '5', '8')]
        solution_full = [('s', '1', '2', '9', '10'), ('s', '5', '6', '7', '8')]
        self.assertEqual(self.verifier.calculate_approximation_ratio(instance, 10, solution_full, solution_full), 1.0)


if __name__ == '__main__':
    unittest.main()
