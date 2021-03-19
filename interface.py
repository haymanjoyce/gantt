#!/usr/bin/env python3

import logging
import datetime

from tkinter import Tk, Frame, Label, Button, Entry, Toplevel, scrolledtext
from tkinter import NORMAL, DISABLED, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, ALL, WORD, FIRST, LAST
from openpyxl import load_workbook
from tkcalendar import DateEntry

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
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.mainloop()

    def on_close(self):
        utils.wipe_log()
        try:
            self.quit()
        except RuntimeError:
            self.destroy()


class Controls(Frame):
    def __init__(self, parent):
        super(Controls, self).__init__(parent)

        self.pack()
        self.configure(padx=10, pady=5)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.parent = parent
        self.chart = None
        self.file_source = None
        self.workbook_clean = None
        self.workbook_processed = None
        self.settings = utils.get_settings()

        self.v_cmd_1 = (self.register(self.field_validation_1), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.v_cmd_2 = (self.register(self.field_validation_2), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.lbl_width = Label(self, text="Chart width:")
        self.lbl_height = Label(self, text="Chart height:")
        self.ent_width = Entry(self, relief="groove", validate="key", validatecommand=self.v_cmd_1)
        self.ent_height = Entry(self, relief="groove", validate="key", validatecommand=self.v_cmd_1)
        self.lbl_start = Label(self, text="Timescale start:")
        self.lbl_finish = Label(self, text="Timescale finish:")
        self.ent_start = DateEntry(self, date_pattern='yyyy/MM/dd', relief="groove")
        self.ent_finish = DateEntry(self, date_pattern='yyyy/MM/dd', relief="groove")
        self.lbl_source = Label(self, text="Source file:")
        self.ent_filepath = Entry(self, text="", relief="groove", validate="key", validatecommand=self.v_cmd_2)
        self.btn_select = Button(self, text="Select file", command=self.on_select, relief="groove")
        self.btn_run = Button(self, text="Run", command=self.on_run, relief="groove")
        self.scroller = scrolledtext.ScrolledText(self, width=45, height=10, wrap=WORD, state=DISABLED)  # defines window width
        self.btn_copy = Button(self, text="Copy to clipboard", command=self.on_copy, relief="groove")
        self.btn_image = Button(self, text="Save as image file", command=self.on_save, relief="groove")
        self.btn_export = Button(self, text="Export as Excel spreadsheet", command=self.on_export, relief="groove")
        self.btn_postscript = Button(self, text="Save as PostScript file", command=self.on_postscript, relief="groove")

        self.pack_widgets()
        self.bind_widgets()
        self.insert_field_data()
        self.wipe_scroller()
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

    @staticmethod
    def field_validation_2(*args):
        if args[2].isdigit():
            return False
        elif args[2] == "":
            return True
        else:
            return True

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
        self.ent_filepath.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(0, 5))
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

    def insert_field_data(self):
        self.ent_width.insert(0, self.settings.get("width", 800))
        self.ent_height.insert(0, self.settings.get("height", 600))
        self.ent_start.set_date(self.settings.get("start", datetime.date.today().strftime('%Y/%m/%d')))
        self.ent_finish.set_date(self.settings.get("finish", (datetime.date.today() + datetime.timedelta(days=10)).strftime('%Y/%m/%d')))

    def extract_field_data(self):
        self.settings["width"] = self.ent_width.get()
        self.settings["height"] = self.ent_height.get()
        self.settings["start"] = self.ent_start.get_date().strftime('%Y/%m/%d')
        self.settings["finish"] = self.ent_finish.get_date().strftime('%Y/%m/%d')

    def check_finish(self, *args):
        start = self.ent_start.get_date()
        finish = self.ent_finish.get_date()
        if start > finish:
            logging.warning("Start greater than finish.")
        elif start == finish:
            logging.warning("Start is the same as finish.")

    def check_start(self, *args):
        start = self.ent_start.get_date()
        finish = self.ent_finish.get_date()
        if start > finish:
            logging.warning("Finish is less than start.")
        elif start == finish:
            logging.warning("Finish is the same as start.")

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
            self.ent_filepath.delete(0, END)
            self.ent_filepath.insert(0, file_source)
            self.set_button_states([1, 1, 0, 0, 0, 0])
        else:
            self.file_source = None
            self.ent_filepath.delete(0, END)
            self.set_button_states([1, 0, 0, 0, 0, 0])

    def on_select(self):
        self.file_source = utils.get_file_name(self.file_source)
        self.set_file_source(self.file_source)

    def wipe_scroller(self):
        self.scroller.config(state=NORMAL)
        self.scroller.delete('1.0', END)  # from line '1' (entry equivalent is from char 0)
        self.scroller.config(state=DISABLED)

    def update_scroller(self):
        self.wipe_scroller()
        log = utils.get_log()
        self.scroller.configure(state=NORMAL)  # writable
        self.scroller.insert(END, log)
        self.scroller.configure(state=DISABLED)  # readable

    def prep_data(self):
        workbook = load_workbook(self.file_source)
        workbook = Checker(workbook).run()
        self.workbook_clean = Cleaner(workbook).run()
        self.workbook_processed = Processor(self.workbook_clean).run()

    def create_chart(self):
        if self.chart:
            self.chart.destroy()
        self.chart = Chart(self.parent, self.workbook_processed)  # App is the parent
        self.set_button_states([1, 1, 1, 1, 1, 1])

    def on_run(self):
        self.extract_field_data()
        utils.save_settings(self.settings)
        self.prep_data()
        self.create_chart()
        if not utils.get_log():
            logging.info("No errors detected.")
        self.update_scroller()

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
        self.parent.controls.set_button_states([1, 1, 0, 0, 0, 0])
        self.destroy()

