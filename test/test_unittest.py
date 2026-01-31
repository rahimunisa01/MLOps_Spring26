import unittest
from src.calculator import fun1, fun2, fun3, fun4


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(fun1(3, 2), 5)
        self.assertEqual(fun1(-1, 1), 0)

    def test_fun2(self):
        self.assertEqual(fun2(5, 3), -2)
        self.assertEqual(fun2(3, 5), 2)

    def test_fun3(self):
        self.assertEqual(fun3(4, 2), 8)
        self.assertEqual(fun3(0, 5), 0)

    def test_fun4(self):
        # (4 + 2) + (2-4) + (4 * 2) = 6 - 2 + 8 = 16
        self.assertEqual(fun4(4, 2), 12)


if __name__ == "__main__":
    unittest.main()

