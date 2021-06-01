#!/usr/bin/env python3

"""This module is for loading Excel (i.e. user) data into data classes."""

import logging

from features import Scale, Bar, Label

GLOBALS = globals()


def load_scale(sheet_row, sheet_mapping):
    item = Scale()
    item.interval = sheet_row[sheet_mapping.get('INTERVAL')]
    item.height = sheet_row[sheet_mapping.get('HEIGHT')]
    item.fill = sheet_row[sheet_mapping.get('FILL')]
    item.border_width = sheet_row[sheet_mapping.get('BORDER WIDTH')]
    item.border_color = sheet_row[sheet_mapping.get('BORDER COLOR')]
    return item


def load_bar(sheet_row, sheet_mapping):
    item = Bar()
    item.key = sheet_row[sheet_mapping.get('KEY')]
    item.row = sheet_row[sheet_mapping.get('ROW')]
    item.start = sheet_row[sheet_mapping.get('START')]
    item.finish = sheet_row[sheet_mapping.get('FINISH')]
    item.fill = sheet_row[sheet_mapping.get('FILL')]
    item.border_width = sheet_row[sheet_mapping.get('BORDER WIDTH')]
    item.border_color = sheet_row[sheet_mapping.get('BORDER COLOR')]
    item.layer = sheet_row[sheet_mapping.get('LAYER')]
    item.height = sheet_row[sheet_mapping.get('HEIGHT')]
    item.nudge = sheet_row[sheet_mapping.get('NUDGE')]
    return item


def load_label(sheet_row, sheet_mapping):
    item = Label()
    item.layer = sheet_row[sheet_mapping.get('LAYER')]
    item.row = sheet_row[sheet_mapping.get('ROW')]
    item.date = sheet_row[sheet_mapping.get('DATE')]
    item.text = sheet_row[sheet_mapping.get('TEXT')]
    item.x_nudge = sheet_row[sheet_mapping.get('X NUDGE')]
    item.y_nudge = sheet_row[sheet_mapping.get('Y NUDGE')]
    item.color = sheet_row[sheet_mapping.get('COLOR')]
    item.size = sheet_row[sheet_mapping.get('SIZE')]
    item.font = sheet_row[sheet_mapping.get('FONT')]
    item.weight = sheet_row[sheet_mapping.get('WEIGHT')]
    item.anchor = sheet_row[sheet_mapping.get('ANCHOR')]
    item.rotation = sheet_row[sheet_mapping.get('ROTATION')]
    item.width = sheet_row[sheet_mapping.get('WIDTH')]
    item.justify = sheet_row[sheet_mapping.get('JUSTIFY')]
    return item


LOADERS = {'Scales': GLOBALS['load_scale'],
           'Bars': GLOBALS['load_bar'],
           'Labels': GLOBALS['load_label'],
           }


def load_items(workbook):
    items = tuple()
    for sheet_name, loader in LOADERS.items():
        sheet = workbook[sheet_name]
        sheet_headers = sheet[1]
        sheet_mapping = get_mapping(sheet_name, sheet_headers)
        for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
            item = loader(sheet_row, sheet_mapping)
            items += item,
    return items


def get_mapping(sheet_name, sheet_headers):
    mapping = dict()
    blank_columns = 0
    for header in sheet_headers:
        if header.value:
            key = header.value
            # key = key.replace(" ", "_")
            key = key.strip()
            key = key.upper()
            value = header.column - 1  # needs to be 0 indexed
            mapping.setdefault(key, value)
        else:
            blank_columns += 1
    if blank_columns:
        logging.warning(f"{blank_columns} blank columns found in {sheet_name}.")
    return mapping
