# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEquals(utils.fact(2), 4)
        self.assertEquals(utils.fact(0), 1)
        self.assertEquals(utils.fact(-3), None)
        pass
    
    def test_roots(self):
        # À compléter...
        self.assertEquals(utils.roots(1, 1, 1), ())
        self.assertEquals(utils.roots(1, 4, 4), (-2.0,))
        self.assertEquals(utils.roots(0, 1, -1), (1.0,))
        self.assertEquals(utils.roots(0, 0, -1), ())
        pass

    
    def test_integrate(self):
        self.assertEquals(utils.integrate('1', 0, 1), 1.0)
        self.assertEquals(utils.integrate('0', 0, 0), 0.0)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
