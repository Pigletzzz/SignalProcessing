from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel
from qfluentwidgets import Pivot

from ui.Ui_FilterDesignerInterface import Ui_FilterDesignerInterface
from view.FirFormSubView import FirFormSubView
from view.IirFormSubView import IirFormSubView


class FilterDesignerView(QWidget, Ui_FilterDesignerInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)

        self.firInterface = FirFormSubView(self.SimpleCardWidget)
        self.iirInterface = IirFormSubView(self.SimpleCardWidget)

        self.initView()

    # 初始化布局
    def initView(self):
        self.horizontalLayout_4.addWidget(self.pivot, 0, Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.stackedWidget)

        self.addSubInterface(self.firInterface, 'firInterface', 'FIR')
        self.addSubInterface(self.iirInterface, 'iirInterface', 'IIR')

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.firInterface)
        self.pivot.setCurrentItem(self.firInterface.objectName())

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