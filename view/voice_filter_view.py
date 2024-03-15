from PyQt5.QtWidgets import QWidget

from ui.Ui_VoiceFilterInterface import Ui_VoiceFilterInterface


class VoiceFilterView(QWidget, Ui_VoiceFilterInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
