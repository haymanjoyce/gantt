#!/usr/bin/env python3

import datetime

import filing
import designs


class Dataset:
    def __init__(self, workbook):

        self.workbook = workbook
        self.settings = filing.get_settings()
        self.dataset = dict()
        self.populate()

    def populate(self):
        self.create_chart()
        self.create_scales()

    def create_chart(self):
        chart = designs.Chart()
        chart.name = "chart"
        chart.width = int(self.settings['width'])
        chart.height = int(self.settings['height'])
        chart.start = datetime.datetime.strptime(self.settings['start'], '%Y/%m/%d')
        chart.finish = datetime.datetime.strptime(self.settings['finish'], '%Y/%m/%d')
        self.dataset.setdefault("chart", chart)

    def create_scales(self):
        data = self.workbook["Scales"]
        scales = list()
        for row in data.iter_rows(min_row=2, values_only=True):
            scale = designs.Scale()
            scale.interval = row[1]
            scales.append(scale)
        self.dataset.setdefault("scales", scales)
        # a = [cell.value for cell in data[1][:3]

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
