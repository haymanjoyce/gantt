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


def check_fieldnames_exist(workbook, mandatory=True):
    for sheet_name in workbook.sheetnames[:1]:
        user_headers = get_sheet_fieldnames(workbook[sheet_name])
        template_sheet = template.TEMPLATE.get(sheet_name)
        template_sheet_fields = template_sheet.keys()
        print(user_headers)
        print(template_sheet_fields)
        for key in template_sheet_fields:
            template_mandatory = template_sheet_fields.get("MANDATORY")
            template_names = template_sheet_fields.get("NAMES")


def get_sheet_fieldnames(sheet):
    return [cell.value for cell in sheet[1][:sheet.max_column]]


def get_field_positions(sheet):
    return [(index, value) for index, value in enumerate(get_sheet_fieldnames(sheet))]


def create_template():
    pass


def create_sample():
    pass


def create_export():
    pass
