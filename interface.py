#!/usr/bin/env python3

import datetime

from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, scrolledtext
from tkinter import NORMAL, DISABLED, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, ALL, WORD
from openpyxl import load_workbook
from tkcalendar import DateEntry

import loggers
import utils

from checking import Checker
from cleaning import Cleaner
from processing import Processor
from drawing import Drawer


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        self.win_x = int(self.winfo_screenwidth() * 0.1)
        self.win_y = int(self.winfo_screenheight() * 0.1)
        self.geometry(f'+{self.win_x}+{self.win_y}')  # w, h, x, y
        self.resizable(False, False)
        self.title("Gantt Page")
        self.wm_iconbitmap(utils.get_path("favicon.ico"))
        self.controls = Controls(self)
        self.mainloop()


class Controls(Frame):
    def __init__(self, parent):
        super(Controls, self).__init__(parent)

        self.self_configure()

        self.parent = parent
        self.chart = None
        self.file_source = None
        self.workbook_clean = None
        self.workbook_processed = None
        self.settings = utils.get_settings()
        self.v_cmd_1 = (self.register(self.field_validation_1), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.lbl_width = Label(self, text="Chart width:")
        self.lbl_height = Label(self, text="Chart height:")
        self.ent_width = Entry(self, relief="groove", validate="key", validatecommand=self.v_cmd_1)
        self.ent_height = Entry(self, relief="groove", validate="key", validatecommand=self.v_cmd_1)
        self.lbl_start = Label(self, text="Timescale start:")
        self.lbl_finish = Label(self, text="Timescale finish:")
        self.ent_start = DateEntry(self, date_pattern='yyyy/MM/dd', relief="groove")
        self.ent_finish = DateEntry(self, date_pattern='yyyy/MM/dd', relief="groove")
        self.lbl_source = Label(self, text="Source file:")
        self.lbl_filepath = Label(self, text="", anchor="w", relief="groove", bg="#fff")
        self.btn_select = Button(self, text="Select file", command=self.on_select, relief="groove")
        self.btn_run = Button(self, text="Run", command=self.on_run, relief="groove")
        self.scroller = scrolledtext.ScrolledText(self, width=45, height=10, wrap=WORD)  # defines window width
        self.btn_copy = Button(self, text="Copy to clipboard", command=self.on_copy, relief="groove")
        self.btn_image = Button(self, text="Save as image file", command=self.on_save, relief="groove")
        self.btn_export = Button(self, text="Export as Excel spreadsheet", command=self.on_export, relief="groove")
        self.btn_postscript = Button(self, text="Save as PostScript file", command=self.on_postscript, relief="groove")

        self.pack_widgets()
        self.bind_widgets()
        self.load_settings()
        self.set_button_states([1, 0, 0, 0, 0, 0])
        self.set_file_source("c:/users/hayma/desktop/gantt.xlsx")  # development only

    @staticmethod
    def field_validation_1(*args):
        if len(args[2]) > 5:
            return False
        elif args[2].isdigit():
            return True
        elif args[2] == "":
            return True
        else:
            return False

    def self_configure(self):
        self.pack()
        self.configure(padx=10, pady=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def pack_widgets(self):
        self.lbl_width.grid(row=0, column=0, sticky="w", pady=(0, 0))
        self.lbl_height.grid(row=0, column=1, sticky="w", pady=(0, 0))
        self.ent_width.grid(row=1, column=0, sticky="nsew", pady=(0, 5), padx=(0, 5))
        self.ent_height.grid(row=1, column=1, sticky="nsew", pady=(0, 5), padx=(5, 0))
        self.lbl_start.grid(row=2, column=0, sticky="w", pady=(0, 0))
        self.lbl_finish.grid(row=2, column=1, sticky="w", pady=(0, 0))
        self.ent_start.grid(row=3, column=0, sticky="nsew", pady=(0, 5), padx=(0, 5))
        self.ent_finish.grid(row=3, column=1, sticky="nsew", pady=(0, 5), padx=(5, 0))
        self.lbl_source.grid(row=4, column=0, columnspan=2, sticky="w")
        self.lbl_filepath.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(0, 5), ipady=2)
        self.btn_select.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_run.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.scroller.grid(row=8, column=0, columnspan=2, pady=(0, 5))
        self.btn_copy.grid(row=9, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_image.grid(row=10, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_export.grid(row=11, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
        self.btn_postscript.grid(row=12, column=0, columnspan=2, sticky="nsew", pady=(0, 0))  # pady 0 for last line

    def bind_widgets(self):
        self.ent_start.bind('<FocusIn>', self.check_finish)
        self.ent_finish.bind('<FocusIn>', self.check_start)

    def load_settings(self):
        if len(self.settings.keys()) == 4:
            self.insert_data()
        else:
            utils.wipe_settings()

    def insert_data(self):
        self.ent_width.insert(0, self.settings["width"])
        self.ent_height.insert(0, self.settings["height"])
        self.ent_start.set_date(self.settings["start"])
        self.ent_finish.set_date(self.settings["finish"])

    def extract_data(self):
        self.settings["width"] = self.ent_width.get()
        self.settings["height"] = self.ent_height.get()
        self.settings["start"] = self.ent_start.get_date().strftime('%Y/%m/%d')
        self.settings["finish"] = self.ent_finish.get_date().strftime('%Y/%m/%d')

    def check_finish(self, *args):
        start = self.ent_start.get_date()
        finish = self.ent_finish.get_date()
        if start > finish:
            cli.warning("Start greater than finish.")
        elif start == finish:
            cli.warning("Start is the same as finish.")

    def check_start(self, *args):
        start = self.ent_start.get_date()
        finish = self.ent_finish.get_date()
        if start > finish:
            cli.warning("Finish is less than start.")
        elif start == finish:
            cli.warning("Finish is the same as start.")

    def set_button_states(self, states=None):
        buttons = [self.btn_select, self.btn_run, self.btn_copy, self.btn_image, self.btn_export, self.btn_postscript]
        if not states:
            states = [1, 0, 0, 0, 0, 0]
        states = [NORMAL if x == 1 else DISABLED for x in states]
        for button, state in zip(buttons, states):
            button.config(state=state)

    def set_file_source(self, file_source=None):
        if file_source:
            self.file_source = file_source
            self.lbl_filepath.configure(text=file_source)
            self.set_button_states([1, 1, 0, 0, 0, 0])
        else:
            self.file_source = None
            self.lbl_filepath.configure(text="")
            self.set_button_states([1, 0, 0, 0, 0, 0])

    def on_select(self):
        self.file_source = utils.get_file_name(self.file_source)
        self.lbl_filepath.configure(text=self.file_source)

        button_states = [1, 1, 0, 0, 0, 0]
        self.set_button_states(button_states)

    def on_run(self):
        # update settings with data from Control
        self.extract_data()

        # save settings to config.json file
        utils.save_settings(self.settings)

        # wipe the scroller
        self.scroller.config(state=NORMAL)
        self.scroller.delete("0.0", END)
        self.scroller.config(state=DISABLED)

        # wipe the data.log file
        log_file = open(utils.get_path("data.log"), "r+")
        log_file.truncate(0)  # erase log file
        cli.info("Log file wiped.")

        # prep file
        workbook = load_workbook(self.file_source)
        workbook = Checker(workbook).run()
        self.workbook_clean = Cleaner(workbook).run()
        self.workbook_processed = Processor(self.workbook_clean).run()

        # populate scroller with data.log content
        with open(utils.get_path("data.log"), "r") as log_file:
            text = str(log_file.read())
        self.scroller.configure(state=NORMAL)  # writable
        self.scroller.insert(END, text)
        self.scroller.configure(state=DISABLED)  # readable
        cli.info("Log file updated.")

        # create chart
        if self.chart:
            self.chart.destroy()
        self.chart = Chart(self.parent, self.workbook_processed)  # App is the parent

        # set button permissions
        button_states = [1, 1, 1, 1, 1, 1]
        self.set_button_states(button_states)

    def on_copy(self):
        utils.copy_to_clipboard(self.chart.drawing)

    def on_save(self):
        utils.save_image(self.chart.drawing)

    def on_export(self):
        utils.export_data(self.workbook_clean)

    def on_postscript(self):
        utils.save_postscript(self.chart.drawing)


class Chart(Toplevel):
    def __init__(self, parent, workbook):
        super(Chart, self).__init__(parent)

        self.win_x = int(self.winfo_screenwidth() * 0.4)
        self.win_y = int(self.winfo_screenheight() * 0.1)
        self.geometry(f'+{self.win_x}+{self.win_y}')  # w, h, x, y
        self.resizable(False, False)
        self.title("Gantt Page")
        self.wm_iconbitmap(utils.get_path("favicon.ico"))
        self.parent = parent
        self.workbook = workbook
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.drawing = Drawer(self)  # Chart is the parent

    def on_close(self):
        button_states = [1, 1, 0, 0, 0, 0]
        self.parent.controls.set_button_states(button_states)
        self.destroy()


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))

