from PyQt5.QtWidgets import QWidget, QAbstractItemView

from ui.Ui_AudioFilterInterface import Ui_AudioFilterInterface


class AudioFilterView(QWidget, Ui_AudioFilterInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.initView()

    def initView(self):
        self.audiosTable.setColumnCount(2)

        self.audiosTable.setHorizontalHeaderLabels(['Title', 'SampleRate'])
        # self.TableWidget.setBorderVisible(True)
        self.audiosTable.verticalHeader().hide()
        # 关闭双击编辑功能
        self.audiosTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
