# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VoiceAnalysisInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VoiceAnalysisInterface(object):
    def setupUi(self, VoiceAnalysisInterface):
        VoiceAnalysisInterface.setObjectName("VoiceAnalysisInterface")
        VoiceAnalysisInterface.resize(505, 421)
        self.horizontalLayout = QtWidgets.QHBoxLayout(VoiceAnalysisInterface)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleLabel = TitleLabel(VoiceAnalysisInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        self.TitleLabel.setObjectName("TitleLabel")
        self.verticalLayout.addWidget(self.TitleLabel)
        self.SimpleCardWidget_3 = SimpleCardWidget(VoiceAnalysisInterface)
        self.SimpleCardWidget_3.setObjectName("SimpleCardWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SimpleCardWidget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SubtitleLabel = SubtitleLabel(self.SimpleCardWidget_3)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.horizontalLayout_2.addWidget(self.SubtitleLabel)
        self.IconWidget = IconWidget(self.SimpleCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IconWidget.sizePolicy().hasHeightForWidth())
        self.IconWidget.setSizePolicy(sizePolicy)
        self.IconWidget.setObjectName("IconWidget")
        self.horizontalLayout_2.addWidget(self.IconWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.TableView = TableView(self.SimpleCardWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableView.sizePolicy().hasHeightForWidth())
        self.TableView.setSizePolicy(sizePolicy)
        self.TableView.setObjectName("TableView")
        self.verticalLayout_2.addWidget(self.TableView)
        self.verticalLayout.addWidget(self.SimpleCardWidget_3)
        self.SimpleCardWidget = SimpleCardWidget(VoiceAnalysisInterface)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.verticalLayout.addWidget(self.SimpleCardWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.SimpleCardWidget_2 = SimpleCardWidget(VoiceAnalysisInterface)
        self.SimpleCardWidget_2.setObjectName("SimpleCardWidget_2")
        self.horizontalLayout.addWidget(self.SimpleCardWidget_2)

        self.retranslateUi(VoiceAnalysisInterface)
        QtCore.QMetaObject.connectSlotsByName(VoiceAnalysisInterface)

    def retranslateUi(self, VoiceAnalysisInterface):
        _translate = QtCore.QCoreApplication.translate
        VoiceAnalysisInterface.setWindowTitle(_translate("VoiceAnalysisInterface", "Form"))
        self.TitleLabel.setText(_translate("VoiceAnalysisInterface", "Voice Analysis"))
        self.SubtitleLabel.setText(_translate("VoiceAnalysisInterface", "Subtitle label"))
from qfluentwidgets import IconWidget, SimpleCardWidget, SubtitleLabel, TableView, TitleLabel
