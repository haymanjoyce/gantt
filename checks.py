#!/usr/bin/env python3

import logging

SCALES = ('Placement', 'Interval', 'Scale Height', 'Date Format', 'Fill Color', 'Font Color', 'Font Size', 'Font Style')
ROWS = ('Row Number', 'Row Height', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style')
TASKS = ('Parent Row', 'Start Date', 'Finish Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Task Number', 'Layer')
MILESTONES = ('Parent Row', 'Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Task Number', 'Layer')
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


def check_merged_cells(workbook):
    for sheet in workbook.sheetnames:
        if bool(workbook[sheet].merged_cells.ranges):
            logging.error(f"Merged cells found in {sheet} sheet.")


def check_sheets_exist(workbook):
    sheet_names = workbook.sheetnames
    missing = []
    for sheet_name in SHEETS.keys():
        if sheet_name not in sheet_names:
            missing.append(sheet_name)
    if missing:
        logging.error(f"Sheets not found: {str(missing).strip('[]')}.")


def check_header_rows_exist(workbook):
    for sheet in workbook.sheetnames:
        if None in [cell.value for cell in workbook[sheet][1][:3]]:
            logging.error(f"Column header(s) missing in {sheet} sheet.")


def check_header_rows(workbook):
    for wb_sheet_name in workbook.sheetnames:
        if wb_sheet_name in SHEETS.keys():
            wb_sheet = workbook[wb_sheet_name]
            wb_field_names = [cell.value for cell in wb_sheet[1]]
            missing = ()
            for field_name in SHEETS[wb_sheet_name]:
                if field_name not in wb_field_names:
                    missing += field_name,
            if missing:
                logging.warning(f"Fields missing from {wb_sheet_name}: {', '.join(missing)}.")
