#!/usr/bin/env python3

import logging
import json
from tkinter import filedialog
from PIL import Image
from io import BytesIO
import win32clipboard as clipboard
import sys
import os


def get_settings():
    try:
        file = open(get_path("config.json"), "r")
        data = file.readline()
        if data:
            return json.loads(data)
        else:
            return dict()
    except FileNotFoundError:
        logging.info("Configuration file not found.")
        file = open(get_path("config.json"), "w")
        file.close()
        logging.info("Configuration file created.")
        return dict()


def save_settings(data):
    with open(get_path("config.json"), "w") as file:
        file.write(json.dumps(data))
    logging.info("Settings saved.")


def wipe_settings():
    with open(get_path("config.json"), "w") as file:
        file.truncate(0)
    logging.info("Settings wiped.")


def get_log():
    with open(get_path("app.log"), "r") as log_file:
        log = str(log_file.read())
    return log


def wipe_log():
    with open(get_path("app.log"), "r+") as file:
        file.truncate(0)  # erase log file


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
            logging.info('Chart saved as: ' + file_name)
        else:
            logging.warning("File type not recognised.")
    else:
        logging.info("Operation cancelled.")


def get_file_name(current_name):
    file = filedialog.askopenfile(title="Select file",
                                  filetypes=(("Excel files", "*.xlsx"),))
    if file:
        file_name = file.name.lower()
    else:
        file_name = current_name
        logging.info("Operation cancelled.")
    return file_name


def export_data(workbook):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=(("Excel files", "*.xlsx"),),
                                    )
    if file:
        file_path = file.name.lower().replace('/', '\\\\')
        if file_path.endswith(".xlsx"):
            workbook.save(filename=file_path)
            logging.info('Chart data saved as: ' + file.name.lower())
        else:
            logging.warning("File type not recognised.")
    else:
        logging.info("Operation cancelled.")


def save_postscript(chart):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=[('PostScript file', '*.ps'), ],
                                    defaultextension="*.ps")
    if file:
        chart.postscript(file=file.name, rotate=1)
        logging.info("Chart saved as: " + file.name)
    else:
        logging.info("Operation cancelled.")


def copy_to_clipboard(chart):
    chart_as_postscript = chart.postscript()
    chart_as_utf = chart_as_postscript.encode('utf-8')
    chart_as_bytecode = BytesIO(chart_as_utf)

    chart_as_bitmap = BytesIO()
    Image.open(chart_as_bytecode).save(chart_as_bitmap, "BMP")

    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(clipboard.CF_DIB, chart_as_bitmap.getvalue()[14:])  # [14:] removes header
    clipboard.CloseClipboard()

    chart_as_bytecode.close()
    chart_as_bitmap.close()


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'
