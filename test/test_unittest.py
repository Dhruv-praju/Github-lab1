import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


from src import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2,3), 5)
        self.assertEqual(calculator.add(5,0), 5)
        self.assertEqual(calculator.add(-1,1), 0)
        self.assertEqual(calculator.add(-1,-1), -2)

    def test_subract(self):
        self.assertEqual(calculator.subract(2,3), -1)
        self.assertEqual(calculator.subract(3,3), 0)
        self.assertEqual(calculator.subract(3,-2), 5)
        self.assertEqual(calculator.subract(-2,-3), 1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2,3), 6)
        self.assertEqual(calculator.multiply(2,-3), -6)
        self.assertEqual(calculator.multiply(-2,-3), 6)
        self.assertEqual(calculator.multiply(0,3), 0)

    def test_add_all(self):
        self.assertEqual(calculator.add_all(1,2,3), 6)
        self.assertEqual(calculator.add_all(1,-2,3), 2)
        self.assertEqual(calculator.add_all(-1,-2,3), 0)
        self.assertEqual(calculator.add_all(-1,-2,-3), -6)
