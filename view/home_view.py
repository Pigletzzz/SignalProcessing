from PyQt5.QtWidgets import QWidget

from ui.Ui_HomeInterface import Ui_HomeInterface


class HomeView(QWidget, Ui_HomeInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
