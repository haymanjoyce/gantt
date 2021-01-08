#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO reading multiple tabs in panda
# TODO set window sizes based on screen size
# TODO add normal app menu so only select file and run showing at top

from tkinter import Tk, Frame, Canvas, Label, Button, Entry, filedialog, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, PhotoImage, DISABLED, StringVar, Menu, Toplevel, RAISED, scrolledtext, Text
from tkinter.ttk import Style, Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import os
import json
import test
import loggers
from math import floor


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        cli.info(f'Screen dimensions (pixels) - W:{self.winfo_screenwidth()} H:{self.winfo_screenheight()}')
        cli.info(f'Screen dimensions (mm) - W:{self.winfo_screenmmwidth()} H:{self.winfo_screenmmheight()}')

        self.width = floor(0.7 * self.winfo_screenwidth())
        self.height = floor(0.7 * self.winfo_screenheight())

        if self.height < 600 or self.width < 800:
            self.width = 800
            self.height = 600

        self.minsize(400, 300)

        self.x = floor((self.winfo_screenwidth() - self.width) * 0.5)
        self.y = floor((self.winfo_screenheight() - self.height) * 0.5)

        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')  # w, h, x, y

        self.title("Main")
        self.wm_iconbitmap("favicon.ico")

        self.filename = None

        self.toolbar = Toolbar(self)
        self.chart = Chart(self)
        self.settings = None
        self.log = None

        self.mainloop()

        # erase log file
        log = open('app.log', 'r+')
        log.truncate(0)


class Toolbar(Frame):
    def __init__(self, parent):
        super(Toolbar, self).__init__(parent)

        self.parent = parent

        self.pack(side=TOP, fill=BOTH, padx=2, pady=(2, 0))

        self.lbl_filename = Label(self, text="Select your Excel file")
        self.btn_log = Button(self, text="View Log", command=self.on_log)
        self.btn_settings = Button(self, text="Settings", command=self.on_settings)
        self.btn_save = Button(self, text="Save As", command=self.on_save, state=DISABLED)
        self.btn_run = Button(self, text="Run", command=self.on_run, state=DISABLED)
        self.btn_select = Button(self, text="Select File", command=self.on_select)

        # order matters
        self.lbl_filename.pack(side=LEFT, fill=X)
        self.btn_log.pack(side=RIGHT, padx=(0, 0))
        self.btn_settings.pack(side=RIGHT, padx=(0, 2))
        self.btn_save.pack(side=RIGHT, padx=(0, 2))
        self.btn_run.pack(side=RIGHT, padx=(0, 2))
        self.btn_select.pack(side=RIGHT, padx=(0, 2))

    def on_select(self):
        # we store filename at root level because it's needed by other classes
        self.parent.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select file", filetypes=(("Excel files (*.xls*)", "*.xls*"), ))

        self.lbl_filename.configure(text=self.parent.filename)

        if len(self.lbl_filename.cget("text")) != 0:
            self.btn_run.config(state="normal")
            self.btn_save.config(state="normal")

    def on_run(self):
        df = pd.read_excel(self.parent.filename)
        print(df)
        # then check it - logging issues - another toplevel
        # then interpret it - adding to df
        # then parse it
        # then render it - chart.create_line(200, 20, 200, 100, width=1)  # x1, y1, x2, y2
        self.parent.chart.itemconfigure(app.chart.line_a, width=4)
        self.parent.chart.create_line(90, 20, 90, 100, width=2)  # x1, y1, x2, y2

    def on_save(self):
        pass

    def on_settings(self):
        # kill any old instances if this class
        if isinstance(self.parent.settings, Settings):
            self.parent.settings.destroy()
        self.parent.settings = Settings(self.parent)
        self.parent.settings.populate()

    def on_log(self):
        # kill any old instances if this class
        if isinstance(self.parent.log, Log):
            self.parent.log.destroy()
        self.parent.log = Log(self.parent)
        self.parent.log.populate()


class Chart(Canvas):
    def __init__(self, parent):
        super(Chart, self).__init__(parent)

        self.configure(bg="#dddddd")
        self.pack(fill=BOTH, expand=True)

        self.line_a = self.create_line(20, 20, 20, 100, width=1)  # x1, y1, x2, y2
        line_b = self.create_line(20, 20, 80, 20, 80, 100, 140, 100)  # series of x, y points

        self.itemconfigure(line_b, fill="red", smooth=True)


class Settings(Toplevel):
    def __init__(self, parent):
        super(Settings, self).__init__(parent)

        self.parent = parent

        self.width = 200
        self.height = 100
        self.minsize(200, 100)
        self.x = floor(self.parent.x + ((self.parent.width * 0.5) - 100))
        self.y = floor(self.parent.y + (self.parent.height * 0.2))

        self.dict_settings = dict()
        self.json_settings = None

        self.title("Settings")
        self.wm_iconbitmap("favicon.ico")
        self.configure(padx=10, pady=10)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.lbl_width = Label(self, text="Page width:")
        self.ent_width = Entry(self, width=10)
        self.lbl_height = Label(self, text="Page height:")
        self.ent_height = Entry(self, width=10)
        self.btn_save = Button(self, text="Save", command=self.on_save)
        self.btn_close = Button(self, text="Close", command=self.on_close)

        self.lbl_width.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.ent_width.grid(row=0, column=1, sticky="nsew", pady=(0, 5))
        self.lbl_height.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.ent_height.grid(row=1, column=1, sticky="nsew", pady=(0, 5))
        self.btn_save.grid(row=2, column=0, sticky="nsew", pady=(5, 0))
        self.btn_close.grid(row=2, column=1, sticky="nsew", pady=(5, 0))

        # you need to set geometry after grid established (for some reason)
        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')  # w, h, x, y

    def populate(self):
        # opening file
        try:
            with open("config.json", "r") as file:
                self.json_settings = file.readline()
        except FileNotFoundError:
            cli.info("Configuration file not found.")
            with open("config.json", "w") as file:
                cli.info("Configuration file created.")
                # you could load file with default content here

        # if file contains data
        if self.json_settings:
            self.dict_settings = json.loads(self.json_settings)
            # populate fields
            self.ent_width.insert(0, self.dict_settings["width"])
            self.ent_height.insert(0, self.dict_settings["height"])
        else:
            cli.info("Blank configuration file.")

    def on_save(self):
        # get settings
        self.dict_settings["width"] = self.ent_width.get()
        self.dict_settings["height"] = self.ent_height.get()

        # save settings
        self.json_settings = json.dumps(self.dict_settings)
        with open('config.json', 'w') as file:
            file.write(self.json_settings)
        gui.info("Settings saved.")

        # make changes to chart object (if any)

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

    def populate(self):
        with open('app.log', "r") as log:
            text = str(log.read())
        self.scroller.configure(state='normal')  # writable
        self.scroller.insert(END, text)
        self.scroller.configure(state='disabled')  # readable


if __name__ == '__main__':

    cli = loggers.Stream()
    cli.info(f"Logger initialised in main module.")

    gui = loggers.File()
    gui.info("Logger initialised.")

    app = App()
