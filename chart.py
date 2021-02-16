#!/usr/bin/env python3

import loggers
from tkinter import Canvas, BOTH


class Chart(Canvas):
    def __init__(self, parent):
        super(Chart, self).__init__(parent)

        self.parent = parent
        self.settings = parent.get_settings()

        self.configure(bg="#dddddd")
        self.pack(fill=BOTH, expand=True)

        self.create_rectangle(0, 0, 1600, 1600, fill="#ff0000")
        self.create_rectangle(0, 0, 800, 800, fill="#0000ff")
        self.create_rectangle(0, 0, 400, 400, fill="#00ff00")
        self.create_rectangle(0, 2, 200, 200, fill="#ff0000", outline="#000")


cli = loggers.Stream()
