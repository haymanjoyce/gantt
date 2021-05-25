#!/usr/bin/env python3

import logging

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font

TEMPLATE = {
    "Scales": ("Interval", "Height", "Fill", "Border Width", "Border Color"),
    "Bars": ("Key", "Row", "Start", "Finish", "Fill", "Border Width", "Border Color", "Layer", "Height", "Nudge"),
    "Labels": ("Temp", ),
}

SAMPLE = {
    "Scales": (['y', 40, 'red', 1, 'black'],
               ['m', 30, 'blue', 1, 'black'],
               ['d', 20, 'green', 0.5, 'black']),
    "Bars": ([1, 1, "21 Dec 20", "5 Jan 21", "red", 0.5, "black"],
             [2, 3, "21 Dec 20", "5 Jan 21", "red", 0.5, "black", 1, 20],
             [3, 5, "21 Dec 20", "5 Jan 21", "red", 0.5, "black", 1, 20, -5]),
    "Labels": (['temp', ],
               ['temp', ],
               ['temp', ]),
}


def create_workbook(data):
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


def populate_workbook(workbook, data):
    for key, value in data.items():
        sheet = workbook[key]
        for row in value:
            sheet.append(row)
    return workbook
