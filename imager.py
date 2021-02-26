#!/usr/bin/env python3

import loggers
from io import BytesIO
from PIL import Image
from settings import *
from tkinter import Toplevel, Canvas, BOTH
from math import floor
import settings


class Imager(Toplevel):
    def __init__(self, parent):
        super(Imager, self).__init__(parent)

        self.title("Test")
        self.wm_iconbitmap("favicon.ico")

        self.parent = parent

        self.settings = get_settings()
        self.width = eval(self.settings['width'])
        self.height = eval(self.settings['height'])

        # minsize / fixed

        # ensure only one instance

        self.x = floor((self.winfo_screenwidth()//2) - (self.width//2))
        self.y = floor((self.winfo_screenheight()//2) - (self.height//2))

        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')  # w, h, x, y

        self.canvas = Canvas(self)
        self.canvas.pack()

        self.render()

    def draw(self, width, height):
        self.canvas.create_rectangle(0, 0, width, height, fill="#ff0000")
        self.canvas.create_rectangle(0, 0, width // 2, height // 2, fill="#0000ff")
        self.canvas.create_rectangle(0, 0, width // 3, height // 3, fill="#00ff00")
        self.canvas.create_rectangle(0, 0, width // 4, height // 4, fill="#ff0000", outline="#000")

    def render(self):
        self.canvas.delete("all")  # required for redraw (e.g. on settings change)
        self.canvas.config(width=self.width, height=self.height)
        self.draw(self.width, self.height)

    def to_bytecode(self):
        to_postscript = self.canvas.postscript()
        to_utf8 = to_postscript.encode('utf-8')
        return BytesIO(to_utf8)


cli = loggers.Stream()

