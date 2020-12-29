# plan: tkinter, canvas , postscript, convert postscript to other formats
# TODO sketch out on_run and on_save
# TODO explore dynamically creating and amending objects

from tkinter import Tk, Frame, Canvas, Label, Button, Entry, filedialog, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, PhotoImage, DISABLED, StringVar, Menu, Toplevel, RAISED
from tkinter.ttk import Style, Button
import pandas as pd  # requires manual install of openpyxl (xlrd only does xls)
import os


class Toolbar(Frame):
    def __init__(self, parent):
        super(Toolbar, self).__init__(parent)

        self.btn_select = Button(self, text="Select...", command=self.on_select)
        self.btn_save = Button(self, text="Save...", command=self.on_save, state=DISABLED)
        self.btn_settings = Button(self, text="Settings...", command=self.on_settings)
        self.btn_run = Button(self, text="Run...", command=self.on_run, state=DISABLED)
        self.lbl_filename = Label(self, text="Select Excel file")

        self.lbl_filename.pack(side=LEFT, fill=X)

        self.btn_settings.pack(side=RIGHT, padx=(0, 0))
        self.btn_save.pack(side=RIGHT, padx=(0, 2))
        self.btn_run.pack(side=RIGHT, padx=(0, 2))
        self.btn_select.pack(side=RIGHT, padx=(0, 2))

    def on_select(self):
        # we store filename with root because it's needed by other classes
        root.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select file", filetypes=(("Excel files (*.xls*)", "*.xls*"), ))

        self.lbl_filename.configure(text=root.filename)

        if len(self.lbl_filename.cget("text")) != 0:
            self.btn_run.config(state="normal")
            self.btn_save.config(state="normal")

    def on_run(self):
        df = pd.read_excel(root.filename)
        print(df)
        # then check it - logging issues - another toplevel
        # then interpret it - adding to df
        # then parse it
        # then render it - chart.create_line(200, 20, 200, 100, width=1)  # x1, y1, x2, y2
        chart.itemconfigure(chart.line_a, width=4)

    def on_save(self):
        pass

    def on_settings(self):

        settings = Settings()

        with open("config.txt", "r") as file:
            data = file.readline()

        settings.ent_width.insert(0, data)


class Chart(Canvas):
    def __init__(self, parent):
        super(Chart, self).__init__(parent)

        self.configure(bg="#dddddd")

        self.line_a = self.create_line(20, 20, 20, 100, width=1)  # x1, y1, x2, y2
        line_b = self.create_line(20, 20, 80, 20, 80, 100, 140, 100)  # series of x, y points

        self.itemconfigure(line_b, fill="red", smooth=True)


class Settings(Toplevel):
    def __init__(self):
        super(Settings, self).__init__()

        self.lbl_width = Label(self, text="Page width:")
        self.ent_width = Entry(self, width=10)
        self.lbl_height = Label(self, text="Page height:")
        self.ent_height = Entry(self, width=10)
        self.btn_save = Button(self, text="Save", command=self.on_save)
        self.btn_close = Button(self, text="Close")

        self.configure(padx=10, pady=10)
        self.lbl_width.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
        self.ent_width.grid(row=0, column=1, sticky="nsew", pady=(0, 5))
        self.lbl_height.grid(row=1, column=0, sticky="nsew", pady=(0, 5))
        self.ent_height.grid(row=1, column=1, sticky="nsew", pady=(0, 5))
        self.btn_save.grid(row=2, column=0, sticky="nsew", pady=(5, 0))
        self.btn_close.grid(row=2, column=1, sticky="nsew", pady=(5, 0))

    def on_save(self):
        print("Save stuff")
        config_file = open("config.txt", "w")
        config_data = self.ent_width.get()
        config_file.write(config_data)
        config_file.close()
        # and make any changes to chart object


class Log(Toplevel):
    def __init__(self, parent):
        super(Log, self).__init__(parent)


root = Tk()

print(f'W: {root.winfo_screenwidth()}px H: {root.winfo_screenheight()}px')
print(f'W: {root.winfo_screenmmwidth()}mm H: {root.winfo_screenmmheight()}mm')

root.geometry(f'{800}x{600}+{560}+{200}')  # w, h, x, y
root.minsize(800, 600)

root.title("www.gantt.page")
root.wm_iconbitmap("favicon.ico")

root.filename = None

toolbar = Toolbar(root)
toolbar.pack(side=TOP, fill=BOTH, padx=2, pady=(2, 0))

chart = Chart(root)
chart.pack(fill=BOTH, expand=True)

root.mainloop()

