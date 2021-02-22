#!/usr/bin/env python3

import loggers
from tkinter import Canvas, BOTH, Scrollbar, HORIZONTAL, VERTICAL, X, Y, LEFT, RIGHT, TOP, BOTTOM


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

        self.config(width=200, height=200, scrollregion=(0, 0, 400, 2000))
        self.config(xscrollcommand=h_bar.set, yscrollcommand=v_bar.set)
        self.pack(fill=BOTH, expand=True)

        # canvas = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))
        # hbar = Scrollbar(frame, orient=HORIZONTAL)
        # hbar.pack(side=BOTTOM, fill=X)
        # hbar.config(command=canvas.xview)
        # vbar = Scrollbar(frame, orient=VERTICAL)
        # vbar.pack(side=RIGHT, fill=Y)
        # vbar.config(command=canvas.yview)
        # canvas.config(width=300, height=300)
        # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        # canvas.pack(side=LEFT, expand=True, fill=BOTH)

        self.create_rectangle(0, 0, 1600, 1600, fill="#ff0000")
        self.create_rectangle(0, 0, 800, 800, fill="#0000ff")
        self.create_rectangle(0, 0, 400, 400, fill="#00ff00")
        self.create_rectangle(0, 2, 200, 200, fill="#ff0000", outline="#000")


cli = loggers.Stream()
