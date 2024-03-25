import sys

from PyQt5.QtWidgets import QApplication

from controller.AudioFileController import AudioFileController
from controller.FilterController import FilterController
from controller.route_controller import RouteController
from convert2py import convertUi2Py
from model.AudioModel import AudioModel
from model.FilterModel import FilterModel
from view.MainWindowView import MainWindow

if __name__ == '__main__':
    # TEST 执行一次convert编译ui文件
    convertUi2Py()

    try:
        app = QApplication(sys.argv)
        myWin = MainWindow()

        audioModel = AudioModel()
        filterModel = FilterModel()

        routeController = RouteController(myWin)
        audioFileController = AudioFileController(myWin.audioAnalysisView, myWin.audioFilterView, audioModel)
        filterController = FilterController(myWin.filterDesignerView, filterModel)

        myWin.homeView.routeController = routeController
        myWin.audioAnalysisView.audioFileController = audioFileController
        myWin.filterDesignerView.filterController = filterController

        myWin.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"发生了未知异常: {e}")
