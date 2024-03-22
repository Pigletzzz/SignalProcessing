from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QAbstractItemView
from qfluentwidgets import FluentIcon
from qfluentwidgets.multimedia import SimpleMediaPlayBar

from controller.AudioFileController import AudioFileController
from entity.Audio import Audio
from tool.UnitTool import byteToMB, secToMMSS
from ui.Ui_AudioAnalysisInterface import Ui_AudioAnalysisInterface


class AudioAnalysisView(QWidget, Ui_AudioAnalysisInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.audioFileController: AudioFileController = None

        self.initView()
        self.initEvent()

    # 初始化界面
    def initView(self):
        self.fileButton.setIcon(FluentIcon.FOLDER)

        self.filesTable.setColumnCount(2)
        self.filesTable.setHorizontalHeaderLabels(['Title', 'Duration'])
        # self.TableWidget.setBorderVisible(True)
        self.filesTable.verticalHeader().hide()
        # 关闭双击编辑功能
        self.filesTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 初始化音频bar
        self.simplePlayerBar = SimpleMediaPlayBar(self)
        self.verticalLayout_4.addWidget(self.simplePlayerBar)

    # 初始化事件
    def initEvent(self):
        self.fileButton.clicked.connect(self.onFileButtonClicked)
        self.filesTable.itemSelectionChanged.connect(self.onItemChose)

    # 文件选择按下事件
    def onFileButtonClicked(self):
        # 打开文件选择器
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;MP3 Files (*.mp3);;WAV Files (*.wav)",
                                                  options=options)

        if fileName:
            self.audioFileController.readFile(fileName)

    # 为table添加一项
    def addTabItem(self, audio: Audio):
        # 新加一行
        row_count = self.filesTable.rowCount()
        self.filesTable.insertRow(row_count)
        # 设置行的参数
        self.filesTable.setItem(row_count, 0, QTableWidgetItem(audio.title))
        self.filesTable.setItem(row_count, 1, QTableWidgetItem(secToMMSS(audio.duration)))
        self.filesTable.selectRow(row_count)

        # self.showAudio(audio)

    def onItemChose(self):
        self.audioFileController.selectFile(self.filesTable.selectedIndexes()[0].row())

    def setupAudio(self, audio: Audio):
        # 进行详细信息的显示
        _translate = QtCore.QCoreApplication.translate
        self.fileNameLabel.setText(_translate("AudioAnalysisInterface", audio.title))
        self.fileDirLabel.setText(_translate("AudioAnalysisInterface", audio.path))
        self.fileSizeLabel.setText(_translate("AudioAnalysisInterface", byteToMB(audio.size)))
        self.sampleRateLabel.setText(_translate("AudioAnalysisInterface", str(audio.sampleRate / 1000) + " KHz"))
        self.durationLabel.setText(_translate("AudioAnalysisInterface", str(secToMMSS(audio.duration))))

        # 设置播放器器资源
        self.simplePlayerBar.player.setSource(QUrl.fromLocalFile(audio.path + '/' + audio.title))

    def resizeEvent(self, event: QResizeEvent):
        super().resizeEvent(event)
        self.setLabelMaxSize()

    def setLabelMaxSize(self):
        # TODO 根据GraphicsView的宽度设置这个宽度
        maxWidth = self.SimpleCardWidget.width() - self.StrongBodyLabel_6.width() - 24
        self.fileNameLabel.setMaximumWidth(maxWidth if maxWidth > 100 else 100)
        self.fileDirLabel.setMaximumWidth(maxWidth if maxWidth > 100 else 100)
