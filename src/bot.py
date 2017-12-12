from src.engine import *

import math
import random


class Neuron:
    def __init__(self, inputCount: int, outputCount: int):
        self.__inputWeights = []
        for i in range(inputCount):
            self.__inputWeights += [random.random()]
        self.__outputWeights = []
        for i in range(outputCount):
            self.__outputWeights += [random.random()]

    def calculate(self, data):
        res = 0
        for i in range(len(self.__inputWeights)):
            res += self.__inputWeights[i] * data[i] / 4 # normalization
        res = 1 / (1 + math.exp(-res))

        output = []
        for weight in self.__outputWeights:
            output += [weight * res]

        return output

class Bot:
    def __init__(self, engine: Engine, index = 1):
        self.__engine = engine
        self.__index = index

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
                    data[pos.x + pos.y * w] = 3 # Own snake
                else:
                    data[pos.x + pos.y * w] = 4 # Enemy snake

        return self.calculateDirection(data)

    def calculateDirection(self, data):
        neuron = Neuron(len(data), 4)
        res = neuron.calculate(data)
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
