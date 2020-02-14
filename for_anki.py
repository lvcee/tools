#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__time__: 2020-02-14 10:21
"""

import webbrowser
import pyperclip
from lvce import *
from collections import namedtuple
import re


# 从剪切板获取onenote链接，转化为anki所需要的链接
def create_link():
    old_link = pyperclip.paste()

    """
    
    new_link = 'onenote:#必备&section-id={BDF6C2E5-A466-4384-9082-7EAF72C59A0B}&page-id={F0273EB6-BD46-4E70-8F6F-D5CE163E22E1}&end&base-path=https://d.docs.live.net/ceddce8c575b6400/文档/计算机/软件.one'
    old_link = 'https://onedrive.live.com/view.aspx?resid=CEDDCE8C575B6400%21583&id=documents&wd=target%28%E8%BD%AF%E4%BB%B6.one%7CBDF6C2E5-A466-4384-9082-7EAF72C59A0B%2F%E5%BF%85%E5%A4%87%7CF0273EB6-BD46-4E70-8F6F-D5CE163E22E1%2F%29\
               onenote:https://d.docs.live.net/ceddce8c575b6400/文档/计算机/软件.one#必备&section-id={BDF6C2E5-A466-4384-9082-7EAF72C59A0B}&page-id={F0273EB6-BD46-4E70-8F6F-D5CE163E22E1}&end '

    """

    Content = namedtuple('Content', ['one', 'name', 'section_id', 'page_id'])
    content = Content._make(*re.findall(r'.*?onenote:(.*?.one)#(.*?)&section-id={(.*?)}&page-id={(.*?)}&end', old_link))
    data = 'onenote:#{}&section-id={{{}}}&page-id={{{}}}&end&base-path={}'.format(content.name, content.section_id, content.page_id, content.one)
    link = '<a href="{}">onenote page</a>'.format(data)
    pyperclip.copy(link)


# 获取剪切板中的anki链接信息，然后打开OneNote页面
def show_link():
    link = pyperclip.paste()
    webbrowser.open_new(link)



if __name__ == '__main__':
    pass

