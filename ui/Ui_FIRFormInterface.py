# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FIRFormInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_FIRFormInterface(object):
    def setupUi(self, FIRFormInterface):
        FIRFormInterface.setObjectName("FIRFormInterface")
        FIRFormInterface.resize(398, 295)
        self.formLayout = QtWidgets.QFormLayout(FIRFormInterface)
        self.formLayout.setObjectName("formLayout")
        self.BodyLabel_2 = BodyLabel(FIRFormInterface)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_2)
        self.typesBox = ComboBox(FIRFormInterface)
        self.typesBox.setObjectName("typesBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.typesBox)
        self.BodyLabel_5 = BodyLabel(FIRFormInterface)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_5)
        self.sampleRateEdit = LineEdit(FIRFormInterface)
        self.sampleRateEdit.setObjectName("sampleRateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sampleRateEdit)
        self.BodyLabel_4 = BodyLabel(FIRFormInterface)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_4)
        self.orderEdit = LineEdit(FIRFormInterface)
        self.orderEdit.setObjectName("orderEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.orderEdit)
        self.BodyLabel_3 = BodyLabel(FIRFormInterface)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_3)
        self.cutoffEditLow = LineEdit(FIRFormInterface)
        self.cutoffEditLow.setObjectName("cutoffEditLow")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cutoffEditLow)
        self.BodyLabel = BodyLabel(FIRFormInterface)
        self.BodyLabel.setObjectName("BodyLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.BodyLabel)
        self.windowsBox = ComboBox(FIRFormInterface)
        self.windowsBox.setObjectName("windowsBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.windowsBox)
        self.cutoffEditHigh = LineEdit(FIRFormInterface)
        self.cutoffEditHigh.setObjectName("cutoffEditHigh")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cutoffEditHigh)
        self.BodyLabel_6 = BodyLabel(FIRFormInterface)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_6)

        self.retranslateUi(FIRFormInterface)
        QtCore.QMetaObject.connectSlotsByName(FIRFormInterface)

    def retranslateUi(self, FIRFormInterface):
        _translate = QtCore.QCoreApplication.translate
        FIRFormInterface.setWindowTitle(_translate("FIRFormInterface", "Form"))
        self.BodyLabel_2.setText(_translate("FIRFormInterface", "类型"))
        self.BodyLabel_5.setText(_translate("FIRFormInterface", "采样率"))
        self.BodyLabel_4.setText(_translate("FIRFormInterface", "阶数"))
        self.BodyLabel_3.setText(_translate("FIRFormInterface", "截止频率"))
        self.BodyLabel.setText(_translate("FIRFormInterface", "窗函数"))
        self.BodyLabel_6.setText(_translate("FIRFormInterface", "高频率"))
from qfluentwidgets import BodyLabel, ComboBox, LineEdit
