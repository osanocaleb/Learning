import unittest

import calc
class TestTry1(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calc.try1(5,3,'add'),8)
	def test_substract(self):
		self.assertEqual(calc.try_1(3,5,'subtract'),-2,msg="")
	def test_multiplication(self):
		self.assertEqual(calc.try_1(3,5,'multiply'),15)
	def test_division(self):
		self.assertEqual(calc.try_1(10,3,'divide'),3)
	def test_division_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			calc.try_1(10,0,'divide')