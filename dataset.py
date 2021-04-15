#!/usr/bin/env python3

import datetime
import logging

from attr import attrs, attrib, Factory

import filing
import designs


@attrs
class ChartData:

    type = attrib(default="chart")
    settings = attrib(default=Factory(filing.get_config_data))
    width = attrib()
    height = attrib()
    start = attrib()
    finish = attrib()

    @width.default
    def default_width(self):
        if self.settings.get('width'):
            return int(self.settings['width'])
        else:
            return 800

    @height.default
    def default_height(self):
        if self.settings.get('height'):
            return int(self.settings['height'])
        else:
            return 600

    @start.default
    def default_start(self):
        if self.settings.get('start'):
            return datetime.datetime.strptime(self.settings['start'], '%Y/%m/%d')
        else:
            return datetime.datetime.today()

    @finish.default
    def default_finish(self):
        if self.settings.get('finish'):
            return datetime.datetime.strptime(self.settings['finish'], '%Y/%m/%d')
        else:
            return self.start + datetime.timedelta(20)


class RowData:
    def __init__(self, workbook):

        self.workbook = workbook
        self.settings = filing.get_config_data()
        self.sheet_dict = dict()

    def create_objects(self):
        sheet_name = "Scales"
        dict_key = sheet_name.lower()
        sheet_data = self.workbook[sheet_name]
        sheet_headers = sheet_data[1]
        mapping = get_mapping(sheet_headers, sheet_name)
        object_list = list()
        for sheet_row in sheet_data.iter_rows(min_row=2, values_only=True):
            new_obj = designs.Scale()
            new_obj.height = sheet_row[mapping.get('HEIGHT')]
            new_obj.start = sheet_row[mapping.get('START')]
            new_obj.finish = sheet_row[mapping.get('FINISH')]
            new_obj.interval = sheet_row[mapping.get('INTERVAL')]
            object_list.append(new_obj)
        self.sheet_dict.setdefault(dict_key, object_list)

    def create_rows(self):
        pass

    def create_tasks(self):
        pass

    def create_milestones(self):
        pass

    def create_relationships(self):
        pass

    def create_curtains(self):
        pass

    def create_bars(self):
        pass


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
