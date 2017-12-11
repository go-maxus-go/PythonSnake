from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QKeyEvent, QFont
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from random import randint
from time import sleep

from src.point import *
from src.field import *
from src.snake import *
from src.consolerender import *

class MainWnd(QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedSize(400, 300)
        self.setFont(QFont("Courier", 20))

        self.__interval = 500 # time delay between loops
        self.__field = Field(10, 10)
        self.__snakeSize = 5

        data = []
        for i in range(self.__snakeSize):
            data.append(Point2D(self.__snakeSize - i - 1, 0))
        self.__snake1 = Snake(self.__field, Direction.Right, data)
        data = []
        for i in range(self.__field.width() - self.__snakeSize, self.__field.width()):
            data.append(Point2D(i, self.__field.height() - 1))
        self.__snake2 = Snake(self.__field, Direction.Left, data)
        self.__apple = Point2D()
        self.__render = ConsoleRender(self.__field, [self.__snake1, self.__snake2], [self.__apple])
        self.putApple()
        self.render()

        self.__timer = QTimer()
        self.__timer.setInterval(self.__interval)
        self.__timer.timeout.connect(self.loop)
        self.__timer.start()

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

    def loop(self):
        self.__snake1.makeStep()
        self.__snake2.makeStep()
        if self.__snake1.head() == self.__apple:
            self.__snake1.setApple()
            self.putApple()
        if self.__snake2.head() == self.__apple:
            self.__snake2.setApple()
            self.putApple()

        snake1 = self.checkSnake(self.__snake1, self.__snake2)
        snake2 = self.checkSnake(self.__snake2, self.__snake1)
        if snake1 and not snake2:
            self.setText("Player 1 win")
        if snake2 and not snake1:
            self.setText("Player 2 win")
        if not snake1 and not snake2:
            self.setText("Sudden death")

        if not snake1 or not snake2:
            self.__timer.stop()
        else:
            self.render()

    def checkSnake(self, snake, opponent):
        if self.__field.cell(snake.head()) == CellType.Wall:
            return False
        for i in range(1, snake.size()):
            if snake.head() == snake.pos(i):
                return False

        for i in range(opponent.size()):
            if snake.head() == opponent.pos(i):
                return False

        return True

    def render(self):
        data = self.__render.render()
        text = ""
        for y in range(self.__field.height()):
            str = ""
            for x in range(self.__field.width()):
                str += data[x + y * self.__field.width()]
            text += str + '\n'
        self.setText(text)

    def keyPressEvent(self, ev: QKeyEvent):
        if ev.key() == QtCore.Qt.Key_W:
            self.__snake1.setDirection(Direction.Up)
        if ev.key() == QtCore.Qt.Key_A:
            self.__snake1.setDirection(Direction.Left)
        if ev.key() == QtCore.Qt.Key_S:
            self.__snake1.setDirection(Direction.Down)
        if ev.key() == QtCore.Qt.Key_D:
            self.__snake1.setDirection(Direction.Right)

        if ev.key() == QtCore.Qt.Key_Left:
            self.__snake2.setDirection(Direction.Left)
        if ev.key() == QtCore.Qt.Key_Right:
            self.__snake2.setDirection(Direction.Right)
        if ev.key() == QtCore.Qt.Key_Up:
            self.__snake2.setDirection(Direction.Up)
        if ev.key() == QtCore.Qt.Key_Down:
            self.__snake2.setDirection(Direction.Down)

        return super().keyPressEvent(ev)
