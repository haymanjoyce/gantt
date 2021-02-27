#!/usr/bin/env python3

import loggers
from io import BytesIO
from PIL import Image
from settings import *
from tkinter import Toplevel, Canvas, BOTH
from math import floor
import settings


class Preview(Toplevel):
    """
    This Canvas is used for generating images.
    Instance configured for display not adequate for generating images.
    Reconfiguration limitations mean cannot make one instance dual purpose.
    """

    def __init__(self, parent):
        super(Preview, self).__init__(parent)

        self.parent = parent
        self.title("Test")

        self.iconify()  # hack to suppress pre-configured window flash
        self.wm_iconbitmap("favicon.ico")
        self.deiconify()

        self.settings = get_settings()
        self.width = eval(self.settings['width'])
        self.height = eval(self.settings['height'])

        self.x = floor(((self.winfo_screenwidth()//2) - self.width//2))
        self.y = floor(((self.winfo_screenheight()//2) - self.height//2))


        # ensure only one instance

        # hide

        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y

        self.resizable(False, False)

        self.canvas = Canvas(self)

        self.render()

        self.canvas.pack()



    def draw(self, x=0, y=0, width=100, height=100):
        self.canvas.create_rectangle(x, y, width, height, fill="#ff0000")
        self.canvas.create_rectangle(x, y, width // 2, height // 2, fill="#0000ff")
        self.canvas.create_rectangle(x, y, width // 3, height // 3, fill="#00ff00")
        self.canvas.create_rectangle(x, y, width // 4, height // 4, fill="#ff0000", outline="#000")

    def render(self):
        self.canvas.delete("all")  # required for redraw (e.g. on settings change)
        self.canvas.config(width=self.width, height=self.height)
        self.draw(0, 0, self.width, self.height)

    def to_bytecode(self):
        to_postscript = self.canvas.postscript()
        to_utf8 = to_postscript.encode('utf-8')
        return BytesIO(to_utf8)


cli = loggers.Stream()

