import sys

from PyQt5.QtWidgets import QApplication

from view.main_window_view import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
