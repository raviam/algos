import unittest
from fibo import fib2

class FiboTestCase(unittest.TestCase):
	""" Tets for 'fibo.py'."""
	def test_fibs_below_100(self):
		self.assertEqual(fib2(100),[1,1,2,3,5,8,13,21,34,55,89])
if __name__ =='__main__':
	unittest.main()