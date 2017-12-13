from src.engine import *
from src.neuron_network import *

class Bot:
    def __init__(self, engine: Engine, index = 1):
        self.__engine = engine
        self.__index = index
        self.__ai = NeuronNetwork(engine.field().width() * engine.field().height(), 4)

    def index(self):
        return self.__index

    def direction(self):
        data = []
        w = self.__engine.field().width()
        h = self.__engine.field().height()
        for y in range(h):
            for x in range(w):
                data += [self.__engine.field().cell(Point2D(x, y))]

        apple = self.__engine.apple()
        data[apple.x + apple.y * w] = 2 # apple
        for index in range(2):
            snake = self.__engine.snake(index)
            for i in range(snake.size()):
                pos = snake.pos(i)
                if index == self.__index:
                    if i == 0:
                        data[pos.x + pos.y * w] = 3 # Own head
                    else:
                        data[pos.x + pos.y * w] = 4 # Own snake
                else:
                    if i == 0:
                        data[pos.x + pos.y * w] = 5 # Enemy head
                    else:
                        data[pos.x + pos.y * w] = 6 # Enemy snake

        return self.calculateDirection(data)

    def calculateDirection(self, data):
        res = self.__ai.calculate(data)
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
