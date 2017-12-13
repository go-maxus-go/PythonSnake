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

    def neurons(self):
        return self.__neurons

    def setNeurons(self, neurons):
        self.__neurons = neurons

    def makeChild(self, layer):
        neurons = []
        for i in range(len(self.__neurons)):
            neurons += [self.__neurons[i].makeChild(layer.neurons()[i])]
        layer = NeuronLayer(0, 0)
        layer.setNeurons(neurons)
        return layer

