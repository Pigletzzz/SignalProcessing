import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel
from matplotlib import pyplot
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from qfluentwidgets import Pivot, InfoBar, InfoBarPosition

from controller.FilterController import FilterController
from ui.Ui_FilterDesignerInterface import Ui_FilterDesignerInterface
from view.FirFormSubView import FirFormSubView
from view.IirFormSubView import IirFormSubView


class FilterDesignerView(QWidget, Ui_FilterDesignerInterface):
    def __init__(self, parent=None, filterController: FilterController = None):
        super().__init__(parent=parent)
        self.ampFigure = None
        self.ampCanvas = None
        self.phaseFigure = None
        self.phaseCanvas = None
        self.groupDelayFigure = None
        self.groupDelayCanvas = None
        self.zeroPoleFigure = None
        self.zeroPoleCanvas = None
        self.setupUi(self)

        self.filterController = filterController

        # 导航栏相关成员变量声明
        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)

        # 子页面成员变量声明
        self.firInterface = FirFormSubView(self.SimpleCardWidget)
        self.iirInterface = IirFormSubView(self.SimpleCardWidget)

        self.initView()
        self.initEvent()

    # 初始化布局
    def initView(self):
        # 初始化菜单栏
        self.horizontalLayout_4.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.addSubInterface(self.firInterface, 'firInterface', 'FIR')
        self.addSubInterface(self.iirInterface, 'iirInterface', 'IIR')

        self.stackedWidget.setCurrentWidget(self.firInterface)
        self.pivot.setCurrentItem(self.firInterface.objectName())

        # 初始化四个图表
        self.ampFigure = pyplot.figure()
        self.ampCanvas = FigureCanvasQTAgg(self.ampFigure)
        self.horizontalLayout_3.addWidget(self.ampCanvas)

        self.phaseFigure = pyplot.figure()
        self.phaseCanvas = FigureCanvasQTAgg(self.phaseFigure)
        self.horizontalLayout_3.addWidget(self.phaseCanvas)

        self.groupDelayFigure = pyplot.figure()
        self.groupDelayCanvas = FigureCanvasQTAgg(self.groupDelayFigure)
        self.horizontalLayout_2.addWidget(self.groupDelayCanvas)

        self.zeroPoleFigure = pyplot.figure()
        self.zeroPoleCanvas = FigureCanvasQTAgg(self.zeroPoleFigure)
        self.horizontalLayout_2.addWidget(self.zeroPoleCanvas)


    # 初始化点击事件
    def initEvent(self):
        # 导航栏点击事件
        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        # 确认按钮点击事件
        self.confirmButton.clicked.connect(self.onConfirmClicked)

    # 添加子页面的方法
    def addSubInterface(self, widget: QLabel, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    # 导航栏点击事件
    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())

    def onConfirmClicked(self):
        # TODO 读取的时候注意是否为空
        if self.stackedWidget.currentIndex() == 0:
            # FIR滤波器设计
            # 获取输入的数据
            passband = self.firInterface.typesBox.currentIndex()
            window = self.firInterface.windowsBox.currentIndex()
            order = self.firInterface.orderEdit.text()
            sampleRate = self.firInterface.sampleRateEdit.text()
            cutoffFreq1 = self.firInterface.cutoffEditLow.text()
            cutoffFreq2 = self.firInterface.cutoffEditHigh.text()

            # 执行Fir滤波器设计
            self.filterController.firDesign(sampleRate, order, cutoffFreq1, cutoffFreq2, passband, window)

        else:
            # IIR滤波器设计
            print('iir designer')

    def onPlotUpdate(self, w, h, fs, nfft):
        f = np.linspace(0, fs, nfft)
        h_db = 20 * np.log10(np.abs(h))  # 幅度响应（dB）
        h_angle = np.unwrap(np.angle(h))  # 相位响应（弧度）
        group_delay = -np.diff(h_angle) / (2.0 * np.pi) * fs / nfft  # 群延迟响应（秒）

        # 执行Fir图表显示
        # 绘制幅度响应
        self.ampFigure.clf()
        ampPlot = self.ampFigure.subplots()
        ampPlot.plot(f[:nfft // 2], h_db[:nfft // 2])
        ampPlot.set_title('Amplitude Response (dB)')
        ampPlot.set_xlabel('Frequency (Hz)')
        ampPlot.set_ylabel('Magnitude')
        ampPlot.grid(True)
        self.ampCanvas.draw()

        # 绘制相位响应
        self.phaseFigure.clf()
        phasePlot = self.phaseFigure.subplots()
        phasePlot.plot(f[:nfft // 2], h_angle[:nfft // 2])
        phasePlot.set_title('Phase Response (radians)')
        phasePlot.set_xlabel('Frequency (Hz)')
        phasePlot.set_ylabel('Phase')
        phasePlot.grid(True)
        self.phaseCanvas.draw()

        # 绘制群延迟响应
        self.groupDelayFigure.clf()
        groupDelayPlot = self.groupDelayFigure.subplots()
        groupDelayPlot.plot(f[1:nfft // 2], group_delay[1:nfft // 2])
        groupDelayPlot.set_title('Group Delay Response (seconds)')
        groupDelayPlot.set_xlabel('Frequency (Hz)')
        groupDelayPlot.set_ylabel('Group Delay')
        groupDelayPlot.grid(True)
        self.groupDelayCanvas.draw()

        # 绘制零极点分布
        self.zeroPoleFigure.clf()
        zeroPolePlot = self.zeroPoleFigure.subplots()

    def onFailedInfo(self, content: str):
        InfoBar.error(
            title='Error',
            content=content,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=5000,
            parent=self
        )
