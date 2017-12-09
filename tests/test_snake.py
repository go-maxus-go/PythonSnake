import unittest

from src.field import *
from src.snake import *

class TestSnake(unittest.TestCase):

    def setUp(self):
        self.field = Field(10, 10)
        self.snake = Snake(self.field, Direction.Right,
                           [Point2D(4, 0),
                            Point2D(3, 0),
                            Point2D(2, 0),
                            Point2D(1, 0),
                            Point2D(0, 0)])

    def test_head(self):
        self.assertEqual(self.snake.head(), Point2D(4, 0))

    def test_direction(self):
        self.assertEqual(self.snake.direction(), Direction.Right)

        self.snake.setDirection(Direction.Up)
        self.assertEqual(self.snake.direction(), Direction.Up)

        self.snake.setDirection(Direction.Left)
        self.assertEqual(self.snake.direction(), Direction.Up)

        self.snake.setDirection(Direction.Down)
        self.assertEqual(self.snake.direction(), Direction.Down)

    def test_size(self):
        self.assertEqual(self.snake.size(), 5)

    def test_pos(self):
        self.assertEqual(self.snake.pos(0), Point2D(4, 0))
        self.assertEqual(self.snake.pos(1), Point2D(3, 0))
        self.assertEqual(self.snake.pos(2), Point2D(2, 0))
        self.assertEqual(self.snake.pos(3), Point2D(1, 0))
        self.assertEqual(self.snake.pos(4), Point2D(0, 0))

    def test_step_direction(self):
        self.snake.makeStep()
        self.assertEqual(self.snake.head(), Point2D(5, 0))
        self.assertEqual(self.snake.size(), 5)
        self.assertEqual(self.snake.pos(0), Point2D(5, 0))
        self.assertEqual(self.snake.pos(1), Point2D(4, 0))
        self.assertEqual(self.snake.pos(2), Point2D(3, 0))
        self.assertEqual(self.snake.pos(3), Point2D(2, 0))
        self.assertEqual(self.snake.pos(4), Point2D(1, 0))

        self.snake.setDirection(Direction.Down)
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 5)
        self.assertEqual(self.snake.pos(0), Point2D(5, 1))
        self.assertEqual(self.snake.pos(1), Point2D(5, 0))
        self.assertEqual(self.snake.pos(2), Point2D(4, 0))
        self.assertEqual(self.snake.pos(3), Point2D(3, 0))
        self.assertEqual(self.snake.pos(4), Point2D(2, 0))

        self.snake.setDirection(Direction.Left)
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 5)
        self.assertEqual(self.snake.pos(0), Point2D(4, 1))
        self.assertEqual(self.snake.pos(1), Point2D(5, 1))
        self.assertEqual(self.snake.pos(2), Point2D(5, 0))
        self.assertEqual(self.snake.pos(3), Point2D(4, 0))
        self.assertEqual(self.snake.pos(4), Point2D(3, 0))

        self.snake.makeStep()
        self.snake.setDirection(Direction.Up)
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 5)
        self.assertEqual(self.snake.pos(0), Point2D(3, 0))
        self.assertEqual(self.snake.pos(1), Point2D(3, 1))
        self.assertEqual(self.snake.pos(2), Point2D(4, 1))
        self.assertEqual(self.snake.pos(3), Point2D(5, 1))
        self.assertEqual(self.snake.pos(4), Point2D(5, 0))

    def test_step_apple(self):
        self.snake.setApple()
        self.snake.makeStep()
        self.snake.makeStep()
        self.snake.makeStep()
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 5)
        self.assertEqual(self.snake.pos(0), Point2D(8, 0))
        self.assertEqual(self.snake.pos(1), Point2D(7, 0))
        self.assertEqual(self.snake.pos(2), Point2D(6, 0))
        self.assertEqual(self.snake.pos(3), Point2D(5, 0))
        self.assertEqual(self.snake.pos(4), Point2D(4, 0))

        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 6)
        self.assertEqual(self.snake.pos(0), Point2D(9, 0))
        self.assertEqual(self.snake.pos(1), Point2D(8, 0))
        self.assertEqual(self.snake.pos(2), Point2D(7, 0))
        self.assertEqual(self.snake.pos(3), Point2D(6, 0))
        self.assertEqual(self.snake.pos(4), Point2D(5, 0))
        self.assertEqual(self.snake.pos(5), Point2D(4, 0))

    def test_step_over_edge(self):
        self.snake = Snake(self.field, Direction.Right,
                           [Point2D(9, 0),
                            Point2D(8, 0),
                            Point2D(7, 0),
                            Point2D(6, 0)])
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 4)
        self.assertEqual(self.snake.pos(0), Point2D(0, 0))
        self.assertEqual(self.snake.pos(1), Point2D(9, 0))
        self.assertEqual(self.snake.pos(2), Point2D(8, 0))
        self.assertEqual(self.snake.pos(3), Point2D(7, 0))

        self.snake = Snake(self.field, Direction.Left,
                           [Point2D(0, 0),
                            Point2D(1, 0),
                            Point2D(2, 0),
                            Point2D(3, 0)])
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 4)
        self.assertEqual(self.snake.pos(0), Point2D(9, 0))
        self.assertEqual(self.snake.pos(1), Point2D(0, 0))
        self.assertEqual(self.snake.pos(2), Point2D(1, 0))
        self.assertEqual(self.snake.pos(3), Point2D(2, 0))

        self.snake = Snake(self.field, Direction.Up,
                           [Point2D(0, 0),
                            Point2D(0, 1),
                            Point2D(0, 2),
                            Point2D(0, 3)])
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 4)
        self.assertEqual(self.snake.pos(0), Point2D(0, 9))
        self.assertEqual(self.snake.pos(1), Point2D(0, 0))
        self.assertEqual(self.snake.pos(2), Point2D(0, 1))
        self.assertEqual(self.snake.pos(3), Point2D(0, 2))

        self.snake = Snake(self.field, Direction.Down,
                           [Point2D(0, 9),
                            Point2D(0, 8),
                            Point2D(0, 7),
                            Point2D(0, 6)])
        self.snake.makeStep()
        self.assertEqual(self.snake.size(), 4)
        self.assertEqual(self.snake.pos(0), Point2D(0, 0))
        self.assertEqual(self.snake.pos(1), Point2D(0, 9))
        self.assertEqual(self.snake.pos(2), Point2D(0, 8))
        self.assertEqual(self.snake.pos(3), Point2D(0, 7))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSnake))
    return suite

if __name__ == '__main__':
    unittest.main()
