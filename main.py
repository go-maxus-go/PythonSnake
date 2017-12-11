import sys
from src.mainwnd import *
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = MainWnd()
    wnd.show()

    sys.exit(app.exec_())
