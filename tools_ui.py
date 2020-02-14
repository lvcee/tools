# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tools(object):
    def setupUi(self, Tools):
        Tools.setObjectName("Tools")
        Tools.resize(605, 428)
        self.groupBox = QtWidgets.QGroupBox(Tools)
        self.groupBox.setGeometry(QtCore.QRect(60, 110, 176, 55))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.anki_create_link_btn = QtWidgets.QPushButton(self.groupBox)
        self.anki_create_link_btn.setObjectName("anki_create_link_btn")
        self.horizontalLayout.addWidget(self.anki_create_link_btn)
        self.anki_show_link_btn = QtWidgets.QPushButton(self.groupBox)
        self.anki_show_link_btn.setObjectName("anki_show_link_btn")
        self.horizontalLayout.addWidget(self.anki_show_link_btn)

        self.retranslateUi(Tools)
        QtCore.QMetaObject.connectSlotsByName(Tools)

    def retranslateUi(self, Tools):
        _translate = QtCore.QCoreApplication.translate
        Tools.setWindowTitle(_translate("Tools", "Lvce Tools"))
        self.groupBox.setTitle(_translate("Tools", "anki"))
        self.anki_create_link_btn.setText(_translate("Tools", "create_link"))
        self.anki_show_link_btn.setText(_translate("Tools", "show_link"))
