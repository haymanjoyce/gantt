#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO set window sizes based on screen size
# TODO reading multiple tabs in pandas
# TODO stop log button creating more than one dialogue and put working into method
# TODO apply multiple window solution to settings
# TODO set geometry of Settings without killing grid
# TODO switch to internal padding

from tkinter import Tk, Frame, Canvas, Label, Button, Entry, filedialog, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, PhotoImage, DISABLED, StringVar, Menu, Toplevel, RAISED, scrolledtext, Text
from tkinter.ttk import Style, Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import os
import logging
import logging.config


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        print(f'Screen dimensions (pixels) - W:{self.winfo_screenwidth()} H:{self.winfo_screenheight()}')
        print(f'Screen dimensions (mm) - W:{self.winfo_screenmmwidth()} H:{self.winfo_screenmmheight()}')

        logging.info(f'Logging initialised.')

        self.geometry(f'{800}x{600}+{560}+{200}')  # w, h, x, y
        self.minsize(800, 600)
        self.title("Main")
        self.wm_iconbitmap("favicon.ico")

        self.filename = None

        self.toolbar = Toolbar(self)
        self.chart = Chart(self)
        self.settings = None
        self.log = None

        self.mainloop()


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
        settings = Settings(self.parent)
        with open("config.txt", "r") as file:
            data = file.readline()
        settings.ent_width.insert(0, data)

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
        self.btn_close = Button(self, text="Close")

        self.lbl_width.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.ent_width.grid(row=0, column=1, sticky="nsew", pady=(0, 5))
        self.lbl_height.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.ent_height.grid(row=1, column=1, sticky="nsew", pady=(0, 5))
        self.btn_save.grid(row=2, column=0, sticky="nsew", pady=(5, 0))
        self.btn_close.grid(row=2, column=1, sticky="nsew", pady=(5, 0))

        # you need to set geometry after grid established
        self.geometry(f'+{860}+{250}')  # w, h, x, y
        self.minsize(200, 100)

    def on_save(self):
        with open('config.txt', 'w') as config_file:
            config_data = self.ent_width.get()
            config_file.write(config_data)
        # and then make any changes to chart object


class Log(Toplevel):
    def __init__(self, parent):
        super(Log, self).__init__(parent)

        self.geometry(f'{500}x{500}+{710}+{250}')  # w, h, x, y
        self.minsize(200, 400)
        self.title("Log")
        self.wm_iconbitmap("favicon.ico")

        self.viewer = scrolledtext.ScrolledText(self)
        self.viewer.configure(state='disabled')
        self.viewer.pack(expand=True, fill=BOTH)

    def populate(self):
        with open('app.log', "r") as app_log:
            text = str(app_log.read())
        self.viewer.configure(state='normal')  # writable
        self.viewer.insert(END, text)
        self.viewer.configure(state='disabled')  # readable


if __name__ == '__main__':

    logging.basicConfig(filename='app.log', level=10, filemode='w', format='%(levelname)s - %(message)s')  # 10 is debug, 20 is info

    app = App()
