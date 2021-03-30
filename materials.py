#!/usr/bin/env python3

"""This module is for creating a list of dataclass objects."""

import datetime

import utils
import designs


class Materials:
    def __init__(self, workbook):

        self.workbook = workbook
        self.settings = utils.get_settings()
        self.inventory = dict()
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
        self.inventory.setdefault("chart", chart)

    def create_scales(self):
        data = self.workbook["Scales"]
        scales = list()
        for row in data.iter_rows(min_row=2, values_only=True):
            scale = designs.Scale()
            scale.interval = row[1]
            scales.append(scale)
        self.inventory.setdefault("scales", scales)
        print(self.inventory.get("scales"))
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
