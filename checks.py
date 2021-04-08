#!/usr/bin/env python3

import logging
# from template import SHEETS


def check_merged_cells(workbook):
    issues = 0
    for sheet in workbook.sheetnames:
        if bool(workbook[sheet].merged_cells.ranges):
            logging.error(f"Merged cells found in {sheet} sheet.")
            issues += 1
    if issues == 0:
        logging.info(f"No merged cells found.")


def check_sheets_exist(workbook):
    sheet_names = workbook.sheetnames
    missing = []
    for sheet_name in SHEETS.keys():
        if sheet_name not in sheet_names:
            missing.append(sheet_name)
    if missing:
        logging.error(f"Sheets not found: {str(missing).strip('[]')}.")
    else:
        logging.info(f"No missing sheets.")


def check_header_rows_exist(workbook):
    issues = 0
    for sheet in workbook.sheetnames:
        if None in [cell.value for cell in workbook[sheet][1][:3]]:
            logging.error(f"Column header(s) missing in {sheet} sheet.")
            issues += 1
    if issues == 0:
        logging.info(f"Header rows exist.")


def check_header_rows(workbook):
    issues = 0
    for wb_sheet_name in workbook.sheetnames:
        if wb_sheet_name in SHEETS.keys():
            wb_sheet = workbook[wb_sheet_name]
            wb_field_names = [cell.value for cell in wb_sheet[1]]
            missing = ()
            for field_name in SHEETS[wb_sheet_name]:
                if field_name not in wb_field_names:
                    missing += field_name,
            if missing:
                logging.warning(f"Fields missing:\nIn {wb_sheet_name}: {', '.join(missing)}.")
                issues += 1
    if issues == 0:
        logging.info(f"No missing fields.")


def check_misspelled_headers(workbook):
    issues = 0
    for wb_sheet_name in workbook.sheetnames:
        if wb_sheet_name in SHEETS.keys():
            wb_sheet = workbook[wb_sheet_name]
            wb_field_names = [cell.value for cell in wb_sheet[1]]
            misspelled = ()
            for wb_field_name in wb_field_names:
                if wb_field_name not in SHEETS[wb_sheet_name]:
                    misspelled += wb_field_name,
            if misspelled:
                logging.warning(f"Possible misspellings:\nIn {wb_sheet_name}: {', '.join(misspelled)}.")
                issues += 1
    if issues == 0:
        logging.info(f"No misspelled fields.")
