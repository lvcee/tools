# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tools(object):
    def setupUi(self, Tools):
        Tools.setObjectName("Tools")
        Tools.resize(605, 428)
        self.groupBox = QtWidgets.QGroupBox(Tools)
        self.groupBox.setGeometry(QtCore.QRect(60, 110, 201, 71))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.anki_create_link_btn = QtWidgets.QPushButton(self.groupBox)
        self.anki_create_link_btn.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.anki_create_link_btn.setFlat(False)
        self.anki_create_link_btn.setObjectName("anki_create_link_btn")

        self.retranslateUi(Tools)
        QtCore.QMetaObject.connectSlotsByName(Tools)

    def retranslateUi(self, Tools):
        _translate = QtCore.QCoreApplication.translate
        Tools.setWindowTitle(_translate("Tools", "Lvce Tools"))
        self.groupBox.setTitle(_translate("Tools", "anki"))
        self.anki_create_link_btn.setText(_translate("Tools", "create_link"))
