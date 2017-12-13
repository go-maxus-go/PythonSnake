from src.neuron import *

class NeuronLayer:
    def __init__(self, inputCount: int, neuronCount: int):
        self.__neurons = []
        for i in range(neuronCount):
            self.__neurons += [Neuron(inputCount)]

    def calculate(self, data):
        res = []
        for neuron in self.__neurons:
            res += [neuron.calculate(data)]
        return res
