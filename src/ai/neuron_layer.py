from src.ai.neuron import *


class NeuronLayer:
    def __init__(self, inputCount: int, neuronCount: int):
        self.__neurons = []
        self.__deviation = random.random() * 2 - 1
        for i in range(neuronCount):
            self.__neurons += [Neuron(inputCount)]

    def calculate(self, data):
        res = []
        for neuron in self.__neurons:
            res += [neuron.calculate(data)]
        return res

    def neurons(self):
        return self.__neurons

    def setNeurons(self, neurons):
        self.__neurons = neurons

    def deviation(self):
        return self.__deviation

    def setDeviation(self, deviation):
        self.__deviation = deviation

    def makeChild(self, layer):
        neurons = []
        for i in range(len(self.__neurons)):
            neurons += [self.__neurons[i].makeChild(layer.neurons()[i])]
        layer = NeuronLayer(0, 0)
        layer.setNeurons(neurons)
        layer.setDeviation((self.deviation() + layer.deviation()) / 2)
        return layer
