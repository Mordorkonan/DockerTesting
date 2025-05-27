import unittest
from main_module import MainModule

class MainModuleTestCase(unittest.TestCase):

	def test_add(self):
		self.assertEqual(MainModule.add(1, 2), 3)

	def test_sub(self):
		self.assertEqual(MainModule.sub(3, 6), -3)

	def test_mul(self):
		self.assertEqual(MainModule.mul(3, 0), 0)

	def test_div(self):
		self.assertEqual(MainModule.div(3, 3), 1)

	def test_div_zero(self):
		self.assertEqual(MainModule.div(3, 0), 0)


if __name__ == '__main__': unittest.main()
