#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2019年1月8日
@author: Irony
@site: https://pyqt.site https://github.com/PyQt5
@email: 892768447@qq.com
@file: Widgets.ProgressButton
@description: 
"""

from PyQt5.QtCore import (QObject, QParallelAnimationGroup, QPauseAnimation,
                          QPropertyAnimation, QRectF, QSequentialAnimationGroup,
                          Qt, pyqtProperty, pyqtSignal)
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QPushButton


class CircleItem(QObject):

    _x = 0  # x坐标
    _opacity = 1  # 透明度0~1
    valueChanged = pyqtSignal()

    @pyqtProperty(float)
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x
        self.valueChanged.emit()

    @pyqtProperty(float)
    def opacity(self):
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        self._opacity = opacity


class ProgressButton(QPushButton):

    _waiting = False
    _circleRadius = 3  # 半径
    _circleColor = QColor(255, 255, 255)  # 圆圈颜色

    def __init__(self, *args, **kwargs):
        super(ProgressButton, self).__init__(*args, **kwargs)
        self._oldText = ''
        self._items = []

    def showWaiting(self, show=True):
        self.setEnabled(not show)
        self._waiting = show
        if show:
            self._oldText = self.text()
            self.setText('')
            self._items.clear()
            self._initAnimations()
            for _, animation in self._items:
                animation.start()
        else:
            self.setText(self._oldText)
            for _, animation in self._items:
                animation.stop()

    def paintEvent(self, event):
        if not self._waiting:
            # 交给原来的绘制
            super(ProgressButton, self).paintEvent(event)
            return
        # 自定义绘制
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setPen(Qt.NoPen)

        for item, _ in self._items:
            painter.save()
            color = self._circleColor.toRgb()
            color.setAlphaF(item.opacity)
            painter.setBrush(color)
            diameter = 2 * self._circleRadius
            painter.drawRoundedRect(
                QRectF(item.x / 100 * self.width() - diameter,
                       (self.height() - self._circleRadius) / 2, diameter,
                       diameter), self._circleRadius, self._circleRadius)
            painter.restore()

    def _initAnimations(self):
        for index in range(5):  # 5个小圆
            item = CircleItem(self)
            item.valueChanged.connect(self.update)
            # 串行动画组
            seqAnimation = QSequentialAnimationGroup(self)
            seqAnimation.setLoopCount(-1)
            self._items.append((item, seqAnimation))

            # 暂停延迟动画
            seqAnimation.addAnimation(QPauseAnimation(150 * index, self))

            # 加速,并行动画组1
            parAnimation1 = QParallelAnimationGroup(self)
            # 透明度
            parAnimation1.addAnimation(
                QPropertyAnimation(item,
                                   b'opacity',
                                   self,
                                   duration=400,
                                   startValue=0,
                                   endValue=1.0))
            # x坐标
            parAnimation1.addAnimation(
                QPropertyAnimation(item,
                                   b'x',
                                   self,
                                   duration=400,
                                   startValue=0,
                                   endValue=25.0))
            seqAnimation.addAnimation(parAnimation1)
            ##

            # 匀速
            seqAnimation.addAnimation(
                QPropertyAnimation(item,
                                   b'x',
                                   self,
                                   duration=2000,
                                   startValue=25.0,
                                   endValue=75.0))

            # 加速,并行动画组2
            parAnimation2 = QParallelAnimationGroup(self)
            # 透明度
            parAnimation2.addAnimation(
                QPropertyAnimation(item,
                                   b'opacity',
                                   self,
                                   duration=400,
                                   startValue=1.0,
                                   endValue=0))
            # x坐标
            parAnimation2.addAnimation(
                QPropertyAnimation(item,
                                   b'x',
                                   self,
                                   duration=400,
                                   startValue=75.0,
                                   endValue=100.0))
            seqAnimation.addAnimation(parAnimation2)
            ##

            # 暂停延迟动画
            seqAnimation.addAnimation(
                QPauseAnimation((5 - index - 1) * 150, self))

    @pyqtProperty(int)
    def circleRadius(self):
        return self._circleRadius

    @circleRadius.setter
    def circleRadius(self, radius):
        if self._circleRadius != radius:
            self._circleRadius = radius
            self.update()

    @pyqtProperty(QColor)
    def circleColor(self):
        return self._circleColor

    @circleColor.setter
    def circleColor(self, color):
        if self._circleColor != color:
            self._circleColor = color
            self.update()
