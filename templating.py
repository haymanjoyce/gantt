#!/usr/bin/env python3

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
    "Connectors": ("From Row", "From Date", "From Nudge", "To Row", "To Date", "To Nudge", "Arrow Head", "Width", "Color", "Layer"),
}


SAMPLE = {
    "Scales": (['y', 40, 'red', 0.5, 'black'],
               ['m', 30, 'blue', 0.5, 'black'],
               ['d', 20, 'green', 0.5, 'black']),
    "Bars": ([1, 1, to_date_object("21 Dec 20"), to_date_object("5 Jan 21"), "red", 0.5, "black"],
             [2, 3, to_date_object("21 Dec 20"), to_date_object("5 Jan 21"), "red", 0.5, "black", 1, 20],
             [3, 5, to_date_object("21 Dec 20"), to_date_object("5 Jan 21"), "red", 0.5, "black", 1, 20, -5]),
    "Labels": ([1, to_date_object("21 Dec 20"), 'one', ],
               [2, to_date_object("5 Jan 21"), 'two', ],
               [3, to_date_object("1 Jan 21"), 'three', ]),
    "Connectors": ([1, to_date_object("21 Dec 20"), 0, 3, to_date_object("1 Jan 21"), 0, 'No', 1, 'black', 1],
                   [2, to_date_object("23 Dec 20"), 0, 2, to_date_object("3 Jan 21"), 0, 'Yes', 3, 'red', 1],
                   [3, to_date_object("25 Dec 20"), 0, 1, to_date_object("6 Jan 21"), 0, 'No', 1, 'black', 1],),
}
