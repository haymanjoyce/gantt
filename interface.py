#!/usr/bin/env python3

from tkinter import Tk, Frame, Label, Button, Entry, Menu, Toplevel, Canvas
from tkinter import NORMAL, DISABLED, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, ALL
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import dialogues
from utils import *
from math import floor
from io import BytesIO
from copy import copy
import win32clipboard as clipboard


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        self.width = 300
        self.height = 400
        self.x = int((self.winfo_screenwidth() * 0.5) - (self.width * 0.5))
        self.y = int((self.winfo_screenheight() * 0.2))
        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')  # w, h, x, y
        self.resizable(False, False)
        self.title("Gantt Page")
        self.wm_iconbitmap("favicon.ico")

        self.sourcefile = None
        self.settings = get_settings()
        self.mainframe = Controls(self)
        self.preview = None
        self.log = None

        self.mainloop()
        log = open('app.log', 'r+')
        log.truncate(0)  # erase log fill


class Controls(Frame):
    def __init__(self, parent):
        super(Controls, self).__init__(parent)

        self.pack(fill=BOTH, expand=True)
        self.configure(padx=10, pady=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.parent = parent

        self.lbl_width = Label(self, text="Chart width:")
        self.lbl_height = Label(self, text="Chart height:")
        self.ent_width = Entry(self, relief="groove")
        self.ent_height = Entry(self, relief="groove")
        self.lbl_start = Label(self, text="Timescale start:")
        self.lbl_finish = Label(self, text="Timescale finish:")
        self.ent_start = Entry(self, relief="groove")
        self.ent_finish = Entry(self, relief="groove")

        self.lbl_source = Label(self, text="Source file:")
        self.lbl_filepath = Label(self, text=self.parent.sourcefile, relief="groove", bg="#fff", anchor="w")
        self.btn_select = Button(self, text="Select file", command=self.on_select, state=NORMAL, relief="groove")
        self.btn_run = Button(self, text="Run", command=self.on_run, state=DISABLED, relief="groove")
        self.btn_copy = Button(self, text="Copy to clipboard", command=self.on_copy, state=DISABLED, relief="groove")
        self.btn_image = Button(self, text="Save as image file", command=self.on_save, state=NORMAL, relief="groove")
        self.btn_export = Button(self, text="Export as Excel spreadsheet", command=self.on_export, state=DISABLED, relief="groove")

        self.lbl_width.grid(row=0, column=0, sticky="w", pady=(0, 0))
        self.lbl_height.grid(row=0, column=1, sticky="w", pady=(0, 0))
        self.ent_width.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(0, 5))
        self.ent_height.grid(row=1, column=1, sticky="nsew", pady=(0, 5), padx=(5, 0))
        self.lbl_start.grid(row=2, column=0, sticky="w", pady=(0, 0))
        self.lbl_finish.grid(row=2, column=1, sticky="w", pady=(0, 0))
        self.ent_start.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(0, 5))
        self.ent_finish.grid(row=3, column=1, sticky="nsew", pady=(0, 5), padx=(5, 0))

        self.lbl_source.grid(row=4, column=0, columnspan=2, sticky="w")
        self.lbl_filepath.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(0, 5), ipady=5)
        self.btn_select.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_run.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_copy.grid(row=8, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_image.grid(row=9, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_export.grid(row=10, column=0, columnspan=2, sticky="nsew", pady=(0, 5))

        if len(self.parent.settings.keys()) == 4:
            self.insert_data()
        else:
            wipe_settings()

    def insert_data(self):
        self.ent_width.insert(0, self.parent.settings["width"])
        self.ent_height.insert(0, self.parent.settings["height"])
        self.ent_start.insert(0, self.parent.settings["start"])
        self.ent_finish.insert(0, self.parent.settings["finish"])

    def extract_data(self):
        self.parent.settings["width"] = self.ent_width.get()
        self.parent.settings["height"] = self.ent_height.get()
        self.parent.settings["start"] = self.ent_start.get()
        self.parent.settings["finish"] = self.ent_finish.get()

    def on_select(self):
        self.parent.sourcefile = dialogues.get_file_name(self.parent.sourcefile)
        self.lbl_filepath.configure(text=self.parent.sourcefile)
        self.btn_run.config(state=NORMAL)

    def on_run(self):
        self.extract_data()
        save_settings(self.parent.settings)

        if self.parent.preview:
            self.parent.preview.destroy()
        self.parent.preview = Preview(self.parent)

        if self.parent.log:
            self.parent.log.destroy()
        self.parent.log = dialogues.Log(self.parent)

        file = pd.ExcelFile(self.parent.sourcefile)
        sheet_0 = pd.read_excel(file, 0)
        sheet_1 = pd.read_excel(file, 1)
        print(sheet_1)

    def on_save(self):
        dialogues.save_image(self.parent.preview.chart.postscript(), get_settings())

    def on_export(self, df=pd.DataFrame()):
        data = pd.DataFrame([[1, 2], [1, 2]], columns=list('AB'))
        df = df.append(data)
        dialogues.export_data(df)

    def on_copy(self):
        pass
        # clipboard.OpenClipboard()
        # clipboard.EmptyClipboard()
        # clipboard.SetClipboardData(as_object, None)
        # clipboard.CloseClipboard()


class Chart(Canvas):
    def __init__(self, parent, width, height):
        super(Chart, self).__init__(parent)

        self.parent = parent
        self.config(width=width, height=height)
        self.draw(0, 0, width, height)

    def draw(self, x=0, y=0, width=100, height=100):
        self.create_rectangle(x, y, width, height, fill="#ff0000")
        self.create_rectangle(x, y, width // 2, height // 2, fill="#0000ff")
        self.create_rectangle(x, y, width // 3, height // 3, fill="#00ff00")
        self.create_rectangle(x, y, width // 4, height // 4, fill="#ff0000", outline="#000")

    def to_bytecode(self):
        to_postscript = self.postscript()
        to_utf8 = to_postscript.encode('utf-8')
        return BytesIO(to_utf8)


class Preview(Toplevel):
    def __init__(self, parent):
        super(Preview, self).__init__(parent)

        self.parent = parent
        self.width = eval(self.parent.settings['width'])
        self.height = eval(self.parent.settings['height'])
        self.x = floor(((self.winfo_screenwidth() // 2) - self.width // 2))
        self.y = floor(((self.winfo_screenheight() // 2) - self.height // 2))
        self.chart = Chart(self, self.width, self.height)
        self.chart.pack()

        self.title("Test")
        self.wm_iconbitmap("favicon.ico")
        self.resizable(False, False)
        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y


cli = loggers.Stream()