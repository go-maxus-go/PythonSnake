import unittest

from src.consolerender import *

class TestConsoleRender(unittest.TestCase):
    def setUp(self):
        self.field = Field(5, 5,
                                 [0,0,0,0,0,
                                  1,0,0,0,0,
                                  1,0,0,0,0,
                                  1,0,0,0,0,
                                  0,0,0,0,0])
        self.snakes = [Snake(self.field, Direction.Left, [Point2D(0, 0), Point2D(1, 0), Point2D(2, 0)]),
                       Snake(self.field, Direction.Right, [Point2D(2, 4), Point2D(1, 4), Point2D(0, 4)])]
        self.apples = [Apple(3, 3), Apple(2, 2)]
        self.render = ConsoleRender(self.field, self.snakes, self.apples)

    def test_render(self):
        expected = ['O','*','*','.','.',
                    'X','.','.','.','.',
                    'X','.','@','.','.',
                    'X','.','.','@','.',
                    '*','*','O','.','.']
        result = self.render.render()
        self.assertEqual(expected, result)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestConsoleRender))
    return suite

if __name__ == '__main__':
    unittest.main()
