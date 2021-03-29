#!/usr/bin/env python3

"""Ragbag of functions that are meant to be class or object agnostic (i.e. static)."""

import logging
import json
from tkinter import filedialog
from PIL import Image
from io import BytesIO
import win32clipboard as clipboard
import sys
import os

LOG_FILE = "app.log"
CONFIG_FILE = "config.json"


# MISCELLANEOUS

def get_path(filename):
    """Provides path to app if bundled into one .exe file."""
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'


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

    logging.info("Image copied to clipboard.")


# SETTINGS

def get_settings():
    try:
        file = open(get_path(CONFIG_FILE), "r")
        data = file.readline()
        if data:
            return json.loads(data)
        else:
            return dict()
    except FileNotFoundError:
        logging.debug("Configuration file not found.")
        file = open(get_path(CONFIG_FILE), "w")
        file.close()
        logging.debug("Configuration file created.")
        return dict()


def save_settings(data):
    with open(get_path(CONFIG_FILE), "w") as file:
        file.write(json.dumps(data))
    logging.info("Settings saved.")


def wipe_settings():
    with open(get_path(CONFIG_FILE), "w") as file:
        file.truncate(0)
    logging.info("Settings wiped.")


# LOG

def get_log():
    with open(get_path(LOG_FILE), "r") as log_file:
        log = str(log_file.read())
    return log


def wipe_log():
    with open(get_path(LOG_FILE), "r+") as file:
        file.truncate(0)  # erase log file


# DIALOGUES

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
        logging.debug("Operation cancelled.")


def get_file_name(current_name):
    file = filedialog.askopenfile(title="Select file",
                                  filetypes=(("Excel files", "*.xlsx"),))
    if file:
        file_name = file.name.lower()
    else:
        file_name = current_name
        logging.debug("Operation cancelled.")
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
        logging.debug("Operation cancelled.")


def save_postscript(chart):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=[('PostScript file', '*.ps'), ],
                                    defaultextension="*.ps")
    if file:
        chart.postscript(file=file.name, rotate=1)
        logging.info("Chart saved as: " + file.name)
    else:
        logging.debug("Operation cancelled.")


# OPENPYXL

def check_merged_cells(workbook):
    for sheet in workbook.sheetnames:
        if bool(workbook[sheet].merged_cells.ranges):
            logging.error(f"Merged cells found in {sheet} sheet.")


def check_header_rows_exists(workbook):
    for sheet in workbook.sheetnames:
        if None in [cell.value for cell in workbook[sheet][1][:3]]:
            logging.error(f"Column header(s) missing in {sheet} sheet.")


def check_header_names(workbook):
    for sheet_name in workbook.sheetnames:
        get_sheet_headers(workbook[sheet_name])


def run_checks(workbook):
    check_merged_cells(workbook)
    check_header_names(workbook)
    check_header_names(workbook)


def get_sheet_headers(sheet):
    return [cell.value for cell in sheet[1][:sheet.max_column]]


def get_sheet_names(workbook):
    return workbook.sheetnames


def create_template():
    pass


def create_sample():
    pass


def create_export():
    pass
