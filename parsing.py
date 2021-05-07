#!/usr/bin/env python3

import logging

from features import Scale, Row, Task, Milestone, Relationship, Curtain
from features import FEATURES

from settings import Settings

GLOBALS = globals()


class Parser:
    def __init__(self, workbook):
        self.workbook = workbook
        self.settings = Settings()

    def load_items(self):
        features = tuple()
        for feature_type in FEATURES:
            sheet_name = feature_type + 's'
            sheet = self.workbook[sheet_name]
            sheet_headers = sheet[1]
            mapping = get_mapping(sheet_name, sheet_headers)
            if feature_type == 'Scale':
                # y = self.settings.y
                for count, sheet_row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):
                    feature = GLOBALS.get(feature_type)()
                    # feature.type
                    feature.labels = ""
                    feature.width = self.settings.width
                    feature.height = sheet_row[mapping.get('HEIGHT')]
                    feature.start = self.settings.start
                    feature.finish = self.settings.finish
                    feature.interval = sheet_row[mapping.get('INTERVAL')]
                    feature.rank = count
                    feature.x = self.settings.x
                    # feature.y
                    feature.fill = sheet_row[mapping.get('FILL')]
                    feature.border_color = sheet_row[mapping.get('BORDER COLOR')]
                    feature.border_width = sheet_row[mapping.get('BORDER WIDTH')]
                    # y += feature.height
                    features += feature,
            elif feature_type == 'Row':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    feature = GLOBALS.get(feature_type)()
                    features += feature,
            elif feature_type == 'Task':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    feature = GLOBALS.get(feature_type)()
                    features += feature,
            elif feature_type == 'Milestone':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    feature = GLOBALS.get(feature_type)()
                    features += feature,
            elif feature_type == 'Relationship':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    feature = GLOBALS.get(feature_type)()
                    features += feature,
            elif feature_type == 'Curtain':
                for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                    feature = GLOBALS.get(feature_type)()
                    features += feature,
            else:
                logging.debug(f"{feature_type} data class not recognised.")
                raise ValueError(feature_type)
        return features


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
