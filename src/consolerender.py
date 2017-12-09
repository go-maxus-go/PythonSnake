from src.apple import *
from src.field import *
from src.snake import *

class Codes(enumerate):
    Empty = '.'
    Wall = 'X'
    Apple = '@'
    Snake = '*'
    HeadSnake = 'O'

class ConsoleRender:
    def __init__(self, field, snakes, apples):
        self.__field = field
        self.__snakes = snakes
        self.__apples = apples

    def render(self):
        data = list("")
        for y in range(self.__field.height()):
            for x in range(self.__field.width()):
                value = self.__field.cell(Point2D(x, y))
                if value == CellType.Empty:
                    data += Codes.Empty
                if value == CellType.Wall:
                    data += Codes.Wall

        for apple in self.__apples:
            data[self.__field.width() * apple.y() + apple.x()] = Codes.Apple

        for snake in self.__snakes:
            for i in range(snake.size()):
                point = snake.pos(i)
                if i == 0:
                    data[point.x + point.y * self.__field.width()] = Codes.HeadSnake
                else:
                   data[self.__field.width() * point.y + point.x] = Codes.Snake
        return data
