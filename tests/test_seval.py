import unittest

from seval.seval import parse_string


class SevalTest(unittest.TestCase):
    def test_bin_op(self):
        e, env = parse_string({}, "1 + 3")
        self.assertEqual(e, [4])

        e, _ = parse_string({}, "3 // 4")
        self.assertEqual(e, [0])

    def test_env_lookup(self):
        e, env = parse_string({'x': 3}, "x")
        self.assertEqual(e, [3])

        e, env = parse_string({'x': {'y': 3}}, "x")
        self.assertEqual(e, [{'y': 3}])

    def test_tuple(self):
        e, env = parse_string({}, "(3, 4)")
        self.assertEqual(e, [(3, 4)])

    def test_list(self):
        e, env = parse_string({}, "[]")
        self.assertEqual(e, [[]])

        e, env = parse_string({}, "[3, 4, 5]")
        self.assertEqual(e, [[3, 4, 5]])

        e, env = parse_string({}, "[3*4, 4*4, 5*4]")
        self.assertEqual(e, [[12, 16, 20]])

    def test_dict(self):
        e, env = parse_string({}, "{'x': 4}")
        self.assertEqual(e, [{'x': 4}])

    def test_compare_op(self):
        e, env = parse_string({}, "3 > 4")
        self.assertEqual(e, [False])

        e, env = parse_string({}, "(2*3) > 4")
        self.assertEqual(e, [True])

        e, env = parse_string({}, "[3,4,5] == [5,6,7]")
        self.assertEqual(e, [False])

    def test_unary_op(self):
        e, env = parse_string({}, "not True")
        self.assertEqual(e, [False])

def run_all():
    unittest.main()