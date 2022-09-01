#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019年1月5日
@author: Irony
@site: https://pyqt.site https://github.com/PyQt5
@email: 892768447@qq.com
@file: Utils.Constants
@description: 常量
"""

from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QNetworkRequest

RoleRoot = Qt.UserRole + 1  # 根目录各个目录
RolePath = Qt.UserRole + 2  # item的绝对
RoleValue = Qt.UserRole + 3  # item当前进度条
RoleTotal = Qt.UserRole + 4  # item进度条总的值
RoleCode = Qt.UserRole + 5  # item代码

HomeFile = 'Resources/Markdown/index.html'

ConfigFile = 'Resources/Data/Config.ini'
UpgradeFile = 'Resources/Data/Upgrade/Upgrade.{}.zip'

ImageDir = 'Resources/Images/Avatars'
ImageAvatar = 'Resources/Images/Avatars/avatar.png'

LogName = 'PyQtClient'
LogFormatterDebug = '[%(asctime)s %(name)s %(module)s:%(funcName)s:%(lineno)s] %(levelname)-8s %(message)s'
LogFormatter = '[%(asctime)s %(name)s] %(levelname)-8s %(message)s'
LogFile = 'Resources/Data/app.log'

DirWallpaper = 'Resources/Images/Wallpaper'  # 壁纸目录
DirThemes = 'Resources/Themes'  # 主题目录
DirErrors = 'Resources/Data/Errors'  # 错误日志目录
DirProject = 'Resources/Data/Projects'  # 本地项目目录
DirProjects = 'Resources/Data/Projects/PyQt'  # 本地项目目录
DirCurrent = 'Resources/Data/Projects/PyQt'  # 当前README.md目录
CurrentReadme = ''  # 当前加载的README.md路径

AttrCallback = QNetworkRequest.User + 1
AttrFilePath = QNetworkRequest.User + 2
UrlProject = 'https://github.com/PyQt5/PyQtClient'
UrlQQ = 'tencent://message/?uin=892768447'
UrlGroup = 'tencent://groupwpa/?subcmd=all&param=7B2267726F757055696E223A3234363236393931392C2274696D655374616D70223A313531383537323831357D0A'
UrlIssues = 'https://github.com/PyQt5/PyQtClient/issues/new'
UrlGetAppsByCategory = 'http://bizhi.ludashi.com/live/wallpaper/categoryList?category={category}&pageno={pageno}&count={count}&type=1&_={time}'

_Sha = ''
_Account = ''
_Password = ''
_Username = ''
_Status = ''
_Emoji = ''
