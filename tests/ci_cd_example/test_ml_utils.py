from unittest import TestCase

from ci_cd_example.ml_utils import returns_four

class Test(TestCase):
	def test_returns_four():
		self.assertEqual(returns_four(), 4)
