from src.neuron_layer import *

import copy
import pickle

class NeuronNetwork:
    def __init__(self, inputCount: int, outputCount: int):
        self.__fname = 'gen/state.txt'
        neuronCount = 10
        self.__layers = [NeuronLayer(inputCount, neuronCount),
                         NeuronLayer(neuronCount, outputCount)]
    def calculate(self, data):
        res = copy.deepcopy(data)
        for layer in self.__layers:
            res = layer.calculate(res)
        return res

    def load(self):
        with open(self.__fname, 'rb') as f:
            self.__neurons = pickle.load(f)

    def save(self):
        with open(self.__fname, 'wb') as f:
            pickle.dump(self.__neurons, f)
