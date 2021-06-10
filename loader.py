#!/usr/bin/env python3

"""This module is for loading Excel (i.e. user) data into dataclass objects."""

import logging

from features import Scale, Bar, Label, Connector, Pipe, Curtain, Separator, Section, Box, Note


class Loader:
    def __init__(self, workbook):
        self.workbook = workbook
        self.items = tuple()
        self.assignments = {'Scales': self.load_scale,
                            'Bars': self.load_bar,
                            'Labels': self.load_label,
                            'Connectors': self.load_connector,
                            'Pipes': self.load_pipe,
                            'Curtains': self.load_curtain,
                            'Separators': self.load_separator,
                            'Sections': self.load_section,
                            'Boxes': self.load_box,
                            'Notes': self.load_note,
                            }
        self.load_items()

    def load_items(self):
        for sheet_name, loader in self.assignments.items():
            sheet = self.workbook[sheet_name]
            sheet_headers = sheet[1]
            sheet_mapping = self.get_mapping(sheet_name, sheet_headers)
            for sheet_row in sheet.iter_rows(min_row=2, values_only=True):
                item = loader(sheet_row, sheet_mapping)
                self.items += item,

    @staticmethod
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

    @staticmethod
    def load_scale(sheet_row, sheet_mapping):
        item = Scale()
        item.interval = sheet_row[sheet_mapping.get('INTERVAL')]
        item.height = sheet_row[sheet_mapping.get('HEIGHT')]
        item.fill = sheet_row[sheet_mapping.get('FILL')]
        item.border_width = sheet_row[sheet_mapping.get('BORDER WIDTH')]
        item.border_color = sheet_row[sheet_mapping.get('BORDER COLOR')]
        return item

    @staticmethod
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

    @staticmethod
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
        item.anchor = sheet_row[sheet_mapping.get('ANCHOR')]
        item.rotation = sheet_row[sheet_mapping.get('ROTATION')]
        item.width = sheet_row[sheet_mapping.get('WIDTH')]
        item.justify = sheet_row[sheet_mapping.get('JUSTIFY')]
        item.bold = sheet_row[sheet_mapping.get('BOLD')]
        item.italic = sheet_row[sheet_mapping.get('ITALIC')]
        item.underline = sheet_row[sheet_mapping.get('UNDERLINE')]
        item.strikethrough = sheet_row[sheet_mapping.get('STRIKETHROUGH')]
        return item

    @staticmethod
    def load_connector(sheet_row, sheet_mapping):
        item = Connector()
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        item.from_row = sheet_row[sheet_mapping.get('FROM ROW')]
        item.from_date = sheet_row[sheet_mapping.get('FROM DATE')]
        item.from_nudge = sheet_row[sheet_mapping.get('FROM NUDGE')]
        item.to_row = sheet_row[sheet_mapping.get('TO ROW')]
        item.to_date = sheet_row[sheet_mapping.get('TO DATE')]
        item.to_nudge = sheet_row[sheet_mapping.get('TO NUDGE')]
        item.arrow_head = sheet_row[sheet_mapping.get('ARROW HEAD')]
        item.width = sheet_row[sheet_mapping.get('WIDTH')]
        item.color = sheet_row[sheet_mapping.get('COLOR')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        item.shaft_nudge = sheet_row[sheet_mapping.get('SHAFT NUDGE')]
        return item

    @staticmethod
    def load_pipe(sheet_row, sheet_mapping):
        item = Pipe()
        item.date = sheet_row[sheet_mapping.get('DATE')]
        item.width = sheet_row[sheet_mapping.get('WIDTH')]
        item.color = sheet_row[sheet_mapping.get('COLOR')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        return item

    @staticmethod
    def load_curtain(sheet_row, sheet_mapping):
        item = Curtain()
        item.start = sheet_row[sheet_mapping.get('START')]
        item.finish = sheet_row[sheet_mapping.get('FINISH')]
        item.color = sheet_row[sheet_mapping.get('COLOR')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        return item

    @staticmethod
    def load_separator(sheet_row, sheet_mapping):
        item = Separator()
        item.row = sheet_row[sheet_mapping.get('ROW')]
        item.width = sheet_row[sheet_mapping.get('WIDTH')]
        item.color = sheet_row[sheet_mapping.get('COLOR')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        return item

    @staticmethod
    def load_section(sheet_row, sheet_mapping):
        item = Section()
        item.from_row = sheet_row[sheet_mapping.get('FROM ROW')]
        item.to_row = sheet_row[sheet_mapping.get('TO ROW')]
        item.color = sheet_row[sheet_mapping.get('FILL COLOR')]
        item.border_color = sheet_row[sheet_mapping.get('BORDER COLOR')]
        item.border_width = sheet_row[sheet_mapping.get('BORDER WIDTH')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        return item

    @staticmethod
    def load_box(sheet_row, sheet_mapping):
        item = Box()
        item.x = sheet_row[sheet_mapping.get('X')]
        item.y = sheet_row[sheet_mapping.get('Y')]
        item.width = sheet_row[sheet_mapping.get('WIDTH')]
        item.height = sheet_row[sheet_mapping.get('HEIGHT')]
        item.fill_color = sheet_row[sheet_mapping.get('FILL COLOR')]
        item.border_color = sheet_row[sheet_mapping.get('BORDER COLOR')]
        item.border_width = sheet_row[sheet_mapping.get('BORDER WIDTH')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        return item


    @staticmethod
    def load_note(sheet_row, sheet_mapping):
        item = Note()
        item.text = sheet_row[sheet_mapping.get('TEXT')]
        item.x = sheet_row[sheet_mapping.get('X')]
        item.y = sheet_row[sheet_mapping.get('Y')]
        item.layer = sheet_row[sheet_mapping.get('LAYER')]
        item.color = sheet_row[sheet_mapping.get('COLOR')]
        item.size = sheet_row[sheet_mapping.get('SIZE')]
        item.font = sheet_row[sheet_mapping.get('FONT')]
        item.anchor = sheet_row[sheet_mapping.get('ANCHOR')]
        item.rotation = sheet_row[sheet_mapping.get('ROTATION')]
        item.width = sheet_row[sheet_mapping.get('WIDTH')]
        item.justify = sheet_row[sheet_mapping.get('JUSTIFY')]
        item.bold = sheet_row[sheet_mapping.get('BOLD')]
        item.italic = sheet_row[sheet_mapping.get('ITALIC')]
        item.underline = sheet_row[sheet_mapping.get('UNDERLINE')]
        item.strikethrough = sheet_row[sheet_mapping.get('STRIKETHROUGH')]
        return item
