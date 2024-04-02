from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QWidget

from ui.Ui_IIRFormInterface import Ui_IIRFormInterface


class IirFormSubView(QWidget, Ui_IIRFormInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.initView()
        self.initEvent()

    def initView(self):
        passbandItems = ['低通', '高通', '带通', '带阻']
        self.passbandsBox.addItems(passbandItems)
        self.passbandsBox.setCurrentIndex(-1)

        protoTypesItems = ['巴特沃兹', '切比雪夫-Ⅰ', '切比雪夫-Ⅱ', '椭圆']
        self.protoTypesBox.addItems(protoTypesItems)
        self.protoTypesBox.setCurrentIndex(-1)

        # 为输入框配置限制器
        # TODO 找另一种方法替换限制器
        intValidator = QIntValidator(self)
        doubleValidator = QDoubleValidator()
        intValidator.setBottom(0)
        doubleValidator.setBottom(0)
        self.sampleRateEdit.setValidator(intValidator)
        self.passbandFreqHighEdit.setValidator(intValidator)
        self.passbandFreqLowEdit.setValidator(intValidator)
        self.stopbandFreqHighEdit.setValidator(intValidator)
        self.stopbandFreqLowEdit.setValidator(intValidator)
        self.passbandRippleEdit.setValidator(doubleValidator)
        self.stopbandAttenuationEdit.setValidator(doubleValidator)

        # 隐藏通带高频率和阻带高频率
        self.formLayout.takeRow(3)
        self.BodyLabel_5.hide()
        self.passbandFreqHighEdit.hide()
        self.formLayout.takeRow(4)
        self.BodyLabel_6.hide()
        self.stopbandFreqHighEdit.hide()

    def initEvent(self):
        self.passbandsBox.currentIndexChanged.connect(self.onPassbandChanged)

    def onPassbandChanged(self):
        _translate = QCoreApplication.translate
        if self.passbandsBox.currentText() in ['高通', '低通'] and self.formLayout.rowCount() == 9:
            # 拿走一行并隐藏控件
            # 使用removeRow会将widget删除，导致无法再次显示
            self.formLayout.takeRow(3)
            self.BodyLabel_5.hide()
            self.passbandFreqHighEdit.hide()
            self.formLayout.takeRow(4)
            self.BodyLabel_6.hide()
            self.stopbandFreqHighEdit.hide()
        elif self.passbandsBox.currentText() in ['带通', '带阻'] and self.formLayout.rowCount() == 7:
            # 增加一行并显示，因为先前隐藏了控件
            self.formLayout.insertRow(3, self.BodyLabel_5, self.passbandFreqHighEdit)
            self.BodyLabel_5.show()
            self.passbandFreqHighEdit.show()
            # self.BodyLabel_3.setText(_translate("FIRFormInterface", "低频率"))
            self.formLayout.insertRow(5, self.BodyLabel_6, self.stopbandFreqHighEdit)
            self.BodyLabel_6.show()
            self.stopbandFreqHighEdit.show()
            # self.BodyLabel_6.setText(_translate("FIRFormInterface", "高频率"))
