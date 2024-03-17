import sys

from PyQt5.QtWidgets import QApplication

from controller.route_controller import RouteController
from view.main_window_view import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    routeController = RouteController(myWin, myWin.widgets)
    myWin.homeView.routeController = routeController

    myWin.show()
    sys.exit(app.exec_())
