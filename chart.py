#!/usr/bin/env python3

import loggers
from tkinter import Canvas, BOTH, Scrollbar, HORIZONTAL, VERTICAL, X, Y, LEFT, RIGHT, TOP, BOTTOM
from tkinter import Toplevel
from settings import *
import copy


class Chart(Canvas):
    def __init__(self, parent):
        super(Chart, self).__init__(parent)

        self.parent = parent

        self.configure(bg="#dddddd")

        h_bar = Scrollbar(self.parent, orient=HORIZONTAL)
        h_bar.pack(side=BOTTOM, fill=X)
        h_bar.config(command=self.xview)
        v_bar = Scrollbar(self.parent, orient=VERTICAL)
        v_bar.pack(side=RIGHT, fill=Y)
        v_bar.config(command=self.yview)

        self.config(xscrollcommand=h_bar.set, yscrollcommand=v_bar.set)

        self.pack(fill=BOTH, expand=True)

        self.render()

    def draw(self, width, height):
        self.create_rectangle(0, 0, width, height, fill="#ff0000")
        self.create_rectangle(0, 0, width//2, height//2, fill="#0000ff")
        self.create_rectangle(0, 0, width//3, height//3, fill="#00ff00")
        self.create_rectangle(0, 0, width//4, height//4, fill="#ff0000", outline="#000")

    def render(self):
        settings = get_settings()
        width = eval(settings['width'])
        height = eval(settings['height'])
        self.delete("all")  # required for redraw (e.g. on settings change)
        self.config(scrollregion=(0, 0, width, height))
        self.draw(width, height)


cli = loggers.Stream()
