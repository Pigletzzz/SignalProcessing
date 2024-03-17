from PyQt5.QtWidgets import QWidget

from controller.route_controller import RouteController
from ui.Ui_HomeInterface import Ui_HomeInterface


class HomeView(QWidget, Ui_HomeInterface):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.routeController: RouteController = None

        self.initSignal()

    def initSignal(self):
        self.voiceAnalysisButton.clicked.connect(self.onVoiceAnalysisButtonClicked)
        self.filterDesignerButton.clicked.connect(self.onFilterDesignerButtonClicked)

    def onVoiceAnalysisButtonClicked(self):
        self.routeController.routeToView(1)

    def onFilterDesignerButtonClicked(self):
        self.routeController.routeToView(2)
