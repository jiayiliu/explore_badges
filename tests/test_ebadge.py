import unittest

from ebadge import EBadge

class TestEBadge(unittest.TestCase):
    def testA(self):
        a = EBadge()
        self.assertEqual(a.funcA(), 1)