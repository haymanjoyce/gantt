#!/usr/bin/env python3

""""This module is for, where required, calculating and/or adding data class attribute values."""

import logging

from datetime import timedelta
from pprint import pprint as pp

from settings import Settings
from features import Row, Interval


class Processor:
    def __init__(self, data):
        self.items = data
        self.settings = Settings()
        self.time_delta = (self.settings.finish - self.settings.start)
        self.total_days = self.time_delta.days
        self.pixels_per_day = self.settings.width / self.total_days
        self.first_row = self.set_scales()
        self.row_height = self.get_row_height()
        self.set_intervals()
        self.set_rows()
        self.set_bars()
        self.set_labels()

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
            if scale.interval == 'DAYS':
                self.set_days(scale)
            elif scale.interval == 'WEEKS':
                pass
            elif scale.interval == 'MONTHS':
                self.set_months(scale)
            elif scale.interval == 'QUARTERS':
                pass
            elif scale.interval == 'HALVES':
                pass
            elif scale.interval == 'YEARS':
                self.set_years(scale)
            else:
                raise ValueError(scale.interval)

    def set_days(self, scale):
        for day in range(0, self.total_days):
            interval = Interval()
            interval.date = scale.start + timedelta(day)
            interval.x = day * self.pixels_per_day
            interval.y = scale.y
            interval.height = scale.height
            interval.border_width = scale.border_width
            interval.border_color = scale.border_color
            interval.fill = scale.fill
            interval.width = self.pixels_per_day
            interval.format = "%d"  # not user defined (at the moment)
            self.items += interval,

    def set_weeks(self, scale):
        pass

    def set_months(self, scale):
        current_interval_date = scale.start
        current_interval_duration = 0
        current_interval_x = 0
        current_date = scale.start
        for day in range(0, self.total_days + 32):  # number added to render any last period if partial
            if current_interval_date.month == current_date.month:
                current_interval_duration += 1
            else:
                interval = Interval()
                interval.y = scale.y
                interval.height = scale.height
                interval.border_width = scale.border_width
                interval.border_color = scale.border_color
                interval.fill = scale.fill
                interval.date = current_interval_date
                interval.format = "%b"
                interval.x = current_interval_x
                interval.width = current_interval_duration * self.pixels_per_day
                self.items += interval,
                current_interval_date = current_date
                current_interval_duration = 1  # to capture the iteration
                current_interval_x += interval.width
            current_date += timedelta(days=1)

    def set_quarters(self, scale):
        pass

    def set_halves(self, scale):
        pass

    def set_years(self, scale):
        current_interval_date = scale.start
        current_interval_duration = 0
        current_interval_x = 0
        current_date = scale.start
        for day in range(0, self.total_days + 366):  # number added to render any last period if partial
            if current_interval_date.year == current_date.year:
                current_interval_duration += 1
            else:
                interval = Interval()
                interval.y = scale.y
                interval.height = scale.height
                interval.border_width = scale.border_width
                interval.border_color = scale.border_color
                interval.fill = scale.fill
                interval.date = current_interval_date
                interval.format = "%Y"
                interval.x = current_interval_x
                interval.width = current_interval_duration * self.pixels_per_day
                self.items += interval,
                current_interval_date = current_date
                current_interval_duration = 1  # to capture the iteration
                current_interval_x += interval.width
            current_date += timedelta(days=1)

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

    def set_labels(self):
        labels = [item for item in self.items if item.type == 'label']
        for label in labels:

            delta_x = label.date - self.settings.start
            label.x = delta_x.days * self.pixels_per_day

            label.y = [item.y for item in self.items if item.type == 'row' if item.key == label.row][0]
            baseline_offset = self.row_height / 2
            label.y += baseline_offset  # aligns text to middle of row by default

            if label.x_nudge:
                label.x += label.x_nudge

            if label.y_nudge:
                label.y += label.y_nudge
