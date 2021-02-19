#!/usr/bin/env python3

import loggers
from tkinter import Label, Button, Entry, filedialog, END, BOTH
from tkinter import Toplevel, scrolledtext
from tkinter.ttk import Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
from math import floor
from PIL import Image
import io


class Settings(Toplevel):
    def __init__(self, parent):
        super(Settings, self).__init__(parent)

        self.parent = parent

        self.width = 200
        self.minsize(200, 100)
        self.x = floor(self.parent.x + ((self.parent.width * 0.5) - 100))
        self.y = floor(self.parent.y + (self.parent.height * 0.2))

        self.data = self.parent.get_settings()

        self.title("Settings")
        self.wm_iconbitmap("favicon.ico")
        self.configure(padx=10, pady=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.lbl_width = Label(self, text="Page width:")
        self.ent_width = Entry(self, width=10)
        self.lbl_height = Label(self, text="Page height:")
        self.ent_height = Entry(self, width=10)
        self.lbl_top_margin = Label(self, text="Top margin:")
        self.ent_top_margin = Entry(self, width=10)
        self.lbl_left_margin = Label(self, text="Left margin:")
        self.ent_left_margin = Entry(self, width=10)
        self.btn_save = Button(self, text="Save", command=self.on_save)
        self.btn_close = Button(self, text="Close", command=self.on_close)

        self.lbl_width.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.ent_width.grid(row=0, column=1, sticky="nsew", pady=(0, 5))
        self.lbl_height.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.ent_height.grid(row=1, column=1, sticky="nsew", pady=(0, 5))
        self.lbl_top_margin.grid(row=3, column=0, sticky="nsew", pady=(0, 5))
        self.ent_top_margin.grid(row=3, column=1, sticky="nsew", pady=(0, 5))
        self.lbl_left_margin.grid(row=4, column=0, sticky="nsew", pady=(0, 5))
        self.ent_left_margin.grid(row=4, column=1, sticky="nsew", pady=(0, 5))
        self.btn_save.grid(row=5, column=0, sticky="nsew", pady=(5, 0))
        self.btn_close.grid(row=5, column=1, sticky="nsew", pady=(5, 0))

        self.on_open()  # populate fields

        # you need to set geometry after grid established (for some reason)
        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y

    def on_open(self):
        if len(self.data.keys()) == 4:
            self.ent_width.insert(0, self.data["width"])
            self.ent_height.insert(0, self.data["height"])
            self.ent_top_margin.insert(0, self.data['top_margin'])
            self.ent_left_margin.insert(0, self.data['left_margin'])
        else:
            cli.info("Missing fields in configuration file.")
            self.parent.wipe_file('config.json')
            cli.info("Configuration file wiped.")

    def on_save(self):
        self.data["width"] = self.ent_width.get()
        self.data["height"] = self.ent_height.get()
        self.data['top_margin'] = self.ent_top_margin.get()
        self.data['left_margin'] = self.ent_left_margin.get()
        self.parent.save_settings(self.data)

    def on_close(self):
        self.destroy()


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
        ('PDF file', '*.pdf'),
        ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        ('BMP file', '*.bmp'),
        ('TIFF file', '*.tif'),
        ('PostScript file', '*.ps'),
        ('All files', '*.*')
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
            chart_as_bytecode = io.BytesIO(chart_encoded)
            Image.open(chart_as_bytecode).save(file_name)
            cli.info('Chart saved as: ' + file_name)
        else:
            cli.warning("Cannot write to that format.")


def get_name(placeholder):
    file = filedialog.askopenfile(initialdir="/desktop", title="Select file",
                                  filetypes=(("Excel files (*.xls*)", "*.xls*"),))
    if file:
        file_name = file.name.lower()
    else:
        file_name = placeholder
        cli.debug("File selection cancelled.")
    return file_name


cli = loggers.Stream()
