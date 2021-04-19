#!/usr/bin/env python3

import logging
from tkinter import filedialog
from PIL import Image
from io import BytesIO


def save_image(chart):
    """Handles export of chart to various formats.  Requires Ghostscript on client machine."""
    file_types = [
        ('PDF file', '*.pdf'),
        ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        ('BMP file', '*.bmp'),
        ('TIFF file', '*.tif'),
    ]
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=file_types,
                                    defaultextension="*.pdf",
                                    initialfile="*.pdf"
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
    file = filedialog.askopenfile(title="Select File",
                                  filetypes=(("Excel files", "*.xlsx"),),
                                  )
    if file:
        file_name = file.name.lower()
    else:
        file_name = current_name
        logging.debug("Operation cancelled.")
    return file_name


def save_postscript(chart):
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=[('PostScript file', '*.ps'), ],
                                    defaultextension="*.ps",
                                    initialfile="*.ps")
    if file:
        chart.postscript(file=file.name, rotate=1)
        logging.info("Chart saved as: " + file.name)
    else:
        logging.debug("Operation cancelled.")


def export_workbook(workbook):
    try:
        file = filedialog.asksaveasfile(mode="w",
                                        title="Save As",
                                        filetypes=(("Excel files", "*.xlsx"),),
                                        initialfile="*.xlsx"
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
    except PermissionError:
        logging.warning("Permission denied.  Destination file may be open.")
