from PyQt5.QtWidgets import QWidget

from ui.Ui_FilterDesignerInterface import Ui_FilterDesignerInterface
class FilterDesignerInterface(QWidget, Ui_FilterDesignerInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)