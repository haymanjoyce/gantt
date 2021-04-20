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
            for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                item = GLOBALS.get(design)()
                if design == 'Scale':
                    item.type = item.type
                    item.labels = ""
                    item.width = self.chart.width
                    item.height = sheet_row[mapping.get('HEIGHT')]
                    item.start = self.chart.start
                    item.finish = self.chart.finish
                    item.interval = sheet_row[mapping.get('INTERVAL')]
                elif design == 'Row':
                    pass
                elif design == 'Task':
                    pass
                elif design == 'Milestone':
                    pass
                elif design == 'Relationship':
                    pass
                elif design == 'Curtain':
                    pass
                else:
                    logging.debug(f"{design} data class not recognised.")
                    raise ValueError(design)
                items += item,
        return items


def get_mapping(sheet_name, sheet_headers):
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
