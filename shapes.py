#!/usr/bin/env python3

import logging
import math

from attr import attrs, attrib, Factory


@attrs
class Rectangle:
    x = attrib(default=0)
    y = attrib(default=0)
    fill = attrib(default="red")
    border_color = attrib(default="black")
    __width = attrib(default=800)
    __height = attrib(default=100)
    __border_width = attrib(default=0)
    _x = attrib(default=0)
    _y = attrib(default=0)
    _x0 = attrib(default=0)
    _y0 = attrib(default=0)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 6:
            self.__width = 6

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 6:
            self.__height = 6

    @property
    def border_width(self):
        return self.__border_width

    @border_width.setter
    def border_width(self, value):
        value = abs(int(value))  # ensure value is a positive integer
        even_border_width = math.ceil(value / 2) * 2  # for tidy rendering we need even numbers
        available_width = self.width - (even_border_width * 2)
        available_height = self.height - (even_border_width * 2)
        available_space = sorted([available_width, available_height])[0]
        if even_border_width >= available_space:
            even_border_width = math.ceil(available_space / 2) * 2
        if value == 0:
            self.__border_width = 0
            self._x = self.x
            self._y = self.y
            self._x0 = self.x + self.width
            self._y0 = self.y + self.height
        elif value < 1:  # under 1 treated as zero but outline still visible when 0 so hidden with fill color
            self.__border_width = 2
            self._x = self.x + 1
            self._y = self.y + 1
            self._x0 = self.x + self.width - 2
            self._y0 = self.y + self.height - 2
            self.border_color = self.fill
        else:
            self.__border_width = even_border_width
            self._x = self.x + (even_border_width / 2)
            self._y = self.y + (even_border_width / 2)
            self._x0 = self.x + self.width - even_border_width
            self._y0 = self.y + self.height - even_border_width
