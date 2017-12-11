from random import randint

from src.point import *
from src.field import *
from src.snake import *
from src.consolerender import *

class State(enumerate):
    InProgress = 0
    SuddenDeath = 1
    Player1Win = 2
    Player2Win = 3

class Engine:
    def __init__(self):
        self.__field = Field(10, 10)
        self.__snakeSize = 5
        self.__state = State.InProgress

        data1 = []
        for i in range(self.__snakeSize):
            data1.append(Point2D(self.__snakeSize - i - 1, 0))
        data2 = []
        for i in range(self.__field.width() - self.__snakeSize, self.__field.width()):
            data2.append(Point2D(i, self.__field.height() - 1))
        self.__snakes = [Snake(self.__field, Direction.Right, data1),
                         Snake(self.__field, Direction.Left, data2)]

        self.__apple = Point2D()
        self.putApple()
        self.__render = ConsoleRender(self.__field, self.__snakes, [self.__apple])

    def field(self):
        return copy.copy(self.__field)

    def state(self):
        return copy.copy(self.__state)

    def apple(self):
        return copy.copy(self.__apple)

    def snake(self, index):
        return copy.copy(self.__snakes[index])

    def setSnakeDirection(self, index: int, direction: Direction):
        self.__snakes[index].setDirection(direction)

    def putApple(self):
        while True:
            self.__apple.x = randint(0, self.__field.width() - 1)
            self.__apple.y = randint(0, self.__field.height() - 1)
            breaker = True
            for snake in self.__snakes:
                for i in range(snake.size()):
                    if snake.pos(i) == self.__apple:
                        breaker = False
            if self.__field.cell(self.__apple) == CellType.Wall:
                continue
            if breaker:
                break

    def loop(self):
        if self.state() != State.InProgress:
            return self.state()

        for snake in self.__snakes:
            snake.makeStep()
            if snake.head() == self.__apple:
                snake.setApple()
                self.putApple()

        snake1 = self.checkSnake(self.__snakes[0], self.__snakes[1])
        snake2 = self.checkSnake(self.__snakes[1], self.__snakes[0])
        if snake1 and not snake2:
            self.__state = State.Player1Win
        if snake2 and not snake1:
            self.__state = State.Player2Win
        if not snake1 and not snake2:
            self.__state = State.SuddenDeath

        return self.state()

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
        return text

    def checkCell(self, point: Point2D):
        if self.__field.cell(point) == CellType.Wall:
            return True
        for snake in self.__snakes:
            for i in range(snake.size()):
                if snake.pos(i) == point:
                    return True
        return False

    def adjustCellCoordinates(self, point: Point2D):
        while point.x < 0:
            point.x += self.__field.width()
        while point.y < 0:
            point.y += self.__field.height()
        while point.x >= self.__field.width():
            point.x -= self.__field.width()
        while point.y >= self.__field.height():
            point.y -= self.__field.height()
        return point

    def getParams(self, index: int):
        snake = self.__snakes[index]
        head = snake.head()
        result = [head.x, head.y]

        if snake.direction() == Direction.Up:
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y - 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x, head.y - 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y - 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y)))]
        if snake.direction() == Direction.Right:
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x, head.y - 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y - 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y + 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x, head.y + 1)))]
        if snake.direction() == Direction.Down:
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x + 1, head.y + 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x, head.y + 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y + 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y)))]
        if snake.direction() == Direction.Left:
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x, head.y + 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y + 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x - 1, head.y - 1)))]
            result += [self.checkCell(self.adjustCellCoordinates(Point2D(head.x, head.y - 1)))]

        result += [self.apple().x, self.apple().y]
        return result
