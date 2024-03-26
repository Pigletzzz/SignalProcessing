import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel, QVBoxLayout
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
        layout = QVBoxLayout()  # 垂直布局
        layout.addWidget(self.ampCanvas)
        self.amplitudePlotWidget.setLayout(layout)

        # 测试代码
        ax = self.ampFigure.subplots()
        t = np.linspace(0, 2 * np.pi, 50)
        ax.plot(t, np.sin(t))
        self.ampCanvas.draw()

        self.phaseFigure = pyplot.figure()
        self.phaseCanvas = FigureCanvasQTAgg(self.phaseFigure)
        layout = QVBoxLayout()  # 垂直布局
        layout.addWidget(self.phaseCanvas)
        self.amplitudePlotWidget.setLayout(layout)

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

            # 执行Fir图表显示
            # self.ampFigure.
        else:
            # IIR滤波器设计
            print('iir designer')

    def onPlotShow(self):
        print('update')

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
