#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__time__: 2020-02-15 11:25
"""

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from PyQt5 import QtWidgets, QtCore, QtGui
from aqt import utils
import webbrowser

# from aqt import gui_hooks
from anki import hooks

from anki.hooks import runHook, addHook
import anki
import json
import re




def show_on_onenote():
    # card = mw.col.sched.getCard()  # type: anki.cards.Card
    card = mw.reviewer.card  # type: anki.cards.Card
    data = re.findall(r'(onenote:#.*?.one)', card.q())
    webbrowser.open_new(data[0])



action = QAction("在OneNote打开", mw)
action.setShortcut('Alt+O')
action.triggered.connect(show_on_onenote)
mw.form.menuTools.addAction(action)



"""
def myfunc():
    # print("question shown, card question is:", card.q())
    # showInfo(card.q())
    showInfo('test')

addHook('showAnswer', myfunc)

"""



# something
