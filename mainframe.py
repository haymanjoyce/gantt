#!/usr/bin/env python3

import loggers
from tkinter import Tk, Frame, Label, Button, Entry, Menu, Toplevel
from tkinter import NORMAL, DISABLED, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT
# from tkinter.ttk import Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
from math import floor
import dialogues
import chart
from settings import *
# import win32clipboard as clipboard
from io import BytesIO
from PIL import Image
from copy import copy


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

        self.panel = Panel(self)

        self.mainloop()
        log = open('app.log', 'r+')
        log.truncate(0)  # erase log file


class Panel(Frame):
    def __init__(self, parent):
        super(Panel, self).__init__(parent)

        self.pack(fill=BOTH, expand=True)
        self.configure(padx=10, pady=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.parent = parent
        self.source = None
        self.preview = None
        self.log = None

        self.lbl_width = Label(self, text="Chart width:")
        self.lbl_height = Label(self, text="Chart height:")
        self.ent_width = Entry(self, relief="groove")
        self.ent_height = Entry(self, relief="groove")
        self.lbl_start = Label(self, text="Timescale start:")
        self.lbl_finish = Label(self, text="Timescale finish:")
        self.ent_start = Entry(self, relief="groove")
        self.ent_finish = Entry(self, relief="groove")

        self.lbl_source = Label(self, text="Source file:")
        self.lbl_filepath = Label(self, text=self.source, relief="groove", bg="#fff", anchor="w")
        self.btn_select = Button(self, text="Select file", command=self.on_select, state=NORMAL, relief="groove")
        self.btn_run = Button(self, text="Run", command=self.on_run, state=DISABLED, relief="groove")
        self.btn_copy = Button(self, text="Copy to clipboard", command=self.on_copy, state=DISABLED, relief="groove")
        self.btn_image = Button(self, text="Save as image file", command=self.on_save, state=DISABLED, relief="groove")
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

    def on_select(self):
        self.source = dialogues.get_file_name(self.source)
        self.lbl_filepath.configure(text=self.source)
        self.btn_run.config(state=NORMAL)

    def on_run(self):
        if self.preview:
            self.preview.destroy()
        self.preview = dialogues.Preview(self.parent)

        if self.log:
            self.log.destroy()
        self.log = dialogues.Log(self.parent)

        file = pd.ExcelFile(self.source)
        sheet_0 = pd.read_excel(file, 0)
        sheet_1 = pd.read_excel(file, 1)
        print(sheet_1)

    def on_save(self):
        dialogues.save_image(dialogues.Preview(self.parent).canvas.postscript(), get_settings())

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


cli = loggers.Stream()
