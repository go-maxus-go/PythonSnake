import math
import random

class Neuron:
    def __init__(self, inputCount: int):
        self.__weights = []
        for i in range(inputCount):
            self.__weights += [random.random()]

    def calculate(self, data):
        res = 0
        for i in range(len(self.__weights)):
            res += self.__weights[i] * data[i]
        return 1 / (1 + math.exp(-res))

    def weights(self):
        return self.__weights

    def setWeights(self, weights):
        self.__weights = weights

    def makeChild(self, neuron):
        weights = []
        for i in range(len(self.__weights)):
            coin = random.randint(-1, 1)
            rand = random.random() - 0.5
            adder = coin * rand / 10
            if rand > 0:
                weights += [self.__weights[i] + adder]
            else:
                weights += [neuron.weights()[i] + adder]
        newNeuron = Neuron(0)
        newNeuron.setWeights(weights)
        return newNeuron

