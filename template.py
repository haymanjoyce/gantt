#!/usr/bin/env python3

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font

SCALES = ('Placement', 'Interval', 'Scale Height', 'Date Format', 'Fill Color', 'Font Color', 'Font Size', 'Font Style')
ROWS = ('Row Number', 'Height', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style')
TASKS = ('Parent Row', 'ID', 'Start Date', 'Finish Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Text Layer', 'Bar Layer')
MILESTONES = ('Parent Row', 'ID', 'Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Text Layer', 'Bar Layer')
RELATIONSHIPS = ('Source Task', 'Destination Task', 'Line Width', 'Line Color')
CURTAINS = ('Start Date', 'Finish Date', 'Fill Color')
BARS = ('Date', 'Line Color', 'Line Width')

SHEETS = {'Scales': SCALES,
          'Rows': ROWS,
          'Tasks': TASKS,
          'Milestones': MILESTONES,
          'Relationships': RELATIONSHIPS,
          'Curtains': CURTAINS,
          'Bars': BARS}


def create_template():
    workbook = Workbook()
    workbook.remove(workbook.active)
    header = NamedStyle(name="header")
    header.font = Font(bold=True)
    for key, value in SHEETS.items():
        workbook.create_sheet(key)
        workbook[key].append(value)
        for cell in workbook[key][1]:
            cell.style = header
    return workbook
