#!/usr/bin/env python3

import loggers
from tkinter import Tk, Frame, Label, Button, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT
from tkinter import DISABLED, Menu
from tkinter.ttk import Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import json
from math import floor
import dialogues
import chart


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        # DIMENSIONS

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

        # DECORATION

        self.title("Main")
        self.wm_iconbitmap("favicon.ico")

        # PERSISTENT COMPONENTS

        self.menubar = Menubar(self)
        self["menu"] = self.menubar
        # YES: self.config(menu=self.menubar)
        # YES: self.configure(menu=self.menubar)
        # NO: self.menu = self.menubar
        self.toolbar = Toolbar(self)
        self.viewer = Viewer(self)
        self.chart = chart.Chart(self)

        # LOOP

        self.mainloop()

        # CLEAN UP

        # erase log file
        log = open('app.log', 'r+')
        log.truncate(0)

    @staticmethod
    def get_settings():
        try:
            file = open("config.json", "r")
            data = file.readline()
            if data:
                return json.loads(data)
            else:
                return dict()
        except FileNotFoundError:
            cli.info("Configuration file not found.")
            file = open("config.json", "w")
            file.close()
            cli.info("Configuration file created.")
            return dict()

    @staticmethod
    def save_settings(data):
        with open('config.json', 'w') as file:
            file.write(json.dumps(data))

    @staticmethod
    def wipe_file(filename):
        with open(filename, 'w') as file:
            file.truncate(0)


class Menubar(Menu):
    def __init__(self, parent):
        super(Menubar, self).__init__(parent)

        self.parent = parent

        self.file_menu = Menu(self, tearoff=0)
        self.help_menu = Menu(self, tearoff=0)

        self.file_menu.add_command(label="Save As...", command=self.on_save)
        self.file_menu.add_command(label="Settings...", command=self.on_settings)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.on_exit)

        self.help_menu.add_command(label="View Log", command=self.on_log)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Help", command=self.on_help)
        self.help_menu.add_command(label="About", command=self.on_about)

        self.add_cascade(label="File", menu=self.file_menu)
        self.add_cascade(label="Help", menu=self.help_menu)

    def on_save(self):
        dialogues.save_image(self.parent.chart.postscript(), self.parent.get_settings())

    def on_settings(self):
        dialogues.Settings(self.parent)

    def on_exit(self):
        self.parent.quit()

    def on_log(self):
        dialogues.Log(self.parent)

    def on_help(self):
        print("Menu item working!")

    def on_about(self):
        print("Menu item working!")


class Toolbar(Frame):
    def __init__(self, parent):
        super(Toolbar, self).__init__(parent)

        self.parent = parent
        self.file_name = None

        self.pack(side=TOP, fill=BOTH, padx=2, pady=(2, 0))

        self.placeholder = "Select your Excel file"

        self.lbl_filename = Label(self, text=self.placeholder)
        self.btn_run = Button(self, text="Run", command=self.on_run, state=DISABLED)
        self.btn_select = Button(self, text="Select File", command=self.on_select)

        # order matters
        self.lbl_filename.pack(side=LEFT, fill=X)
        self.btn_run.pack(side=RIGHT, padx=(0, 0))
        self.btn_select.pack(side=RIGHT, padx=(0, 2))

    def on_select(self):
        self.file_name = dialogues.get_name(self.placeholder)
        self.lbl_filename.configure(text=self.file_name)
        self.btn_run.config(state="normal")

    def on_run(self):
        df = pd.read_excel(self.file_name)
        print(df)


class Viewer(Frame):
    def __init__(self, parent):
        super(Viewer, self).__init__(parent)

        self.parent = parent

        # frame = Frame(root, width=300, height=300)
        # frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
        # canvas = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))
        # hbar = Scrollbar(frame, orient=HORIZONTAL)
        # hbar.pack(side=BOTTOM, fill=X)
        # hbar.config(command=canvas.xview)
        # vbar = Scrollbar(frame, orient=VERTICAL)
        # vbar.pack(side=RIGHT, fill=Y)
        # vbar.config(command=canvas.yview)
        # canvas.config(width=300, height=300)
        # canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        # canvas.pack(side=LEFT, expand=True, fill=BOTH)


cli = loggers.Stream()
