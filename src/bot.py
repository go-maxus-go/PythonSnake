from src.engine import *

class Bot:
    def __init__(self, engine: Engine, index = 1):
        self.__engine = engine
        self.__index = index

    def index(self):
        return self.__index

    def direction(self):
        return self.__engine.snake(self.__index).direction()
