import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc.operation('+', 1, 1), 2)
        self.assertEqual(calc.operation('+', 10, 10), 20)
        self.assertEqual(calc.operation('+', -30, 30), 0)
        self.assertEqual(calc.operation('+', 50, -10), 40)

    def test_sous(self):
    	self.assertEqual(calc.operation('-', 2, 1), 1)

    def test_wrong_operator(self):
    	with self.assertRaises(TypeError):
    		calc.operation('$', 1, 1)

if __name__ == '__main__':
    unittest.main()