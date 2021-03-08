#!/usr/bin/env python3

import loggers
from tkinter import Canvas
from utils import get_settings


class Drawing(Canvas):
    def __init__(self, parent):
        super(Drawing, self).__init__(parent)

        self.parent = parent

        self.settings = get_settings()
        self.chart_width = eval(self.settings['width'])
        self.chart_height = eval(self.settings['height'])
        self.config(width=self.chart_width, height=self.chart_height)

    def build_placeholder(self):
        self.create_rectangle(0, 0, self.chart_width, self.chart_height, fill="#ff0000")
        self.create_rectangle(0, 0, self.chart_width // 2, self.chart_height // 2, fill="#0000ff")
        self.create_rectangle(0, 0, self.chart_width // 3, self.chart_height // 3, fill="#00ff00")
        self.create_rectangle(0, 0, self.chart_width // 4, self.chart_height // 4, fill="#ff0000")


cli = loggers.Stream()
log = loggers.File()

