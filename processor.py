#!/usr/bin/env python3

import logging

from datetime import timedelta

from settings import Settings
from features import Row, Interval


class Processor:
    def __init__(self, data):
        self.items = data
        self.settings = Settings()
        self.time_delta = (self.settings.finish - self.settings.start)
        self.total_days = self.time_delta.days + 1  # range inclusive of end dates
        self.pixels_per_day = self.settings.width / self.total_days
        self.first_row = self.set_scales()
        self.row_height = self.get_row_height()
        self.set_intervals()
        self.set_rows()
        self.set_bars()

    def set_scales(self):
        scales = [item for item in self.items if item.type == 'scale']
        y = self.settings.y
        for scale in scales:
            scale.x = self.settings.x
            scale.y = y
            scale.width = self.settings.width
            scale.start = self.settings.start
            scale.finish = self.settings.finish
            y += scale.height
        return y  # first row

    def set_intervals(self):
        scales = [item for item in self.items if item.type == 'scale']
        for scale in scales:
            for day in range(0, self.total_days):
                interval = Interval()
                interval.date = scale.start + timedelta(day)
                interval.x = day * self.pixels_per_day
                interval.y = scale.y
                interval.width = self.pixels_per_day
                interval.height = scale.height
                interval.border_width = scale.border_width
                interval.border_color = scale.border_color
                interval.fill = scale.fill
                self.items += interval,

    def get_row_height(self):
        row_space = self.settings.height - self.first_row
        max_height = row_space / self.settings.num_rows
        if self.settings.row_height > max_height:
            return max_height
        else:
            return self.settings.row_height

    def set_rows(self):
        y = self.first_row
        for i in range(0, self.settings.num_rows):
            row = Row()
            row.key = i + 1
            row.x = self.settings.x
            row.y = y
            row.width = self.settings.width
            row.height = self.row_height
            row.layer = 1
            self.items += row,
            y += self.row_height

    def set_bars(self):
        bars = [item for item in self.items if item.type == 'bar']
        for bar in bars:

            if bar.height:
                if bar.height > self.row_height:
                    bar.height = self.row_height
            else:
                bar.height = self.row_height

            if bar.nudge:
                if bar.nudge > self.row_height:
                    bar.nudge = self.row_height
                if bar.nudge < (self.row_height * -1):
                    bar.nudge = (self.row_height * -1)

            delta_x = bar.start - self.settings.start
            delta_width = bar.finish - bar.start

            bar.x = delta_x.days * self.pixels_per_day
            bar.y = [item.y for item in self.items if item.type == 'row' if item.key == bar.row][0]
            bar.width = delta_width.days * self.pixels_per_day

            if bar.nudge:
                bar.y += bar.nudge
