import copy
import pickle

from src.ai.neuron_layer import *


class NeuronNetwork:
    def __init__(self, inputCount: int, outputCount: int):
        self.__fname = 'gen/state.txt'
        self.__layers = [NeuronLayer(inputCount, inputCount * 3),
                         NeuronLayer(inputCount * 3, outputCount)]

    def calculate(self, data):
        res = copy.deepcopy(data)
        for layer in self.__layers:
            res = layer.calculate(res)
        return res

    def load(self):
        with open(self.__fname, 'rb') as f:
            self.__layers = pickle.load(f)

    def save(self):
        with open(self.__fname, 'wb') as f:
            pickle.dump(self.__layers, f)

    def layers(self):
        return self.__layers

    def setLayers(self, layers):
        self.__layers = layers

    def makeChild(self, network):
        layers = []
        for i in range(len(self.__layers)):
            layers += [self.__layers[i].makeChild(network.layers()[i])]
        newNetwork = NeuronNetwork(0, 0)
        newNetwork.setLayers(layers)
        return newNetwork
