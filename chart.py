#!/usr/bin/env python3

import loggers
from tkinter import Canvas, BOTH, Scrollbar, HORIZONTAL, VERTICAL, X, Y, LEFT, RIGHT, TOP, BOTTOM
from settings import *


class Chart(Canvas):
    def __init__(self, parent):
        super(Chart, self).__init__(parent)

        self.parent = parent

        self.configure(bg="#dddddd")

        self.settings = get_settings()
        self.width = eval(self.settings['width'])
        self.height = eval(self.settings['height'])

        h_bar = Scrollbar(self.parent, orient=HORIZONTAL)
        h_bar.pack(side=BOTTOM, fill=X)
        h_bar.config(command=self.xview)
        v_bar = Scrollbar(self.parent, orient=VERTICAL)
        v_bar.pack(side=RIGHT, fill=Y)
        v_bar.config(command=self.yview)

        self.config(xscrollcommand=h_bar.set, yscrollcommand=v_bar.set)
        self.config(scrollregion=(0, 0, self.width, self.height))

        self.pack(fill=BOTH, expand=True)

        self.draw()

    def draw(self):
        self.create_rectangle(0, 0, self.width, self.height, fill="#ff0000")
        self.create_rectangle(0, 0, self.width//2, self.height//2, fill="#0000ff")
        self.create_rectangle(0, 0, self.width//3, self.height//3, fill="#00ff00")
        self.create_rectangle(0, 0, self.width//4, self.height//4, fill="#ff0000", outline="#000")

    def refresh(self):
        self.delete("all")
        self.settings = get_settings()
        self.width = eval(self.settings['width'])
        self.height = eval(self.settings['height'])
        self.config(scrollregion=(0, 0, self.width, self.height))
        self.update()
        self.draw()


cli = loggers.Stream()
