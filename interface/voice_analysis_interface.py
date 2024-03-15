from PyQt5.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from ui.Ui_VoiceAnalysisInterface import Ui_VoiceAnalysisInterface
class VoiceAnalysisInterface(QWidget, Ui_VoiceAnalysisInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.IconWidget.setIcon(FluentIcon.FOLDER)