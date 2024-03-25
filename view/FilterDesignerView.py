from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel
from qfluentwidgets import Pivot

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
        self.horizontalLayout_4.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.addSubInterface(self.firInterface, 'firInterface', 'FIR')
        self.addSubInterface(self.iirInterface, 'iirInterface', 'IIR')

        self.stackedWidget.setCurrentWidget(self.firInterface)
        self.pivot.setCurrentItem(self.firInterface.objectName())

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
            order = int(self.firInterface.orderEdit.text())
            sampleRate = int(self.firInterface.sampleRateEdit.text())
            cutoffFreq = int(self.firInterface.cutoffEdit.text())

            # 执行Fir滤波器设计
            self.filterController.firDesign(sampleRate, order, cutoffFreq)
        else:
            # IIR滤波器设计
            print()
