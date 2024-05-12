import librosa
import numpy as np
from PyQt5.QtCore import QCoreApplication, Qt, QUrl
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem, QStackedWidget, QLabel, QVBoxLayout
from matplotlib import pyplot
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from qfluentwidgets import Pivot
from qfluentwidgets.multimedia import SimpleMediaPlayBar

from entity.Audio import Audio
from entity.Filter import PassbandType, FilterType
from presenter.AudioFilterPresenter import AudioFilterPresenter
from ui.Ui_AudioFilterInterface import Ui_AudioFilterInterface


class AudioFilterView(QWidget, Ui_AudioFilterInterface):
    def __init__(self, parent=None, audioFilterPresenter: AudioFilterPresenter = None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.audioFilterPresenter = audioFilterPresenter

        self.simplePlayerBar = SimpleMediaPlayBar(self)

        # 导航栏相关成员变量声明
        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        # 子页面成员变量声明
        self.originGraphyInterface = QWidget()
        self.processedGraphyInterface = QWidget()

        # 声明原始音频子页面画图相关成员变量
        self.verticalLayout_7 = QVBoxLayout(self.originGraphyInterface)
        self.originStftFigure = pyplot.figure()
        self.originStftCanvas = FigureCanvasQTAgg(self.originStftFigure)
        self.originTimeFigure = pyplot.figure()
        self.originTimeCanvas = FigureCanvasQTAgg(self.originTimeFigure)

        # 声明处理后音频子页面画图相关成员变量
        self.verticalLayout_8 = QVBoxLayout(self.processedGraphyInterface)
        self.processedStftFigure = pyplot.figure()
        self.processedStftCanvas = FigureCanvasQTAgg(self.processedStftFigure)
        self.processedTimeFigure = pyplot.figure()
        self.processedTimeCanvas = FigureCanvasQTAgg(self.processedTimeFigure)

        # 初始化ui
        self.initView()
        # 初始化点击事件
        self.initEvent()

    def initView(self):
        # 初始化音频表格
        self.audiosTable.setColumnCount(2)
        self.audiosTable.setHorizontalHeaderLabels(['Title', 'SampleRate'])
        self.audiosTable.verticalHeader().hide()
        # 关闭双击编辑功能
        self.audiosTable.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 初始化菜单栏
        self.verticalLayout_5.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        # 添加子页
        self.addSubInterface(self.processedGraphyInterface, 'ProcessedGraphyInterface', '处理后音频')
        self.addSubInterface(self.originGraphyInterface, 'OriginGraphyInterface', '原始音频')
        # 设置默认页面
        self.stackedWidget.setCurrentWidget(self.processedGraphyInterface)
        self.pivot.setCurrentItem(self.processedGraphyInterface.objectName())

        # 初始化原始音频页面和初始化图表
        self.verticalLayout_7.addWidget(self.originStftCanvas)
        self.verticalLayout_7.addWidget(self.originTimeCanvas)
        # 初始化处理后音频页面和初始化图表
        self.verticalLayout_8.addWidget(self.processedStftCanvas)
        self.verticalLayout_8.addWidget(self.processedTimeCanvas)

        # 初始化播放组件
        self.verticalLayout_2.addWidget(self.simplePlayerBar)

    def initEvent(self):
        self.filterButton.clicked.connect(self.onFilterButtonClick)
        self.audiosTable.itemClicked.connect(self.onItemChanged)

    # 为audioTable新增项目
    def addAudio(self, audio: Audio):
        # 新加一行
        row_count = self.audiosTable.rowCount()
        self.audiosTable.insertRow(row_count)
        # 设置行的参数
        self.audiosTable.setItem(row_count, 0, QTableWidgetItem(audio.title))
        self.audiosTable.setItem(row_count, 1, QTableWidgetItem(str(audio.sampleRate / 1000) + " KHz"))

    # 更新滤波器信息
    def addFilter(self, filterType: FilterType, passband: PassbandType, sampleRate: int, cutoff):
        _translate = QCoreApplication.translate
        if filterType == FilterType.FIR:
            self.typeLabel.setText(_translate("AudioFilterInterface", "FIR滤波器"))
        else:
            self.typeLabel.setText(_translate("AudioFilterInterface", "IIR滤波器"))

        if passband == PassbandType.LOWPASS:
            self.passbandLabel.setText(_translate("AudioFilterInterface", "低通"))
        elif passband == PassbandType.HIGHPASS:
            self.passbandLabel.setText(_translate("AudioFilterInterface", "高通"))
        elif passband == PassbandType.BANDPASS:
            self.passbandLabel.setText(_translate("AudioFilterInterface", "带通"))
        else:
            self.passbandLabel.setText(_translate("AudioFilterInterface", "带阻"))

        self.cutoffLabel.setText(_translate("AudioFilterInterface", str(cutoff)))
        # 检查是否已选择音频，更新截止频率的信息
        self.onItemChanged()

    # “滤波”按钮的回调函数
    def onFilterButtonClick(self):
        self.audioFilterPresenter.audioFilter(self.audiosTable.selectedIndexes())

    # 添加子页面的方法
    def addSubInterface(self, widget: QLabel, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    # 画出滤波器前后语音的波形图
    def plotOriginAudio(self, y, sr):
        # 滤波器前的波形图
        self.originStftFigure.clf()
        originStftPlot = self.originStftFigure.subplots()
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='linear', ax=originStftPlot)
        self.originStftCanvas.draw()

        self.originTimeFigure.clf()
        originTimePlot = self.originTimeFigure.subplots()
        librosa.display.waveshow(y, sr=sr, ax=originTimePlot)
        self.originTimeCanvas.draw()

    def plotProcessedAudio(self, yout, sr):
        # 滤波后的波形图
        self.processedStftFigure.clf()
        processedStftPlot = self.processedStftFigure.subplots()
        D = librosa.amplitude_to_db(np.abs(librosa.stft(yout)), ref=np.max)
        librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='linear', ax=processedStftPlot)
        self.processedStftCanvas.draw()

        self.processedTimeFigure.clf()
        processedTimePlot = self.processedTimeFigure.subplots()
        librosa.display.waveshow(yout, sr=sr, ax=processedTimePlot)
        self.processedTimeCanvas.draw()

    # 当选择的
    def onItemChanged(self):
        if len(self.audiosTable.selectedIndexes()) == 0:
            return
        sampleRate = self.audioFilterPresenter.getCurrentAudioInfo(self.audiosTable.selectedIndexes()[0].row())
        _translate = QCoreApplication.translate
        # TODO 进不去这个if else
        if self.cutoffLabel.text().title() == '低通' or self.cutoffLabel.text().title() == '高通':
            cutoff = float(self.passbandLabel.text().title())
            self.passbandLabel.setText(_translate("AudioFilterView", str(cutoff * sampleRate) + 'Hz'))
        elif self.cutoffLabel.text().title() == '带通' or self.cutoffLabel.text().title() == '带阻':
            cutoffstr = self.passbandLabel.text().title().strip('[]').split(',')
            cutoff = [float(cutoffstr[0]) * sampleRate, float(cutoffstr[1]) * sampleRate]
            self.passbandLabel.setText(_translate("AudioFilterView", str(cutoff * sampleRate)))

    def setPlayer(self, path: str):
        self.simplePlayerBar.player.setSource(QUrl.fromLocalFile(path))
