#!/usr/bin/env python3


import loggers
from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, Canvas, scrolledtext
from tkinter import NORMAL, DISABLED, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, ALL, WORD
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import utils  # beware importing * (imports logger too)
from io import BytesIO
from copy import copy
import win32clipboard as clipboard


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        self.x = int(self.winfo_screenwidth() * 0.1)
        self.y = int(self.winfo_screenheight() * 0.1)
        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y
        self.resizable(False, False)
        self.title("Gantt Page")
        self.wm_iconbitmap("favicon.ico")

        self.sourcefile = None
        self.settings = utils.get_settings()
        self.mainframe = Controls(self)
        self.preview = None

        self.mainloop()


class Controls(Frame):
    def __init__(self, parent):
        super(Controls, self).__init__(parent)

        self.pack()
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
        self.scroller = scrolledtext.ScrolledText(self, width=45, height=10, wrap=WORD, state=DISABLED)  # defines window width
        self.btn_copy = Button(self, text="Copy to clipboard", command=self.on_copy, state=DISABLED, relief="groove")
        self.btn_image = Button(self, text="Save as image file", command=self.on_save, state=NORMAL, relief="groove")
        self.btn_export = Button(self, text="Export as Excel spreadsheet", command=self.on_export, state=DISABLED, relief="groove")
        self.btn_postscript = Button(self, text="Save as PostScript file", command=self.on_postscript, state=NORMAL, relief="groove")

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
        self.scroller.grid(row=8, column=0, columnspan=2, pady=(0, 5))
        self.btn_copy.grid(row=9, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_image.grid(row=10, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_export.grid(row=11, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_postscript.grid(row=12, column=0, columnspan=2, sticky="nsew", pady=(0, 0))  # pady 0 for last line

        if len(self.parent.settings.keys()) == 4:
            self.insert_data()
        else:
            utils.wipe_settings()

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
        self.parent.sourcefile = utils.get_file_name(self.parent.sourcefile)
        self.lbl_filepath.configure(text=self.parent.sourcefile)
        self.btn_run.config(state=NORMAL)

    def on_run(self):
        self.extract_data()
        utils.save_settings(self.parent.settings)

        self.scroller.config(state=NORMAL)
        self.scroller.delete("0.0", END)
        self.scroller.config(state=DISABLED)

        log_file = open('process.log', 'r+')
        log_file.truncate(0)  # erase log file
        log.info("Logger initialised.")

        if self.parent.preview:
            self.parent.preview.destroy()
        self.parent.preview = Preview(self.parent)

        file = pd.ExcelFile(self.parent.sourcefile)
        sheet_0 = pd.read_excel(file, 0)
        sheet_1 = pd.read_excel(file, 1)
        print(sheet_1)

        with open('process.log', "r") as log_file:
            text = str(log_file.read())
        self.scroller.configure(state=NORMAL)  # writable
        self.scroller.insert(END, text)
        self.scroller.configure(state=DISABLED)  # readable

    def on_copy(self):
        pass
        # clipboard.OpenClipboard()
        # clipboard.EmptyClipboard()
        # clipboard.SetClipboardData(as_object, None)
        # clipboard.CloseClipboard()

    def on_save(self):
        utils.save_image(self.parent.preview.chart.postscript(), utils.get_settings())

    def on_export(self, df=pd.DataFrame()):
        data = pd.DataFrame([[1, 2], [1, 2]], columns=list('AB'))
        df = df.append(data)
        utils.export_data(df)

    def on_postscript(self):
        pass


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

        self.x = int(self.winfo_screenwidth() * 0.4)
        self.y = int(self.winfo_screenheight() * 0.1)
        self.geometry(f'+{self.x}+{self.y}')  # w, h, x, y
        self.resizable(False, False)
        self.title("Gantt Page")
        self.wm_iconbitmap("favicon.ico")

        self.parent = parent
        self.width = eval(self.parent.settings['width'])
        self.height = eval(self.parent.settings['height'])
        self.chart = Chart(self, self.width, self.height)
        self.chart.pack()


cli = loggers.Stream()
log = loggers.File()
