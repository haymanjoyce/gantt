#!/usr/bin/env python3

import logging

from features import Scale, Row, Task, Milestone, Relationship, Curtain
from features import FEATURES
from settings import Settings


class Parser:
    def __init__(self, workbook):
        self.workbook = workbook
        self.settings = Settings()

    def load_items(self):
        items = tuple()
        for feature_type in FEATURES:
            sheet_name = feature_type + 's'
            sheet = self.workbook[sheet_name]
            sheet_headers = sheet[1]
            sheet_mapping = get_mapping(sheet_name, sheet_headers)
            if sheet_name == 'Scales':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = self.load_scale(sheet_row, sheet_mapping)
                    items += item,
            elif sheet_name == 'Rows':
                for sheet_row in sheet.iter_rows(min_row=2):
                    item = self.load_row(sheet_row, sheet_mapping)
                    items += item,
            elif sheet_name == 'Tasks':
                pass
            elif sheet_name == 'Milestones':
                pass
            elif sheet_name == 'Relationships':
                pass
            elif sheet_name == 'Curtains':
                pass
            else:
                raise ValueError(sheet_name)
        return items

    def load_scale(self, sheet_row, sheet_mapping):
        item = Scale()
        # item.type
        item.labels = ""
        item.width = self.settings.width
        item.height = sheet_row[sheet_mapping.get('HEIGHT')]
        item.start = self.settings.start
        item.finish = self.settings.finish
        item.interval = sheet_row[sheet_mapping.get('INTERVAL')]
        # item.rank
        item.x = self.settings.x
        # item.y
        item.fill = sheet_row[sheet_mapping.get('FILL')]
        item.border_color = sheet_row[sheet_mapping.get('BORDER COLOR')]
        item.border_width = sheet_row[sheet_mapping.get('BORDER WIDTH')]
        return item

    def load_row(self, sheet_row, sheet_mapping):
        item = Row()
        # item.type
        item.labels = ""
        item.sheet_row = sheet_row[0].row  # row number attribute of cell, not row
        item.key = sheet_row[sheet_mapping.get('KEY')].value
        item.height = sheet_row[sheet_mapping.get('HEIGHT')].value
        item.fill = sheet_row[sheet_mapping.get('FILL')].value
        item.text = sheet_row[sheet_mapping.get('TEXT')].value
        item.font_color = sheet_row[sheet_mapping.get('FONT COLOR')].value
        item.font_size = sheet_row[sheet_mapping.get('FONT SIZE')].value
        item.font_style = sheet_row[sheet_mapping.get('FONT STYLE')].value
        return item


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
