from PyQt5.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem
from qfluentwidgets.multimedia import SimpleMediaPlayBar

from entity.Audio import Audio
from ui.Ui_AudioFilterInterface import Ui_AudioFilterInterface


class AudioFilterView(QWidget, Ui_AudioFilterInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.simplePlayerBar = SimpleMediaPlayBar(self)

        # 初始化ui
        self.initView()

    def initView(self):
        # 初始化音频表格
        self.audiosTable.setColumnCount(2)
        self.audiosTable.setHorizontalHeaderLabels(['Title', 'SampleRate'])
        self.audiosTable.verticalHeader().hide()
        # 关闭双击编辑功能
        self.audiosTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 初始化播放组件
        self.verticalLayout_2.addWidget(self.simplePlayerBar)

    def addTabItem(self, audio: Audio):
        print("11")
        # 新加一行
        row_count = self.audiosTable.rowCount()
        self.audiosTable.insertRow(row_count)
        # 设置行的参数
        self.audiosTable.setItem(row_count, 0, QTableWidgetItem(audio.title))
        print("22")
        self.audiosTable.setItem(row_count, 1, QTableWidgetItem(str(audio.sampleRate / 1000) + " KHz"))
