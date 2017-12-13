from src.neuron_layer import *

import copy
import pickle

class NeuronNetwork:
    def __init__(self, inputCount: int, outputCount: int):
        self.__fname = 'gen/state.txt'
        neuronCount = inputCount
        self.__layers = [NeuronLayer(inputCount, neuronCount),
                         NeuronLayer(neuronCount, int(neuronCount / 2)),
                         NeuronLayer(int(neuronCount / 2), int(neuronCount / 4)),
                         NeuronLayer(int(neuronCount / 4), int(neuronCount / 10)),
                         NeuronLayer(int(neuronCount / 10), outputCount)]

    def calculate(self, data):
        res = copy.deepcopy(data)
        for i in range(len(res)):
            res[i] = res[i] / 10
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
