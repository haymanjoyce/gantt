#!/usr/bin/env python3

import loggers
import json
from tkinter import filedialog
from PIL import Image
from io import BytesIO


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


def save_image(postscript, settings):
    """Handles export of chart to various formats.  Requires Ghostscript on client machine."""
    file_types = [
        ('All files', '*.*'),
        ('PDF file', '*.pdf'),
        ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        ('BMP file', '*.bmp'),
        ('TIFF file', '*.tif'),
        ('PostScript file', '*.ps'),
    ]
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=file_types,
                                    defaultextension="*.*"
                                    )
    if file:
        file_name = file.name.lower()
        if file_name.endswith(('.pdf', '.jpg', '.png', '.bmp', '.tif', '.ps')):
            chart_encoded = postscript.encode('utf-8')
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


cli = loggers.Stream()
