# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/IIRFormInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_IIRFormInterface(object):
    def setupUi(self, IIRFormInterface):
        IIRFormInterface.setObjectName("IIRFormInterface")
        IIRFormInterface.resize(400, 370)
        self.formLayout = QtWidgets.QFormLayout(IIRFormInterface)
        self.formLayout.setObjectName("formLayout")
        self.BodyLabel_2 = BodyLabel(IIRFormInterface)
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_2)
        self.passbandsBox = ComboBox(IIRFormInterface)
        self.passbandsBox.setObjectName("passbandsBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.passbandsBox)
        self.BodyLabel = BodyLabel(IIRFormInterface)
        self.BodyLabel.setObjectName("BodyLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BodyLabel)
        self.sampleRateEdit = LineEdit(IIRFormInterface)
        self.sampleRateEdit.setText("")
        self.sampleRateEdit.setObjectName("sampleRateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sampleRateEdit)
        self.BodyLabel_3 = BodyLabel(IIRFormInterface)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_3)
        self.passbandFreqLowEdit = LineEdit(IIRFormInterface)
        self.passbandFreqLowEdit.setText("")
        self.passbandFreqLowEdit.setObjectName("passbandFreqLowEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passbandFreqLowEdit)
        self.BodyLabel_5 = BodyLabel(IIRFormInterface)
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_5)
        self.passbandFreqHighEdit = LineEdit(IIRFormInterface)
        self.passbandFreqHighEdit.setText("")
        self.passbandFreqHighEdit.setObjectName("passbandFreqHighEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passbandFreqHighEdit)
        self.stopbandFreqLowEdit = LineEdit(IIRFormInterface)
        self.stopbandFreqLowEdit.setText("")
        self.stopbandFreqLowEdit.setObjectName("stopbandFreqLowEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stopbandFreqLowEdit)
        self.BodyLabel_6 = BodyLabel(IIRFormInterface)
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_6)
        self.stopbandFreqHighEdit = LineEdit(IIRFormInterface)
        self.stopbandFreqHighEdit.setObjectName("stopbandFreqHighEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.stopbandFreqHighEdit)
        self.BodyLabel_7 = BodyLabel(IIRFormInterface)
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_7)
        self.passbandRippleEdit = LineEdit(IIRFormInterface)
        self.passbandRippleEdit.setText("")
        self.passbandRippleEdit.setObjectName("passbandRippleEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.passbandRippleEdit)
        self.BodyLabel_8 = BodyLabel(IIRFormInterface)
        self.BodyLabel_8.setObjectName("BodyLabel_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_8)
        self.stopbandAttenuationEdit = LineEdit(IIRFormInterface)
        self.stopbandAttenuationEdit.setText("")
        self.stopbandAttenuationEdit.setObjectName("stopbandAttenuationEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.stopbandAttenuationEdit)
        self.BodyLabel_9 = BodyLabel(IIRFormInterface)
        self.BodyLabel_9.setObjectName("BodyLabel_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_9)
        self.protoTypesBox = ComboBox(IIRFormInterface)
        self.protoTypesBox.setObjectName("protoTypesBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.protoTypesBox)
        self.BodyLabel_4 = BodyLabel(IIRFormInterface)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_4)

        self.retranslateUi(IIRFormInterface)
        QtCore.QMetaObject.connectSlotsByName(IIRFormInterface)

    def retranslateUi(self, IIRFormInterface):
        _translate = QtCore.QCoreApplication.translate
        IIRFormInterface.setWindowTitle(_translate("IIRFormInterface", "Form"))
        self.BodyLabel_2.setText(_translate("IIRFormInterface", "通带"))
        self.BodyLabel.setText(_translate("IIRFormInterface", "采样率"))
        self.BodyLabel_3.setText(_translate("IIRFormInterface", "通带频率"))
        self.BodyLabel_5.setText(_translate("IIRFormInterface", "通带高频率"))
        self.BodyLabel_6.setText(_translate("IIRFormInterface", "阻带高频率"))
        self.BodyLabel_7.setText(_translate("IIRFormInterface", "通带波纹"))
        self.BodyLabel_8.setText(_translate("IIRFormInterface", "阻带衰减"))
        self.BodyLabel_9.setText(_translate("IIRFormInterface", "原型"))
        self.BodyLabel_4.setText(_translate("IIRFormInterface", "阻带频率"))
from qfluentwidgets import BodyLabel, ComboBox, LineEdit
