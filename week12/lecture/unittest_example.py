import unittest
from quadratic import solve


class TestQuadratic(unittest.TestCase):

    # setup, run first everytime
    def setUp(self):
        self.a, self.b, self.c = 1, -5, 6

    # teardown, run last
    def tearDown(self):
        pass

    # positive test
    def test_roots_correct(self):
        x1, x2 = solve(self.a, self.b, self.c)
        self.assertEqual(x1, 3.0)
        self.assertEqual(x2, 2.0)

     # negative test
    def test_no_real_roots_raises(self):
        with self.assertRaises(ValueError):
            solve(1, 0, 1)


if __name__ == "__main__":
    unittest.main()
