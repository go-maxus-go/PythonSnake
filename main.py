import sys
from PyQt5.QtWidgets import QApplication

from src.mainwnd import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = MainWnd()
    wnd.show()

    sys.exit(app.exec_())
