#!/usr/bin/env python3

import datetime

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
        chart.name = "chart"
        chart.width = int(self.settings['width'])
        chart.height = int(self.settings['height'])
        chart.start = datetime.datetime.strptime(self.settings['start'], '%Y/%m/%d')
        chart.finish = datetime.datetime.strptime(self.settings['finish'], '%Y/%m/%d')
        self.dataset_dict.setdefault("chart", chart)

    def create_scales(self):
        scale_data = self.workbook["Scales"]
        mapping = get_mapping(scale_data)
        print(mapping)
        scales = list()
        for sheet_row in scale_data.iter_rows(min_row=2, values_only=True):
            scale = designs.Scale()
            scale.interval = sheet_row[5]
            scales.append(scale)
        self.dataset_dict.setdefault("scales", scales)

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


def get_mapping(sheet):
    """Maps field names to column numbers in sheet."""
    headers = sheet[1]
    mapping = dict()
    for header in headers:
        key = header.value
        key = key.replace(" ", "_")
        key = key.strip()
        key = key.upper()
        value = header.column
        mapping.setdefault(key, value)
    return mapping
