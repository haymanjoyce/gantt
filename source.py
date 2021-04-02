#!/usr/bin/env python3

import logging
import template


def check_merged_cells(workbook):
    for sheet in workbook.sheetnames:
        if bool(workbook[sheet].merged_cells.ranges):
            logging.error(f"Merged cells found in {sheet} sheet.")


def check_sheets_exist(workbook):
    target = workbook.sheetnames
    standard = template.TEMPLATE.keys()
    missing = []
    for sheet_name in standard:
        if sheet_name not in target:
            missing.append(sheet_name)
    if missing:
        logging.error(f"Sheets not found: {str(missing).strip('[]')}.")


def check_header_rows_exist(workbook):
    for sheet in workbook.sheetnames:
        if None in [cell.value for cell in workbook[sheet][1][:3]]:
            logging.error(f"Column header(s) missing in {sheet} sheet.")


def check_header_names(workbook):
    for sheet_name in workbook.sheetnames:
        get_sheet_headers(workbook[sheet_name])


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
