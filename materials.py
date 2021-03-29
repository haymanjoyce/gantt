#!/usr/bin/env python3

"""This module is for creating a list of dataclass objects."""

import datetime

import utils
import designs


class Materials:
    def __init__(self, workbook):

        self.workbook = workbook
        self.settings = utils.get_settings()
        self.data = list()
        self.populate_list()

    def populate_list(self):
        self.create_chart()

    def create_chart(self):
        chart = designs.Chart()
        chart.name = "chart"
        chart.width = int(self.settings['width'])
        chart.height = int(self.settings['height'])
        chart.start = datetime.datetime.strptime(self.settings['start'], '%Y/%m/%d')
        chart.finish = datetime.datetime.strptime(self.settings['finish'], '%Y/%m/%d')
        self.data.append(chart)

    def create_scale(self):
        pass

    def create_scales(self):
        pass

    def create_row(self):
        pass

    def create_rows(self):
        pass

    def create_task(self):
        pass

    def create_tasks(self):
        pass

    def create_milestone(self):
        pass

    def create_milestones(self):
        pass

    def create_relationship(self):
        pass

    def create_relationships(self):
        pass

    def create_curtain(self):
        pass

    def create_curtains(self):
        pass

    def create_bar(self):
        pass

    def create_bars(self):
        pass
