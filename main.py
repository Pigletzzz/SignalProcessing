import sys

from PyQt5.QtWidgets import QApplication

from controller.AudioFileController import AudioFileController
from controller.route_controller import RouteController
from convert2py import convertUi2Py
from model.AudioModel import AudioModel
from view.MainWindowView import MainWindow

if __name__ == '__main__':
    try:
        # TEST 执行一次convert编译ui文件
        convertUi2Py()

        app = QApplication(sys.argv)
        myWin = MainWindow()

        AudioModel = AudioModel()

        routeController = RouteController(myWin)
        audioFileController = AudioFileController(myWin.audioAnalysisView, myWin.audioFilterView, AudioModel)

        myWin.homeView.routeController = routeController
        myWin.audioAnalysisView.audioFileController = audioFileController

        myWin.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"发生了未知异常: {e}")
