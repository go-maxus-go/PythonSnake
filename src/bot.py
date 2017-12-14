from src.ai.neuron_network import *
from src.engine import *


class Bot:
    def __init__(self, engine: Engine, index: int = 1, ai: NeuronNetwork = None):
        self.__engine = engine
        self.__index = index
        self.__ai = ai

    def index(self):
        return self.__index

    def __checkCell(self, point: Point2D):
        while point.y < 0:
            point.y += self.__engine.field().height()
        while point.y >= self.__engine.field().height():
            point.y -= self.__engine.field().height()
        while point.x < 0:
            point.x += self.__engine.field().width()
        while point.x >= self.__engine.field().width():
            point.x -= self.__engine.field().width()

        if self.__engine.field().cell(point) == CellType.Wall:
            return True
        if self.__engine.snake(0).isInCell(point):
            return True
        if self.__engine.snake(1).isInCell(point):
            return True
        return False

    def __barierDistances(self, point: Point2D):
        counter = 0
        for i in range(1, self.__engine.field().height()):
            newPoint = Point2D(point.x, point.y - i)
            if self.__checkCell(newPoint):
                break
            else:
                counter += 1
        res = [counter]
        counter = 0
        for i in range(1, self.__engine.field().height()):
            newPoint = Point2D(point.x, point.y + i)
            if self.__checkCell(newPoint):
                break
            else:
                counter += 1
        res += [counter]
        counter = 0
        for i in range(1, self.__engine.field().width()):
            newPoint = Point2D(point.x - i, point.y)
            if self.__checkCell(newPoint):
                break
            else:
                counter += 1
        res += [counter]
        counter = 0
        for i in range(1, self.__engine.field().width()):
            newPoint = Point2D(point.x + i, point.y)
            if self.__checkCell(newPoint):
                break
            else:
                counter += 1
        res += [counter]
        return res

    def __getDistance(self, point1: Point2D, point2: Point2D):
        x = point2.x - point1.x
        if abs(x) > self.__engine.field().width() - abs(x):
            if x > 0:
                x = x - self.__engine.field().width()
            else:
                x = self.__engine.field().width() + x
        y = point2.y - point1.y
        if abs(y) > self.__engine.field().height() - abs(y):
            if y > 0:
                y = y - self.__engine.field().height()
            else:
                y = self.__engine.field().height() + y
        return Point2D(x, y)

    def direction(self):
        ownHead = self.__engine.snake(self.__index).head()
        data = self.__barierDistances(ownHead)

        oppIndex = 0
        if self.__index == 0:
            oppIndex = 1
        oppHead = self.__engine.snake(oppIndex).head()
        distance = self.__getDistance(ownHead, oppHead)
        data += [distance.x, distance.y]
        apple = self.__engine.apple()
        distance = self.__getDistance(ownHead, apple)
        data += [distance.x, distance.y]

        return self.calculateDirection(data)

    def calculateDirection(self, data):
        if not self.__ai:
            return self.__engine.snake(self.__index).direction()

        res = self.__ai.calculate(data)
        print(res)
        index = res.index(max(res))
        if index == 0:
            return Direction.Up
        if index == 1:
            return Direction.Left
        if index == 2:
            return Direction.Right
        if index == 3:
            return Direction.Down
        return self.__engine.snake(self.__index).direction()
