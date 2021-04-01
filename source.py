#!/usr/bin/env python3

import logging

VARIANTS = {
    'Start Date': ('Start', ),
    'Finish Date': ('Finish', ),
}


def get_variants(field_name):
    """We don't bother with case (because we convert all to lower case when reading)."""
    variants = (field_name.strip(), field_name.replace(" ", ""), " ".join(field_name.split()), )
    if field_name in VARIANTS:
        variants += VARIANTS.get(field_name)
    return variants


def create_field_dict(field_name, index):
    variants = get_variants(field_name)
    field_dict = dict()
    field_dict.setdefault("MANDATORY", True)
    field_dict.setdefault("NAMES", tuple(set((field_name, ) + variants)))
    field_dict.setdefault("COLUMN", int(index))
    return field_dict


def create_sheet_dict(sheet_headers):
    sheet_dict = dict()
    for index, field_name in enumerate(sheet_headers):
        field_dict = create_field_dict(field_name, index)
        sheet_dict.setdefault(field_name, field_dict)
    return sheet_dict


def create_workbook_dict(workbook):
    wb_dict = dict()
    for sheet_name in workbook.sheetnames:
        sheet_headers = get_sheet_headers(workbook[sheet_name])
        sheet_dict = create_sheet_dict(sheet_headers)
        wb_dict.setdefault(sheet_name, sheet_dict)
    return wb_dict


def check_merged_cells(workbook):
    for sheet in workbook.sheetnames:
        if bool(workbook[sheet].merged_cells.ranges):
            logging.error(f"Merged cells found in {sheet} sheet.")


def check_sheets_exist(workbook):
    pass


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
