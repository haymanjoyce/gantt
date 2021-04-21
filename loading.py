#!/usr/bin/env python3

import logging

from designs import Scale, Row, Task, Milestone, Relationship, Curtain  # import all will bring in logging
from designs import DESIGNS

GLOBALS = globals()


class Loader:
    def __init__(self, workbook, chart):
        self.workbook = workbook
        self.chart = chart

    def load_items(self):
        items = tuple()
        for design in DESIGNS:
            sheet_name = design + 's'
            sheet = self.workbook[sheet_name]
            sheet_headers = sheet[1]
            mapping = get_mapping(sheet_name, sheet_headers)
            if design == 'Scale':
                y = 0
                for count, sheet_row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):
                    item = GLOBALS.get(design)()
                    item.type = item.type
                    item.labels = ""
                    item.width = self.chart.width
                    item.height = sheet_row[mapping.get('HEIGHT')]
                    item.start = self.chart.start
                    item.finish = self.chart.finish
                    item.interval = sheet_row[mapping.get('INTERVAL')]
                    item.rank = count
                    item.x = 0
                    item.y = y
                    item.fill = sheet_row[mapping.get('FILL')]
                    item.border_color = sheet_row[mapping.get('BORDER COLOR')]
                    item.border_width = sheet_row[mapping.get('BORDER WIDTH')]
                    y += item.height
                    items += item,
            elif design == 'Row':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = GLOBALS.get(design)()
                    items += item,
            elif design == 'Task':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = GLOBALS.get(design)()
                    items += item,
            elif design == 'Milestone':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = GLOBALS.get(design)()
                    items += item,
            elif design == 'Relationship':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = GLOBALS.get(design)()
                    items += item,
            elif design == 'Curtain':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    item = GLOBALS.get(design)()
                    items += item,
            else:
                logging.debug(f"{design} data class not recognised.")
                raise ValueError(design)
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
