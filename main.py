# plan: tkinter, canvas , postscript, convert postscript to other formats
# ditching svg; canvas uses vectors; may not be as pretty but will do job
# add in ttk with clam style

from tkinter import Tk, Frame, Canvas, Label, Button, Entry, filedialog, END, BOTH, X, Y, TOP, BOTTOM, LEFT, RIGHT, PhotoImage
from tkinter.ttk import Style, Frame, Label, Button, Entry


class Settings(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbl_width = Label(self, text="Page width:")
        self.ent_width = Entry(self, width=10)
        self.lbl_height = Label(self, text="Page height:")
        self.ent_height = Entry(self, width=10)

        self.lbl_width.grid(row=0, column=0, sticky="nsew", pady=(0, 2))
        self.ent_width.grid(row=0, column=1, sticky="nsew", pady=(0, 2))
        self.lbl_height.grid(row=1, column=0, sticky="nsew")
        self.ent_height.grid(row=1, column=1, sticky="nsew")


class Chart(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = Canvas(self, bg="grey")
        self.canvas.pack(fill=BOTH, expand=True)

        line_a = self.canvas.create_line(20, 20, 20, 100, width=1)  # x1, y1, x2, y2
        line_b = self.canvas.create_line(20, 20, 80, 20, 80, 100, 140, 100)  # series of x, y points

        self.canvas.itemconfigure(line_b, fill="red", smooth=True)


class TopFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.ent_filename = Entry(self)
        self.btn_select = Button(self, text="Select")
        self.btn_run = Button(self, text="Run")

        self.ent_filename.pack(expand=1, side=LEFT, fill=BOTH, padx=(0, 2))
        self.btn_select.pack(side=LEFT, padx=(0, 2))
        self.btn_run.pack(side=LEFT)


class MiddleFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.settings = Settings(self)
        self.chart = Chart(self)

        self.settings.configure(style="Blue.TFrame")
        self.chart.configure(style="Yellow.TFrame")

        self.settings.pack(side=LEFT, fill=Y, padx=2, pady=2)
        self.chart.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 2), pady=2)


class BottomFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.ent_filename = Entry(self)
        self.btn_select = Button(self, text="Select")
        self.btn_export = Button(self, text="Export")

        self.ent_filename.pack(expand=1, side=LEFT, fill=BOTH, padx=(0, 2))
        self.btn_select.pack(side=LEFT, padx=(0, 2))
        self.btn_export.pack(side=LEFT)


class MainFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.top_frame = TopFrame(self)
        self.middle_frame = MiddleFrame(self)
        self.bottom_frame = BottomFrame(self)

        self.configure(style="Red.TFrame")
        self.top_frame.configure(style="Green.TFrame")
        self.middle_frame.configure(style="Red.TFrame")
        self.bottom_frame.configure(style="Green.TFrame")

        self.pack(fill=BOTH, expand=True)
        self.top_frame.pack(side=TOP, fill=X, padx=2, pady=(2, 0))
        self.middle_frame.pack(fill=BOTH, expand=True)
        self.bottom_frame.pack(side=BOTTOM, fill=X, padx=2, pady=(0, 2))

    def greet(self):
        print("Greetings!")


root = Tk()
print(f'W: {root.winfo_screenwidth()}px H: {root.winfo_screenheight()}px')
print(f'W: {root.winfo_screenmmwidth()}mm H: {root.winfo_screenmmheight()}mm')
root.geometry(f'{800}x{600}+{560}+{200}')  # w, h, x, y
root.minsize(800, 600)
root.title("www.gantt.page")
root.iconbitmap(default="favicon.ico")
# root.iconphoto(False, PhotoImage(file="favicon.ico"))
root.style = Style()
root.style.theme_use('clam')
print(f'Theme: {root.style.theme_use()}')
root.style.configure("Blue.TFrame", background="blue")
root.style.configure("Red.TFrame", background="red")
root.style.configure("Green.TFrame", background="green")
root.style.configure("Yellow.TFrame", background="yellow")
app = MainFrame(root)
root.mainloop()



# def select_file():
#     root.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select file",
#                                                filetypes=(("text files", "*.txt"), ("all files", "*.*")))
#     ent_source_file.insert(END, root.filename)
#
#     if len(ent_source_file.get()) != 0:
#         btn_import.config(state="normal")
#
#
# def update_canvas():
#     pass


