#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019年1月2日
@author: Irony
@site: https://pyqt.site https://github.com/PyQt5
@email: 892768447@qq.com
@file: Test.TestRotateButton
@description: 
"""

from PyQt5.QtWidgets import QHBoxLayout, QWidget
from Widgets.Buttons.RotateButton import RotateButton


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)
        layout.addWidget(
            RotateButton('6', self, minimumHeight=96, toolTip='旋转按钮'))
        layout.addWidget(
            RotateButton('',
                         self,
                         minimumHeight=96,
                         image='../Resources/Images/Avatars/avatar.png'))
        layout.addWidget(
            RotateButton('', self, minimumHeight=96, objectName='imageLabel'))


if __name__ == '__main__':
    import cgitb
    import sys
    sys.excepthook = cgitb.enable(1, None, 5, '')
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    RotateButton {
        font-size: 48px;
    }
    ToolTip > QLabel {
        color: white;
        border-radius: 5px;
        padding: 10px;
        background-color: rgba(77, 77, 77, 180);
    }
    #imageLabel {
        qproperty-image: "../Resources/Images/Avatars/avatar.png";
    }
    """)
    w = Window()
    w.show()
    sys.exit(app.exec_())
