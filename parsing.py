#!/usr/bin/env python3

import logging

from features import Scale, Task, Relationship, Curtain, Bar, Group
from settings import Settings


class Parser:
    def __init__(self, workbook):
        self.workbook = workbook
        self.settings = Settings()

    def load_items(self):
        items = tuple()
        features = ('Scale', 'Task', 'Relationship', 'Curtain', 'Bar', 'Group')
        for feature_type in features:
            sheet_name = feature_type + 's'
            sheet = self.workbook[sheet_name]
            sheet_headers = sheet[1]
            sheet_mapping = get_mapping(sheet_name, sheet_headers)
            if sheet_name == 'Scales':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = self.load_scale(sheet_row, sheet_mapping)
                    items += item,
            elif sheet_name == 'Tasks':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = self.load_task(sheet_row, sheet_mapping)
                    items += item,
            elif sheet_name == 'Relationships':
                pass
            elif sheet_name == 'Curtains':
                pass
            elif sheet_name == 'Bars':
                pass
            elif sheet_name == 'Groups':
                pass
            else:
                raise ValueError(sheet_name)
        return items

    def load_scale(self, sheet_row, sheet_mapping):
        item = Scale()
        # item.type
        item.tags = ""
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

    def load_task(self, sheet_row, sheet_mapping):
        item = Task()
        item.row = sheet_row[sheet_mapping.get('ROW')]
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
