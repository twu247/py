import unittest
from hw import hello
class TestHello(unittest.TestCase):
	def test_print(self):
		self.assertAlmostEqual(hello(),"HELLO WORLD...?")