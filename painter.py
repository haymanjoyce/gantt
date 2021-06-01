#!/usr/bin/env python3

import logging
import datetime

from tkinter import Canvas

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

    def draw_line(self):
        pass

    def draw_arrow(self):
        pass

    # SCALES

    def draw_intervals(self):
        items = [item for item in self.items if item.type == 'interval']
        for item in items:
            self.draw_interval(item)
            self.draw_interval_label(item)

    def draw_interval(self, item):
        self.draw_rectangle(x=item.x, y=item.y, rect_width=item.width, rect_height=item.height, fill=item.fill,
                            outline=item.border_color, width=item.border_width, tag=item.type)

    def draw_interval_label(self, item):
        y = item.y + (item.height / 2)
        text = item.date.strftime(item.format)
        self.create_text(item.x, y, text=text, anchor="w")

    # ROWS

    def draw_rows(self):
        items = [item for item in self.items if item.type == 'row']
        for item in items:
            self.draw_row(item)
            self.draw_row_label(item)

    def draw_row(self, item):
        self.draw_rectangle(x=item.x, y=item.y, rect_width=item.width, rect_height=item.height, fill=item.fill,
                            outline=item.border_color, width=item.border_width, tag=item.type)

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
                            outline=item.border_color, width=item.border_width, tag=item.type)

    # LABELS

    def draw_labels(self):
        items = [item for item in self.items if item.type == 'label']
        for item in items:
            self.draw_label(item)

    def draw_label(self, item):
        self.create_text(item.x, item.y, text=item.text, anchor=item.anchor, font=item.font, justify=item.justify,
                         width=item.width, fill=item.color)