from src.field import *
import copy

class Direction(enumerate):
    Up = -1
    Down = 1
    Left = -2
    Right = 2

class Snake:
    def __init__(self, field, direction, data):
        self.__direction = direction
        self.__last_direction = direction
        self.__data = data
        self.__apples = []
        self.__field = field
        if not data:
            raise "Snake data is empty"

    def head(self):
        return copy.copy(self.__data[0])

    def direction(self):
        return copy.copy(self.__direction)

    def setDirection(self, direction):
        if self.__last_direction != -direction:
            self.__direction = direction

    def size(self):
        return len(self.__data)

    def pos(self, index):
        return copy.copy(self.__data[index])

    def isInCell(self, point: Point2D):
        return point in self.__data

    def setApple(self):
        if not self.__apples or self.__apples[-1] != self.head():
            self.__apples.append(self.head())

    def makeStep(self):
        self.__last_direction = self.__direction

        if len(self.__apples) > 0 and self.__apples[0] == self.__data[-1]:
            self.__apples.pop(0)
        else:
            self.__data.pop()

        head = self.head()
        if self.__direction == Direction.Left:
            head.x -= 1
        if self.__direction == Direction.Right:
            head.x += 1
        if self.__direction == Direction.Up:
            head.y -= 1
        if self.__direction == Direction.Down:
            head.y += 1

        if head.x < 0:
            head.x = self.__field.width() - 1
        if head.y < 0:
            head.y = self.__field.height() - 1
        if head.x >= self.__field.width():
            head.x = 0
        if head.y >= self.__field.height():
            head.y = 0

        self.__data = [head] + self.__data
