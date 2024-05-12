from PyQt5.QtWidgets import QWidget

from presenter.RoutePresenter import RoutePresenter
from ui.Ui_HomeInterface import Ui_HomeInterface


class HomeView(QWidget, Ui_HomeInterface):
    def __init__(self, parent=None, routePresenter: RoutePresenter = None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.routePresenter = routePresenter

        self.initSignal()

    def initSignal(self):
        self.audioAnalysisButton.clicked.connect(self.onAudioAnalysisButtonClicked)
        self.filterDesignerButton.clicked.connect(self.onFilterDesignerButtonClicked)

    def onAudioAnalysisButtonClicked(self):
        self.routePresenter.routeToView(1)

    def onFilterDesignerButtonClicked(self):
        self.routePresenter.routeToView(2)
