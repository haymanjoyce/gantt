#!/usr/bin/env python3

""""This module is for, where required, configuring dataclass object values."""

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
        self.total_row_space = self.settings.height - self.first_row
        self.max_row_height = self.total_row_space / self.settings.num_rows
        self.row_height = self.get_row_height()
        self.bottom_line = (self.row_height * self.settings.num_rows) + self.first_row

        self.set_intervals()
        self.set_rows()
        self.set_bars()
        self.set_labels()
        self.set_connectors()
        self.set_pipes()
        self.set_curtains()
        self.set_separators()
        self.set_sections()
        self.set_notes()

    def get_row_height(self):
        if self.settings.row_height > self.max_row_height:
            return self.max_row_height
        else:
            return self.settings.row_height

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

    def set_connectors(self):
        connectors = [item for item in self.items if item.type == 'connector']
        rows = [item for item in self.items if item.type == 'row']
        for connector in connectors:

            from_x_delta = connector.from_date - self.settings.start
            connector.from_x = from_x_delta.days * self.pixels_per_day
            connector.from_x += connector.from_nudge

            to_x_delta = connector.to_date - self.settings.start
            connector.to_x = to_x_delta.days * self.pixels_per_day
            connector.to_x += connector.to_nudge

            halfway = (connector.to_x - connector.from_x) / 2
            connector.shaft_x = connector.from_x + halfway
            connector.shaft_x += connector.shaft_nudge

            half_row_height = self.row_height / 2
            connector.from_y = [row.y for row in rows if connector.from_row == row.key][0] + half_row_height
            connector.to_y = [row.y for row in rows if connector.to_row == row.key][0] + half_row_height

    def set_pipes(self):
        pipes = [item for item in self.items if item.type == 'pipe']
        for pipe in pipes:
            start_delta = pipe.date - self.settings.start
            start_delta_days = start_delta.days
            start_delta_pixels = start_delta_days * self.pixels_per_day
            pipe.x0 = start_delta_pixels
            pipe.y0 = self.first_row
            pipe.x1 = start_delta_pixels
            pipe.y1 = self.bottom_line

    def set_curtains(self):
        curtains = [item for item in self.items if item.type == 'curtain']
        for curtain in curtains:
            start_delta = curtain.start - self.settings.start
            finish_delta = curtain.finish - self.settings.start
            start_delta_days = start_delta.days
            finish_delta_days = finish_delta.days
            start_delta_pixels = start_delta_days * self.pixels_per_day
            finish_delta_pixels = finish_delta_days * self.pixels_per_day
            curtain.x = start_delta_pixels
            curtain.y = self.first_row
            curtain.width = finish_delta_pixels - start_delta_pixels
            curtain.height = self.bottom_line - self.first_row

    def set_separators(self):
        separators = [item for item in self.items if item.type == 'separator']
        rows = [item for item in self.items if item.type == 'row']
        for separator in separators:
            row_y = [row.y for row in rows if row.key == separator.row][0]
            row_bottom = row_y + self.row_height
            separator.x0 = self.settings.x
            separator.y0 = row_bottom
            separator.x1 = self.settings.width
            separator.y1 = row_bottom

    def set_sections(self):
        sections = [item for item in self.items if item.type == 'section']
        rows = [item for item in self.items if item.type == 'row']
        for section in sections:
            from_y = [row.y for row in rows if row.key == section.from_row][0]
            to_y = [row.y for row in rows if row.key == section.to_row][0]
            height = (to_y - from_y) + self.settings.row_height
            section.x = self.settings.x
            section.y = from_y
            section.width = self.settings.width
            section.height = height

    def set_notes(self):
        notes = [item for item in self.items if item.type == 'note']
        for note in notes:
            if not note.anchor:
                note.anchor = 'nw'
