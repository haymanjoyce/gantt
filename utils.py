#!/usr/bin/env python3

import loggers
import json
from tkinter import filedialog
from PIL import Image
from io import BytesIO, StringIO
import win32clipboard as clipboard
import os


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


def save_settings(data):
    with open('config.json', 'w') as file:
        file.write(json.dumps(data))


def wipe_settings():
    with open('config.json', 'w') as file:
        file.truncate(0)


def save_image(chart):
    """Handles export of chart to various formats.  Requires Ghostscript on client machine."""
    file_types = [
        ('All files', '*.*'),
        ('PDF file', '*.pdf'),
        ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        ('BMP file', '*.bmp'),
        ('TIFF file', '*.tif'),
    ]
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=file_types,
                                    defaultextension="*.*"
                                    )
    if file:
        file_name = file.name.lower()
        if file_name.endswith(('.pdf', '.jpg', '.png', '.bmp', '.tif')):
            chart_as_postscript = chart.postscript()
            chart_encoded = chart_as_postscript.encode('utf-8')
            chart_as_bytecode = BytesIO(chart_encoded)
            Image.open(chart_as_bytecode).save(file_name)
            cli.info('Chart saved as: ' + file_name)
        else:
            cli.warning("File type not recognised.")
    else:
        cli.info("Operation cancelled.")


def get_file_name(placeholder):
    file = filedialog.askopenfile(initialdir="/desktop", title="Select file",
                                  filetypes=(("Excel files", "*.xlsx"),))
    if file:
        file_name = file.name.lower()
    else:
        file_name = placeholder
        cli.debug("Operation cancelled.")
    return file_name


def export_data(df):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=(("Excel files", "*.xlsx"),),
                                    )
    if file:
        file_name = file.name.lower()
        if file_name.endswith(".xlsx"):
            df.to_excel(file_name)
            cli.info("Chart saved as" + file_name)
        else:
            cli.warning("File type not recognised.")
    else:
        cli.warning("Operation cancelled.")


def save_postscript(chart):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=[('PostScript file', '*.ps'), ],
                                    defaultextension="*.ps")
    chart.postscript(file=file.name, rotate=1)


def copy_to_clipboard(chart):
    chart_as_postscript = chart.postscript()
    chart_encoded = chart_as_postscript.encode('utf-8')

    # saved as bytecode / string
    chart_as_bytecode = BytesIO(chart_encoded)

    # saves to bmp/tiff file ok
    Image.open(chart_as_bytecode).save("temp.tiff")

    # saves to bmp/tiff in bytes ok
    chart_as_bitmap_bytecode = BytesIO()
    Image.open(chart_as_bytecode).save(chart_as_bitmap_bytecode, "BMP")
    # Image.open(chart_as_bitmap_bytecode).save("temp2.TIFF")
    # print(type(chart_as_bitmap_bytecode.read()))

    # try pointing to file with absolute path
    path_to_file = os.path.abspath("temp2.TIFF")

    # works with text
    # result = 'Some Text'
    # clipboard.OpenClipboard()
    # clipboard.EmptyClipboard()
    # clipboard.SetClipboardText(result, clipboard.CF_TEXT)
    # clipboard.CloseClipboard()

    # these constants are just integers; first argument must be one of these
    print(clipboard.CF_BITMAP)

    # try it with StringIO as per docs...
    chart_as_string_object = StringIO(chart_as_postscript)
    # Image.open(chart_as_string_object).save("temp.png")  # does not work

    # clipboard.OpenClipboard()
    # clipboard.EmptyClipboard()
    # clipboard.SetClipboardData(chart_as_bitmap_bytecode.read(), clipboard.CF_BITMAP)
    # clipboard.CloseClipboard()

    chart_as_bytecode.close()
    chart_as_bitmap_bytecode.close()
    chart_as_string_object.close()


cli = loggers.Stream()
