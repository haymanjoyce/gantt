# plan: tkinter, canvas , postscript, convert postscript to other formats
# ditching svg; canvas uses vectors; may not be as pretty but will do job
# add in ttk with clam style

from tkinter import Tk, Frame, Canvas, Label, Button, Entry, filedialog, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, PhotoImage, DISABLED, StringVar, Menu, Toplevel, RAISED
from tkinter.ttk import Style, Button

class Toolbar(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.btn_open = Button(self, text="Open", command=self.on_open)
        self.btn_save_as = Button(self, text="Save As", command=self.on_save_as)
        self.btn_settings = Button(self, text="Settings", command=self.on_settings)
        self.btn_refresh = Button(self, text="Refresh", command=self.on_refresh)

        self.btn_open.pack(side=LEFT, padx=(0, 2))
        self.btn_save_as.pack(side=LEFT, padx=(0, 2))
        self.btn_settings.pack(side=LEFT, padx=(0, 2))
        self.btn_refresh.pack(side=RIGHT)

    def on_open(self):
        user_file = filedialog.askopenfilename(initialdir="/desktop", title="Select file", filetypes=(("Excel files", "*.xls*"), ))
        print(user_file)

    def on_save_as(self):
        pass

    def on_settings(self):
        settings = Settings()
        config_file = open("config.txt", "r")
        config_data = config_file.readline()
        config_file.close()
        settings.ent_width.insert(0, config_data)

    def on_refresh(self):
        print("Refresh!")


class Chart(Canvas):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(bg="blue")

        line_a = self.create_line(20, 20, 20, 100, width=1)  # x1, y1, x2, y2
        line_b = self.create_line(20, 20, 80, 20, 80, 100, 140, 100)  # series of x, y points

        self.itemconfigure(line_b, fill="red", smooth=True)


class Settings(Toplevel):
    def __init__(self):
        super().__init__()

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


root = Tk()

print(f'W: {root.winfo_screenwidth()}px H: {root.winfo_screenheight()}px')
print(f'W: {root.winfo_screenmmwidth()}mm H: {root.winfo_screenmmheight()}mm')

root.geometry(f'{800}x{600}+{560}+{200}')  # w, h, x, y
root.minsize(800, 600)

root.title("www.gantt.page")
root.wm_iconbitmap("favicon.ico")

root.style = Style()
root.style.theme_use('clam')

toolbar = Toolbar(root)
toolbar.pack(side=TOP, fill=BOTH, padx=2, pady=(2, 0))

chart = Chart(root)
chart.pack(fill=BOTH, expand=True)

root.mainloop()

