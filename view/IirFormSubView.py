from PyQt5.QtWidgets import QWidget

from ui.Ui_IIRFormInterface import Ui_IIRFormInterface


class IirFormSubView(QWidget, Ui_IIRFormInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
