#!/usr/bin/env python3

import logging

from attr import attrs, attrib

SHEETNAMES = ['Scales', 'Rows', 'Tasks', 'Milestones', 'Relationships', 'Curtains', 'Bars']

SCALES = ['Placement', 'Interval', 'Scale Height', 'Date Format', 'Fill Color', 'Font Color', 'Font Size', 'Font Style']
ROWS = ['Row Number', 'Row Height', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style']
TASKS = ['Parent Row', 'Start Date', 'Finish Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Task Number', 'Layer']
MILESTONES = ['Parent Row', 'Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Task Number', 'Layer']
RELATIONSHIPS = ['Source Task', 'Destination Task', 'Line Width', 'Line Color']
CURTAINS = ['Start Date', 'Finish Date', 'Fill Color']
BARS = ['Date', 'Line Color', 'Line Width']


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


def get_header_positions(sheet):
    return [(index, value) for index, value in enumerate(get_sheet_headers(sheet))]


def create_template():
    pass


def create_sample():
    pass


def create_export():
    pass
