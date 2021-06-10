#!/usr/bin/env python3

"""This module is for generating a template spreadsheet with, optionally, sample data."""

import logging

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font
from datetime import datetime


def create_template(data):
    workbook = Workbook()
    workbook.remove(workbook.active)
    header = NamedStyle(name="header")
    header.font = Font(bold=True)
    for key, value in data.items():
        workbook.create_sheet(key)
        workbook[key].append(value)
        for cell in workbook[key][1]:
            cell.style = header
    return workbook


def populate_template(workbook, data):
    for key, lines in data.items():
        sheet = workbook[key]
        for line in lines:
            sheet.append(line)
    return workbook


def to_date_object(string):
    return datetime.strptime(string, "%d %b %y")


def reformat_dates(workbook):
    for sheet in workbook.worksheets:
        for row in sheet:
            for cell in row:
                if isinstance(cell.value, datetime.today().__class__):
                    cell.number_format = "DD MMM YYYY"
    return workbook


TEMPLATE = {
    "Scales": ("Interval", "Height", "Fill", "Border Width", "Border Color"),
    "Bars": ("Key", "Row", "Start", "Finish", "Fill", "Border Width", "Border Color", "Layer", "Height", "Nudge"),
    "Labels": ("Row", "Date", "Text", "X Nudge", "Y Nudge", "Anchor", "Layer", "Rotation", "Width", "Justify", "Color", "Size", "Font", "Bold", "Italic", "Underline", "Strikethrough"),
    "Connectors": ("From Row", "From Date", "From Nudge", "To Row", "To Date", "To Nudge", "Arrow Head", "Width", "Color", "Layer", "Shaft Nudge"),
    "Pipes": ("Date", "Width", "Color", "Layer"),
    "Curtains": ("Start", "Finish", "Color", "Layer"),
    "Separators": ("Row", "Width", "Color", "Layer"),
    "Sections": ("From Row", "To Row", "Fill Color", "Border Color", "Border Width", "Layer"),
    "Boxes": ("X", "Y", "Width", "Height", "Fill Color", "Border Color", "Border Width", "Layer"),
}

SAMPLE = {
    "Scales": (['y', 40, 'red', 0.5, 'black'],
               ['m', 30, 'blue', 0.5, 'black'],
               ['d', 20, 'green', 0.5, 'black'],),
    "Bars": ([1, 1, to_date_object("21 Dec 20"), to_date_object("5 Jan 21"), "red", 0.5, "black"],
             [2, 3, to_date_object("21 Dec 20"), to_date_object("5 Jan 21"), "red", 0.5, "black", 1, 20],
             [3, 5, to_date_object("21 Dec 20"), to_date_object("5 Jan 21"), "red", 0.5, "black", 1, 20, -5],),
    "Labels": ([1, to_date_object("21 Dec 20"), 'one', ],
               [2, to_date_object("5 Jan 21"), 'two', ],
               [3, to_date_object("1 Jan 21"), 'three', ],),
    "Connectors": ([2, to_date_object("21 Dec 20"), 0, 6, to_date_object("1 Jan 21"), 0, 'No', 1, 'black', 1, 0],
                   [2, to_date_object("21 Dec 20"), 0, 6, to_date_object("1 Jan 21"), 0, 'Yes', 1, 'red', 1, 20],
                   [7, to_date_object("1 Jan 21"), 0, 2, to_date_object("6 Jan 21"), 0, 'No', 1, 'black', 1, 0],),
    "Pipes": ([to_date_object("2 Jan 21"), 1, 'pink', 1],
              [to_date_object("30 Jan 21"), 1, 'blue', 2],),
    "Curtains": ([to_date_object("25 Jan 21"), to_date_object("30 Jan 21"), 'light grey', 1],),
    "Separators": ([4, 2, 'purple', 1],),
    "Sections": ([10, 12, 'yellow', 'black', 1, 1],),
    "Boxes": ([300, 300, 200, 200, 'pink', 'black', 1, 1],),
}
