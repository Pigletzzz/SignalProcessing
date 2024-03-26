import sys

from PyQt5.QtWidgets import QApplication

from controller.AudioFileController import AudioFileController
from controller.FilterController import FilterController
from controller.route_controller import RouteController
from model.AudioModel import AudioModel
from model.FilterModel import FilterModel
from view.MainWindowView import MainWindow

if __name__ == '__main__':
    # TEST 执行一次convert编译ui文件
    # convertUi2Py()

    try:
        app = QApplication(sys.argv)
        myWin = MainWindow()

        # 声明Model类
        audioModel = AudioModel()
        filterModel = FilterModel()

        # 声明Controller类
        routeController = RouteController(myWin)
        audioFileController = AudioFileController(myWin.audioAnalysisView, myWin.audioFilterView, audioModel)
        filterController = FilterController(myWin.filterDesignerView, filterModel)

        # 传递Controller
        myWin.homeView.routeController = routeController
        myWin.audioAnalysisView.audioFileController = audioFileController
        myWin.filterDesignerView.filterController = filterController

        myWin.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"发生了未知异常: {e}")
