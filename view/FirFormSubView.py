from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget

from ui.Ui_FIRFormInterface import Ui_FIRFormInterface


class FirFormSubView(QWidget, Ui_FIRFormInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.initView()

    def initView(self):
        typeItems = ['低通', '高通', '带通', '带阻']
        self.typesBox.addItems(typeItems)
        self.typesBox.setCurrentIndex(-1)

        windowItems = ['矩形窗', '巴特列特窗', '汉宁窗', '海明窗', '布拉克曼窗', '凯泽窗']
        self.windowsBox.addItems(windowItems)
        self.windowsBox.setCurrentIndex(-1)

        # 为输入框配置限制器
        # TODO 找另一种方法替换限制器
        validator = QIntValidator(self)
        validator.setBottom(0)
        self.sampleRateEdit.setValidator(validator)
        self.orderEdit.setValidator(validator)
        self.cutoffEditLow.setValidator(validator)
