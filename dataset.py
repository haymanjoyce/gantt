#!/usr/bin/env python3

import datetime
import logging

import filing
import designs


class Dataset:
    def __init__(self, workbook):

        self.workbook = workbook
        self.settings = filing.get_config_data()
        self.dataset_dict = dict()
        self.populate()

    def populate(self):
        self.create_chart()
        self.create_scales()
        self.create_rows()

    def create_chart(self):
        chart = designs.Chart()
        chart.type = "chart"
        chart.width = int(self.settings['width'])
        chart.height = int(self.settings['height'])
        chart.start = datetime.datetime.strptime(self.settings['start'], '%Y/%m/%d')
        chart.finish = datetime.datetime.strptime(self.settings['finish'], '%Y/%m/%d')
        self.dataset_dict.setdefault("chart", chart)

    def create_scales(self):
        sheet_name = "Scales"
        dict_key = sheet_name.lower()
        data = self.workbook[sheet_name]
        headers = data[1]
        mapping = get_mapping(headers, sheet_name)
        object_list = list()
        for sheet_row in data.iter_rows(min_row=2, values_only=True):
            scale = designs.Scale()
            scale.height = sheet_row[mapping.get('HEIGHT')]
            scale.start = sheet_row[mapping.get('START')]
            scale.finish = sheet_row[mapping.get('FINISH')]
            scale.interval = sheet_row[mapping.get('INTERVAL')]
            object_list.append(scale)
        self.dataset_dict.setdefault(dict_key, object_list)

    def create_rows(self):
        row_data = self.workbook["Rows"]
        rows = list()
        for sheet_row in row_data.iter_rows(min_row=2, values_only=True):
            row = designs.Row()
            row.row_number = sheet_row[1]
            rows.append(row)
        self.dataset_dict.setdefault("rows", rows)

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


def get_mapping(headers, sheet_name):
    mapping = dict()
    blank_columns = 0
    for header in headers:
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
