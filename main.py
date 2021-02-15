#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO copying to clipboard
# TODO setting image dimensions and printing
# TODO freezing the app and loading along with GhostScript
# TODO reading multiple tabs in pandas
# TODO convert canvas data to Excel
# TODO scrollbars if canvas larger than window

from tkinter import Tk, Frame, Canvas, Label, Button, Entry, filedialog, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT
from tkinter import PhotoImage, DISABLED, StringVar, Menu, Toplevel, RAISED, scrolledtext, Text
from tkinter.ttk import Style, Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import os
import json
import test
import loggers
from math import floor
from PIL import Image
import io
import data


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
        self.chart = Chart(self)

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
        gui.info("Settings saved.")

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
        Output(self.parent)

    def on_settings(self):
        Settings(self.parent)

    def on_exit(self):
        self.parent.quit()

    def on_log(self):
        Log(self.parent)

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
        self.file_name = Input(self.parent).file_name
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


class Chart(Canvas):
    def __init__(self, parent):
        super(Chart, self).__init__(parent)

        self.parent = parent
        self.settings = parent.get_settings()

        self.configure(bg="#dddddd")
        self.pack(fill=BOTH, expand=True)

        self.create_rectangle(0, 0, 1600, 1600, fill="#ff0000")
        self.create_rectangle(0, 0, 800, 800, fill="#0000ff")
        self.create_rectangle(0, 0, 400, 400, fill="#00ff00")
        self.create_rectangle(0, 2, 200, 200, fill="#ff0000", outline="#000")


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


class Input:
    def __init__(self, parent):

        self.parent = parent
        self.placeholder = self.parent.toolbar.placeholder

        self.file = filedialog.askopenfile(initialdir="/desktop", title="Select file",
                                           filetypes=(("Excel files (*.xls*)", "*.xls*"),))

        if self.file:
            self.file_name = self.file.name.lower()
        else:
            self.file_name = self.placeholder
            cli.debug("File selection cancelled.")

    def as_dataframe(self):
        return pd.read_excel(self.file_name)


class Output:
    """
    Handles export of chart to various formats.
    Image files, including PDF, need Ghostscript installed on client machine.
    as_postscript method is there to show the odd things you need to do to make it work in landscape.
    File class is not derived from tkinter.
    """

    def __init__(self, parent):

        self.parent = parent
        self.chart = self.parent.chart
        self.settings = self.parent.get_settings()

        file_types = [
            ('PDF file', '*.pdf'),
            ('JPG file', '*.jpg'),
            ('PNG file', '*.png'),
            ('BMP file', '*.bmp'),
            ('TIFF file', '*.tif'),
            ('Excel file', '*.xlsx'),
            ('All files', '*.*')
        ]

        self.file = filedialog.asksaveasfile(mode="w",
                                             title="Save As",
                                             filetypes=file_types,
                                             defaultextension="*.*"
                                             )

        if self.file:
            self.file_name = self.file.name.lower()
            self.save_file()

    def save_file(self):
        if self.file_name.endswith(('.pdf', '.jpg', '.png', '.bmp', '.tif')):
            self.as_image()
        elif self.file_name.endswith('.xlsx'):
            self.as_excel()
        else:
            cli.info("Cannot write to that format yet.")

    def as_postscript(self):
        page_x = self.settings['top_margin']
        page_y = self.settings['left_margin']
        chart = self.chart.postscript(rotate=1,
                                      pageanchor='nw',
                                      pagex=page_x,
                                      pagey=page_y)
        self.file.write(chart)
        self.file.close()
        cli.info("Chart saved as postscript file.")

    def as_image(self):
        chart_as_ps = self.chart.postscript()
        chart_encoded = chart_as_ps.encode('utf-8')
        chart_as_bytecode = io.BytesIO(chart_encoded)
        Image.open(chart_as_bytecode).save(self.file_name.lower())
        cli.info('Chart saved as: ' + self.file_name.lower())

    def as_excel(self):
        pass


if __name__ == '__main__':
    cli = loggers.Stream()
    gui = loggers.File()

    cli.info(f"Loggers initialised. "
             f"Example usage: 'cli.debug('Message for developer.')' or 'gui.info('Message for user.')'")

    app = App()
