# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FilterDesignerInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_FilterDesignerInterface(object):
    def setupUi(self, FilterDesignerInterface):
        FilterDesignerInterface.setObjectName("FilterDesignerInterface")
        FilterDesignerInterface.resize(943, 590)
        self.horizontalLayout = QtWidgets.QHBoxLayout(FilterDesignerInterface)
        self.horizontalLayout.setContentsMargins(20, 40, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.SimpleCardWidget = SimpleCardWidget(FilterDesignerInterface)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.SimpleCardWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.confirmButton = PrimaryPushButton(self.SimpleCardWidget)
        self.confirmButton.setObjectName("confirmButton")
        self.verticalLayout_3.addWidget(self.confirmButton)
        self.verticalLayout.addWidget(self.SimpleCardWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.SimpleCardWidget_2 = SimpleCardWidget(FilterDesignerInterface)
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.SimpleCardWidget_2)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(FilterDesignerInterface)
        QtCore.QMetaObject.connectSlotsByName(FilterDesignerInterface)

    def retranslateUi(self, FilterDesignerInterface):
        _translate = QtCore.QCoreApplication.translate
        FilterDesignerInterface.setWindowTitle(_translate("FilterDesignerInterface", "Form"))
        self.confirmButton.setText(_translate("FilterDesignerInterface", "确定"))
from qfluentwidgets import PrimaryPushButton, SimpleCardWidget
