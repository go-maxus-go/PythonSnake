import unittest

from src.apple import *

class TestApple(unittest.TestCase):

    def test_x(self):
        apple = Apple(1, 2)
        self.assertEqual(apple.x(), 1)

    def test_y(self):
        apple = Apple(1, 2)
        self.assertEqual(apple.y(), 2)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestApple))
    return suite

if __name__ == '__main__':
    unittest.main()
