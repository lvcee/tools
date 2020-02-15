#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__time__: 2020-02-14 11:46
"""

from lvce import *
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from tools_ui import Ui_Tools
from PyQt5.QtWidgets import QMenu, QAction, QApplication
from PyQt5.QtGui import QIcon
from for_anki import create_link, show_link
# import webbrowser
# import pyperclip
# from lvce import *
# from collections import namedtuple
# import re
import qdarkstyle


class Tools(QtWidgets.QWidget, Ui_Tools):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_system_tray()
        self.anki()

    # 设置托盘
    def set_system_tray(self):
        self.tray = QtWidgets.QSystemTrayIcon(self)
        self.tray.setIcon(QIcon('tool.png'))

        self.tray.activated.connect(self.system_tray_event)  # 设置托盘点击事件处理函数

        self.tray_menu = QMenu(self)
        self.RestoreAction = QAction('还原 ', self, triggered=self.show)
        self.QuitAction = QAction('退出 ', self, triggered=self.close)
        self.tray_menu.addAction(self.RestoreAction)
        self.tray_menu.addAction(self.QuitAction)
        self.tray.setContextMenu(self.tray_menu)
        self.tray.setToolTip('Lvce Tools')
        self.tray.show()

    # 点击托盘程序，显示或隐藏窗口，如果窗口离图标太远则移动到图标附近
    def system_tray_event(self):
        if self.isHidden():
            self.show()
            self.activateWindow()
        else:
            self.hide()

        pos = QtGui.QCursor.pos()  # type: QtCore.QPoint
        geometry = self.geometry()  # type: QtCore.QRect

        if not pos.x() - (geometry.x() + geometry.width()) < 100 and not pos.y(
        ) - (geometry.y() + geometry.height()) < 100:
            size = self.size()  # type: QtCore.QSize
            offset = 10
            x = pos.x() - size.width() - offset
            y = pos.y() - size.height() - offset
            self.move(x, y)

    # 最小化到托盘
    def hideEvent(self, event):
        self.hide()
        event.ignore()



    def anki(self):
        self.anki_create_link_btn.pressed.connect(create_link)


def set_windows(window:QtWidgets.QWidget):
    window.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())



if __name__ == '__main__':
    window(Tools, func=set_windows, flag=True)
