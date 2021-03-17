#!/usr/bin/env python3

import loggers
import utils
from tkinter import Canvas
from utils import get_settings


class Drawer(Canvas):
    def __init__(self, parent):
        super(Drawer, self).__init__(parent)

        self.parent = parent
        self.workbook = self.parent.workbook

        self.settings = get_settings()
        self.chart_width = int(self.settings['width'])
        self.chart_height = int(self.settings['height'])

        self.build_placeholder()
        self.draw_tasks()
        self.pack()

    def build_placeholder(self):
        self.config(width=self.chart_width, height=self.chart_height)
        self.create_rectangle(0, 0, self.chart_width, self.chart_height, fill="#ff0000")
        self.create_rectangle(0, 0, self.chart_width // 2, self.chart_height // 2, fill="#0000ff")
        self.create_rectangle(0, 0, self.chart_width // 3, self.chart_height // 3, fill="#00ff00")
        self.create_rectangle(0, 0, self.chart_width // 4, self.chart_height // 4, fill="#ff0000")

    def draw_tasks(self):
        sheet = self.workbook["Tasks"]
        text = sheet["A1"].value
        self.create_text(100, 100, text=text)


cli = loggers.Widget()
log = loggers.File(utils.get_path("data.log"))

