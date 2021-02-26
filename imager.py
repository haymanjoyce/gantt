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

        self.parent = parent

        self.settings = get_settings()
        self.width = eval(self.settings['width'])
        self.height = eval(self.settings['height'])

        self.width = 200
        self.minsize(200, 100)
        self.x = floor(self.parent.x + ((self.parent.width * 0.5) - 100))
        self.y = floor(self.parent.y + (self.parent.height * 0.2))

        self.title("Test")
        self.wm_iconbitmap("favicon.ico")

        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y

        self.canvas = Canvas(self)
        # self.canvas.config(width=800)
        # self.canvas.config(bg="blue")
        # self.canvas.pack(fill=BOTH)

        self.canvas.pack()

        self.render()

    def draw(self, width, height):
        self.canvas.create_rectangle(0, 0, width, height, fill="#ff0000")
        self.canvas.create_rectangle(0, 0, width // 2, height // 2, fill="#0000ff")
        self.canvas.create_rectangle(0, 0, width // 3, height // 3, fill="#00ff00")
        self.canvas.create_rectangle(0, 0, width // 4, height // 4, fill="#ff0000", outline="#000")

    def render(self):
        self.canvas.delete("all")  # required for redraw (e.g. on settings change)
        self.draw(self.width, self.height)

    def to_bytecode(self):
        to_postscript = self.canvas.postscript()
        to_utf8 = to_postscript.encode('utf-8')
        return BytesIO(to_utf8)


cli = loggers.Stream()

# we create canvas in TopLevel as it would appear as image (including margins for example)
# we create this class in chart module
# we need not show TopLevel - hidden
# the out put is output = Image.open(bytecode)
# this can be used to save files or paste to clipboard
# you can strip out code from save_image dialogue and just give it the prepared Image object
# this could become class in dialogues and Chart could become class in frames
