import sys

from PyQt5.QtWidgets import QApplication

from model.AudioModel import AudioModel
from model.FilterModel import FilterModel
from presenter.AudioFilePresenter import AudioFilePresenter
from presenter.AudioFilterPresenter import AudioFilterPresenter
from presenter.FilterPresenter import FilterPresenter
from presenter.RoutePresenter import RoutePresenter
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

        # 声明Presenter类
        routePresenter = RoutePresenter(myWin)
        audioFilePresenter = AudioFilePresenter(myWin.audioAnalysisView, myWin.audioFilterView, audioModel)
        filterPresenter = FilterPresenter(myWin.filterDesignerView, myWin.audioFilterView, filterModel)
        audioFilterPresenter = AudioFilterPresenter(myWin.audioFilterView, audioModel, filterModel)

        # 传递Presenter
        myWin.homeView.routePresenter = routePresenter
        myWin.audioAnalysisView.audioFilePresenter = audioFilePresenter
        myWin.filterDesignerView.filterPresenter = filterPresenter
        myWin.audioFilterView.audioFilterPresenter = audioFilterPresenter

        myWin.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"发生了未知异常: {e}")
