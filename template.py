#!/usr/bin/env python3

import logging

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font

TEMPLATE = {
    "Scales": ("Intervals", "Height", "Fill", "Border Width", "Border Color"),
    "Rows": (),
    "Tasks": ("Key", "Row", "Start", "Finish", "Fill", "Border Width", "Border Color", "Layer"),
    "Connections": (),
    "Relationships": (),
    "Curtains": (),
    "Bars": (),
    "Groups": (),
    "Text": (),
    "Box": (),
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
