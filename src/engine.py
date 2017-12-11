from random import randint
from time import sleep

from src.point import *
from src.field import *
from src.snake import *
from src.consolerender import *

class Engine:
    def __init__(self, width: int, height: int, snakeSize: int, interval = .500):
        self.__interval = interval # time delay between loops
        self.__field = Field(width, height)
        # fill snake's data
        data = []
        for i in range(snakeSize):
            data.append(Point2D(snakeSize - i - 1, 0))
        self.__snake1 = Snake(self.__field, Direction.Right, data)
        data = []
        for i in range(width - snakeSize, width):
            data.append(Point2D(i, height - 1))
        self.__snake2 = Snake(self.__field, Direction.Left, data)
        self.__apple = Point2D()
        self.__render = ConsoleRender(self.__field, [self.__snake1, self.__snake2], [self.__apple])

    def putApple(self):
        while True:
            self.__apple.x = randint(0, self.__field.width() - 1)
            self.__apple.y = randint(0, self.__field.height() - 1)
            breaker = True
            for i in range(self.__snake1.size()):
                if self.__snake1.pos(i) == self.__apple:
                    breaker = False
            for i in range(self.__snake2.size()):
                if self.__snake2.pos(i) == self.__apple:
                    breaker = False
            if self.__field.cell(self.__apple) == CellType.Wall:
                continue
            if breaker:
                break

    def start(self):
        self.putApple()
        while True:
            self.render()
            sleep(self.__interval)
            self.__snake1.makeStep()
            self.__snake2.makeStep()
            if self.__snake1.head() == self.__apple:
                self.__snake1.setApple()
                self.putApple()
            if self.__snake2.head() == self.__apple:
                self.__snake2.setApple()
                self.putApple()

    def render(self):
        print('\n' * 100)
        data = self.__render.render()
        for y in range(self.__field.height()):
            str = ""
            for x in range(self.__field.width()):
                str += data[x + y * self.__field.width()]
            print(str)
