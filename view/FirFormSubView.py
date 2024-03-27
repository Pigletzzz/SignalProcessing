from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget

from ui.Ui_FIRFormInterface import Ui_FIRFormInterface


class FirFormSubView(QWidget, Ui_FIRFormInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.initView()
        self.initEvent()

    def initView(self):
        typeItems = ['低通', '高通', '带通', '带阻']
        self.typesBox.addItems(typeItems)
        self.typesBox.setCurrentIndex(-1)

        windowItems = ['矩形窗', '三角窗', '汉宁窗', '海明窗', '布拉克曼窗', '凯泽窗']
        self.windowsBox.addItems(windowItems)
        self.windowsBox.setCurrentIndex(-1)

        # 为输入框配置限制器
        # TODO 找另一种方法替换限制器
        validator = QIntValidator(self)
        validator.setBottom(0)
        self.sampleRateEdit.setValidator(validator)
        self.orderEdit.setValidator(validator)
        self.cutoffEditLow.setValidator(validator)
        self.cutoffEditHigh.setValidator(validator)

        # 删除第二行截止频率
        # 拿走一行并隐藏控件
        # 使用removeRow会将widget删除，导致无法再次显示
        self.formLayout.takeRow(4)
        self.cutoffEditHigh.hide()
        self.BodyLabel_6.hide()

    def initEvent(self):
        # 选择带通/带阻滤波器时的ui处理
        self.typesBox.currentIndexChanged.connect(self.onTypeChanged)

    def onTypeChanged(self):
        _translate = QCoreApplication.translate
        if self.typesBox.currentText() in ['高通', '低通'] and self.formLayout.rowCount() == 6:
            # 拿走一行并隐藏控件
            # 使用removeRow会将widget删除，导致无法再次显示
            self.formLayout.takeRow(4)
            self.cutoffEditHigh.hide()
            self.BodyLabel_6.hide()
            self.BodyLabel_3.setText(_translate("FIRFormInterface", "截止频率"))
        elif self.typesBox.currentText() in ['带通', '带阻'] and self.formLayout.rowCount() == 5:
            # 增加一行并显示，因为先前隐藏了控件
            self.formLayout.insertRow(4, self.BodyLabel_6,
                                      self.cutoffEditHigh)
            self.cutoffEditHigh.show()
            self.BodyLabel_6.show()
            self.BodyLabel_3.setText(_translate("FIRFormInterface", "低频率"))
            self.BodyLabel_6.setText(_translate("FIRFormInterface", "高频率"))
