from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QKeyEvent, QFont
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore

from src.point import *
from src.field import *
from src.snake import *
from src.engine import *
from src.consolerender import *
from src.bot import *

class MainWnd(QLabel):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedSize(400, 300)
        self.setFont(QFont("Courier", 20))

        self.__engine = Engine()
        self.__bot = Bot(self.__engine)

        self.__timer = QTimer()
        self.__timer.setInterval(500)
        self.__timer.timeout.connect(self.loop)
        self.__timer.start()

    def loop(self):
        self.__engine.setSnakeDirection(self.__bot.index(), self.__bot.direction())
        state = self.__engine.loop()
        if state == State.Player1Win:
            self.setText("Player 1 win")
        if state == State.Player2Win:
            self.setText("Player 2 win")
        if state == State.SuddenDeath:
            self.setText("Sudden death")

        if state != State.InProgress:
            self.__timer.stop()
        else:
            self.setText(self.__engine.render())

    def keyPressEvent(self, ev: QKeyEvent):
        # Player 1
        if ev.key() == QtCore.Qt.Key_Left:
            self.__engine.setSnakeDirection(0, Direction.Left)
        if ev.key() == QtCore.Qt.Key_Right:
            self.__engine.setSnakeDirection(0, Direction.Right)
        if ev.key() == QtCore.Qt.Key_Up:
            self.__engine.setSnakeDirection(0, Direction.Up)
        if ev.key() == QtCore.Qt.Key_Down:
            self.__engine.setSnakeDirection(0, Direction.Down)
        # Player 2
#       if ev.key() == QtCore.Qt.Key_W:
#           self.__engine.setSnakeDirection(1, Direction.Up)
#       if ev.key() == QtCore.Qt.Key_A:
#           self.__engine.setSnakeDirection(1, Direction.Left)
#       if ev.key() == QtCore.Qt.Key_S:
#           self.__engine.setSnakeDirection(1, Direction.Down)
#       if ev.key() == QtCore.Qt.Key_D:
#           self.__engine.setSnakeDirection(1, Direction.Right)
        return super().keyPressEvent(ev)
