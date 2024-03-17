from PyQt5.QtWidgets import QWidget, QTableWidget, QTableView, QTableWidgetItem, QAbstractItemView
from qfluentwidgets import FluentIcon, TableWidget, TableItemDelegate

from ui.Ui_VoiceAnalysisInterface import Ui_VoiceAnalysisInterface


class VoiceAnalysisView(QWidget, Ui_VoiceAnalysisInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self._init_view()

    def _init_view(self):
        self.TransparentToolButton.setIcon(FluentIcon.FOLDER)
        self.TableWidget.setColumnCount(2)
        self.TableWidget.setHorizontalHeaderLabels(['Title', 'Duration'])
        self.TableWidget.setBorderVisible(True)
