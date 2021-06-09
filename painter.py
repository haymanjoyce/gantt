#!/usr/bin/env python3

import logging
import datetime

from tkinter import Canvas
from tkinter.constants import *
from tkinter.font import Font
from tkinter.font import BOLD, NORMAL, ITALIC, ROMAN

from settings import Settings


class Painter(Canvas):
    def __init__(self, parent, data):
        super(Painter, self).__init__(parent)

        self.parent = parent
        self.items = data
        self.settings = Settings()
        self.config(width=self.settings.width, height=self.settings.height, background="#fff")
        self.pack()
        self.draw_rows()
        self.draw_bars()
        self.draw_intervals()
        self.draw_labels()
        self.draw_connectors()

    # SHAPES

    def draw_rectangle(self, x, y, rect_width, rect_height, **options):
        x1 = x
        y1 = y
        x2 = x + rect_width
        y2 = y + rect_height
        self.create_rectangle(x1, y1, x2, y2, options)

    def draw_diamond(self):
        pass

    def draw_circle(self):
        pass

    def draw_line(self, *points, arrow=LAST, arrow_shape=(8, 10, 3), capstyle=BUTT, dash=(), color='black',
                  joinstyle=ROUND, smooth=FALSE, tags='', width=1):
        options = {'arrow': arrow, 'arrowshape': arrow_shape, 'capstyle': capstyle, 'dash': dash, 'fill': color,
                   'joinstyle': joinstyle, 'smooth': smooth, 'tags': tags, 'width': width}
        self.create_line(points, **options)

    def draw_text(self, x, y, text='', anchor=CENTER, color='black', width=None, justify=None, tags=None, font=None,
                  size=None, bold=False, italic=False, underline=False, strikethrough=False):

        font_object = Font()
        # font_object = nametofont('TkFixedFont')  # caused global change

        family = font  # name change
        weight = bold
        slant = italic
        underline = int(underline)  # int required as argument
        overstrike = int(strikethrough)

        if size:
            size = 0 - size  # negative denotes pixels
        else:
            # size = font_object.actual()['size']  # does not return global default
            size = -12  # unable to find global default

        if weight:
            weight = BOLD
        else:
            weight = NORMAL

        if slant:
            slant = ITALIC
        else:
            slant = ROMAN

        font_options = {'family': family, 'size': size, 'weight': weight, 'slant': slant, 'underline': underline,
                        'overstrike': overstrike}

        font_object.config(**font_options)

        text_options = {'text': text, 'anchor': anchor, 'fill': color, 'width': width, 'justify': justify, 'tags': tags,
                        'font': font_object}

        self.create_text(x, y, **text_options)

    # SCALES

    def draw_intervals(self):
        items = [item for item in self.items if item.type == 'interval']
        for item in items:
            self.draw_interval(item)
            self.draw_interval_label(item)

    def draw_interval(self, item):
        self.draw_rectangle(x=item.x, y=item.y, rect_width=item.width, rect_height=item.height, fill=item.fill,
                            outline=item.border_color, width=item.border_width, tags=item.layer)

    def draw_interval_label(self, item):
        y = item.y + (item.height / 2)
        text = item.date.strftime(item.format)
        self.create_text(item.x, y, text=text, anchor="w")

    # ROWS

    def draw_rows(self):
        items = [item for item in self.items if item.type == 'row']
        for item in items:
            if self.settings.show_rows:
                self.draw_row(item)
            if self.settings.show_row_nums:
                self.draw_row_label(item)

    def draw_row(self, item):
        self.draw_rectangle(x=item.x, y=item.y, rect_width=item.width, rect_height=item.height, fill=item.fill,
                            outline=item.border_color, width=item.border_width, tags=item.layer)

    def draw_row_label(self, item):
        x = item.x + 20  # note, not proportional to width
        y = item.y + (item.height / 2)
        self.create_text(x, y, text=item.key, anchor="e")

    # BARS

    def draw_bars(self):
        items = [item for item in self.items if item.type == 'bar']
        for item in items:
            self.draw_bar(item)

    def draw_bar(self, item):
        self.draw_rectangle(x=item.x, y=item.y, rect_width=item.width, rect_height=item.height, fill=item.fill,
                            outline=item.border_color, width=item.border_width, tags=item.layer)

    # LABELS

    def draw_labels(self):
        items = [item for item in self.items if item.type == 'label']
        for item in items:
            self.draw_label(item)

    def draw_label(self, item):
        self.draw_text(item.x, item.y, text=item.text, anchor=item.anchor, color=item.color, width=item.width,
                       justify=item.justify, tags=item.layer, font=item.font, bold=item.bold, italic=item.italic,
                       underline=item.underline, strikethrough=item.strikethrough)

    # CONNECTORS

    def draw_connectors(self):
        items = [item for item in self.items if item.type == 'connector']
        for item in items:
            self.draw_connector(item)

    def draw_connector(self, item):
        point_1 = item.from_x, item.from_y
        point_2 = item.shaft_x, item.from_y
        point_3 = item.shaft_x, item.to_y
        point_4 = item.to_x, item.to_y

        points = point_1 + point_2 + point_3 + point_4

        self.draw_line(points, tags=item.layer,
                       color=item.color, width=item.width)


    # type = attrib(default="connector")
    # layer = attrib(default=None)
    # from_row = attrib(default=None)
    # from_date = attrib(default=None)
    # from_nudge = attrib(default=None)
    # to_row = attrib(default=None)
    # to_date = attrib(default=None)
    # to_nudge = attrib(default=None)
    # arrow_head = attrib(default=None)
    # shaft_nudge = attrib(default=None)
    # from_x = attrib(default=None)
    # from_y = attrib(default=None)
    # to_x = attrib(default=None)
    # to_y = attrib(default=None)
    # shaft_x = attrib(default=None)
    # width = attrib(default=0.0)
    # color = attrib(default="black")