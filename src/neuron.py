import math
import random

class Neuron:
    def __init__(self, inputCount: int):
        self.__inputWeights = []
        for i in range(inputCount):
            self.__inputWeights += [random.random()]

    def calculate(self, data):
        res = 0
        for i in range(len(self.__inputWeights)):
            res += self.__inputWeights[i] * data[i]
        return 1 / (1 + math.exp(-res))
