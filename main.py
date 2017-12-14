import sys
from PyQt5.QtWidgets import QApplication

from src.mainwnd import *

if __name__ == '__main__':
#   genCount = 5
#   snakeCount = 16
#   snakesAi = []
#   engine = Engine()
#   inputParamCount = engine.field().width() * engine.field().height() + 6
#   for i in range(snakeCount):
#       snakesAi += [NeuronNetwork(inputParamCount, 4)]
#
#   for i in range(genCount):
#       print("generation number = ", i)
#       newGeneration = []
#       while len(snakesAi) >= 2:
#           print("snakesAi number = ", len(snakesAi))
#           snakeAi1 = snakesAi.pop()
#           snakeAi2 = snakesAi.pop()
#           engine = Engine()
#           bot1 = Bot(engine, snakeAi1, 0)
#           bot2 = Bot(engine, snakeAi2, 1)
#           state = State.InProgress
#           for step in range(100):
#               engine.setSnakeDirection(0, bot1.direction())
#               engine.setSnakeDirection(1, bot2.direction())
#               state = engine.loop()
#               if state != State.InProgress:
#                   break
#           if state == State.Player1Win:
#               newGeneration += [snakeAi1]
#           elif state == State.Player2Win:
#               newGeneration += [snakeAi2]
#           elif engine.snake(0).size() != engine.snake(1).size():
#               if engine.snake(0).size() > engine.snake(1).size():
#                   newGeneration += [snakeAi1]
#               else:
#                   newGeneration += [snakeAi2]
#           else:
#               snakesAi += [NeuronNetwork(inputParamCount, 4)]
#               snakesAi += [NeuronNetwork(inputParamCount, 4)]
#       while len(newGeneration) < snakeCount:
#           print("new generation size = ", len(newGeneration))
#           snake1 = random.randrange(0, len(newGeneration))
#           snake2 = random.randrange(0, len(newGeneration))
#           newGeneration += [newGeneration[snake1].makeChild(newGeneration[snake2])]
#       snakesAi = newGeneration

#   snakesAi[0].save()

    app = QApplication(sys.argv)
    wnd = MainWnd()
    wnd.show()
    sys.exit(app.exec_())
