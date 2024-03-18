from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QFileDialog, QAbstractItemView
from qfluentwidgets import FluentIcon

from controller.voice_file_controller import VoiceFileController
from tool.time_tool import ms_to_min_sec
from ui.Ui_VoiceAnalysisInterface import Ui_VoiceAnalysisInterface
from voice import Voice


class VoiceAnalysisView(QWidget, Ui_VoiceAnalysisInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.voiceFileController: VoiceFileController = None

        self.initView()
        self.initEvent()

    # 初始化界面
    def initView(self):
        self.TransparentToolButton.setIcon(FluentIcon.FOLDER)
        self.TableWidget.setColumnCount(2)
        self.TableWidget.setHorizontalHeaderLabels(['Title', 'Duration'])
        self.TableWidget.setBorderVisible(True)
        self.TableWidget.verticalHeader().hide()
        # 关闭双击编辑功能
        self.TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # 初始化事件
    def initEvent(self):
        self.TransparentToolButton.clicked.connect(self.onFileButtonClicked)

    # 文件选择按下事件
    def onFileButtonClicked(self):
        # 打开文件选择器
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;MP3 Files (*.mp3);;WAV Files (*.wav)",
                                                  options=options)

        if fileName:
            self.voiceFileController.readFile(fileName)

    # 为table添加一项
    def addTabItem(self, voice: Voice):
        # 新加一行
        row_count = self.TableWidget.rowCount()
        self.TableWidget.insertRow(row_count)
        # 设置行的参数
        self.TableWidget.setItem(row_count, 0, QTableWidgetItem(voice.title))
        self.TableWidget.setItem(row_count, 1, QTableWidgetItem(ms_to_min_sec(voice.duration)))
