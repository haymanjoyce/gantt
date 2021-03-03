#!/usr/bin/env python3

from tkinter import Label, Button, Entry, filedialog, END, BOTH
from tkinter import Toplevel, scrolledtext, Canvas
from tkinter.ttk import Button
from math import floor
from PIL import Image
from utils import *
from io import BytesIO


class Preview(Toplevel):
    """
    This Canvas is used for generating images.
    Instance configured for display not adequate for generating images.
    Reconfiguration limitations mean cannot make one instance dual purpose.
    """

    def __init__(self, parent):
        super(Preview, self).__init__(parent)

        self.iconify()  # hack to suppress pre-configured window flash

        self.parent = parent

        self.title("Test")
        self.wm_iconbitmap("favicon.ico")

        self.grab_set()

        self.settings = get_settings()
        self.width = eval(self.settings['width'])
        self.height = eval(self.settings['height'])

        self.x = floor(((self.winfo_screenwidth() // 2) - self.width // 2))
        self.y = floor(((self.winfo_screenheight() // 2) - self.height // 2))

        self.resizable(False, False)

        self.canvas = Canvas(self)

        self.render()

        self.canvas.pack()

        self.deiconify()

        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y

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


class Log(Toplevel):
    def __init__(self, parent):
        super(Log, self).__init__(parent)

        self.parent = parent

        self.width = 400
        self.height = 400
        self.x = floor(self.parent.x + ((self.parent.width * 0.5) - 200))
        self.y = floor(self.parent.y + (self.parent.height * 0.2))
        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')  # w, h, x, y
        self.minsize(300, 300)

        self.title("Log")
        self.wm_iconbitmap("favicon.ico")
        # self.grab_set()

        self.scroller = scrolledtext.ScrolledText(self)
        self.scroller.configure(state='disabled')
        self.scroller.pack(expand=True, fill=BOTH)

        self.on_open()  # populate log

    def on_open(self):
        with open('app.log', "r") as log:
            text = str(log.read())
        self.scroller.configure(state='normal')  # writable
        self.scroller.insert(END, text)
        self.scroller.configure(state='disabled')  # readable


def save_image(postscript, settings):
    """Handles export of chart to various formats.  Requires Ghostscript on client machine."""
    file_types = [
        ('All files', '*.*'),
        ('PDF file', '*.pdf'),
        ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        ('BMP file', '*.bmp'),
        ('TIFF file', '*.tif'),
        ('PostScript file', '*.ps'),
    ]
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=file_types,
                                    defaultextension="*.*"
                                    )
    if file:
        file_name = file.name.lower()
        if file_name.endswith(('.pdf', '.jpg', '.png', '.bmp', '.tif', '.ps')):
            chart_encoded = postscript.encode('utf-8')
            chart_as_bytecode = BytesIO(chart_encoded)
            Image.open(chart_as_bytecode).save(file_name)
            cli.info('Chart saved as: ' + file_name)
        else:
            cli.warning("File type not recognised.")
    else:
        cli.info("Operation cancelled.")


def get_file_name(placeholder):
    file = filedialog.askopenfile(initialdir="/desktop", title="Select file",
                                  filetypes=(("Excel files", "*.xlsx"),))
    if file:
        file_name = file.name.lower()
    else:
        file_name = placeholder
        cli.debug("Operation cancelled.")
    return file_name


def export_data(df):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=(("Excel files", "*.xlsx"),),
                                    )
    if file:
        file_name = file.name.lower()
        if file_name.endswith(".xlsx"):
            df.to_excel(file_name)
            cli.info("Chart saved as" + file_name)
        else:
            cli.warning("File type not recognised.")
    else:
        cli.warning("Operation cancelled.")


cli = loggers.Stream()
