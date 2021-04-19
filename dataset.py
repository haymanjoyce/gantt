#!/usr/bin/env python3

import logging

from designs import Scale, Row, Task, Milestone, Relationship, Curtain  # import all will bring in logging
from designs import DESIGNS

GLOBALS = globals()


def create_object_dict(workbook, chart_object):
    object_dict = dict()
    for design in DESIGNS:
        sheet_name = design + 's'
        sheet = workbook[sheet_name]
        row_objects = get_row_objects(sheet, sheet_name, design, chart_object)
        object_dict.setdefault(sheet_name, row_objects)
    return object_dict


def get_row_objects(sheet, sheet_name, design, chart_object):
    row_objects = list()
    row_object = None
    sheet_headers = sheet[1]
    mapping = get_mapping(sheet_headers, sheet_name)
    for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
        if design == 'Scale':
            row_object = create_scale_object(design, sheet_row, mapping, chart_object)
        row_objects.append(row_object)
    return row_objects


def create_scale_object(design, sheet_row, mapping, chart_object):
    scale = GLOBALS.get(design)()
    scale.type = scale.type
    scale.labels = scale.labels
    scale.width = 800
    scale.height = sheet_row[mapping.get('HEIGHT')]
    scale.start = chart_object.start
    scale.finish = chart_object.finish
    scale.interval = sheet_row[mapping.get('INTERVAL')]
    return scale


def get_mapping(sheet_headers, sheet_name):
    mapping = dict()
    blank_columns = 0
    for header in sheet_headers:
        if header.value:
            key = header.value
            key = key.replace(" ", "_")
            key = key.strip()
            key = key.upper()
            value = header.column - 1  # needs to be 0 indexed
            mapping.setdefault(key, value)
        else:
            blank_columns += 1
    if blank_columns:
        logging.warning(f"{blank_columns} blank columns found in {sheet_name}.")
    return mapping
