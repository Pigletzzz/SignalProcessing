from PyQt5.QtWidgets import QWidget, QAbstractItemView

from ui.Ui_VoiceFilterInterface import Ui_VoiceFilterInterface


class VoiceFilterView(QWidget, Ui_VoiceFilterInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.initView()

    def initView(self):
        self.voiceTable.setColumnCount(2)

        self.voiceTable.setHorizontalHeaderLabels(['Title', 'SampleRate'])
        # self.TableWidget.setBorderVisible(True)
        self.voiceTable.verticalHeader().hide()
        # 关闭双击编辑功能
        self.voiceTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
