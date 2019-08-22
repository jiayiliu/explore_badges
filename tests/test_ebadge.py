import unittest

from ebadge import EBadge

class TestEBadge(unittest.TestCase):
    def testA(self):
        a = EBadge()
        self.assertEqual(a.funcA(), 1)

    def test_exec(self):
        import subprocess
        ans = subprocess.check_output(["python", "-m","ebadge"])
        ans = ans.decode('utf8').strip()
        self.assertEqual(ans, 'a')