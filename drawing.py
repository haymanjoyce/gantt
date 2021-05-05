#!/usr/bin/env python3

import logging
import math
import datetime

from tkinter import Canvas

from filing import get_config_data

from settings import Settings


class Drawing(Canvas):
    def __init__(self, parent, data):
        super(Drawing, self).__init__(parent)

        self.parent = parent
        self.items = data
        self.settings = Settings()
        self.config(width=self.settings.width, height=self.settings.height, background="#eee")
        self.pack()
        self.time_delta = (self.settings.finish - self.settings.start)
        self.total_days = self.time_delta.days + 1  # range inclusive of end dates
        self.pixels_per_day = self.settings.width / self.total_days
        self.draw_scales()

    # SHAPES

    def draw_text(self):
        pass

    def draw_rectangle(self, x, y, rect_width, rect_height, **options):
        x1 = x
        y1 = y
        x2 = x + rect_width
        y2 = y + rect_height
        self.create_rectangle(x1, y1, x2, y2, options)

    def draw_diamond(self):
        pass

    def draw_circle(self):
        pass

    def draw_line(self):
        pass

    def draw_arrow(self):
        pass

    # SCALES

    def draw_scales(self):
        items = [item for item in self.items if item.type == 'scale']
        # items.sort(key=lambda item: item.rank, reverse=True)
        for item in items:
            self.draw_scale(item)

    def draw_scale(self, item):
        options = {'fill': item.fill, 'outline': item.border_color, 'width': item.border_width}

        current_date = item.start

        current_day = current_date.day
        current_month = current_date.month
        current_year = current_date.year

        days_in_month = 0
        days_in_year = 0

        day_x = item.x
        month_x = item.x
        year_x = item.x

        for day in range(1, self.total_days + 1):  # indexed from 1

            if item.interval == 'DAYS':
                self.draw_rectangle(day_x, item.y, self.pixels_per_day, item.height, **options)
                day_x += self.pixels_per_day

            elif item.interval == 'MONTHS':
                if current_month == current_date.month:
                    days_in_month += 1
                else:
                    month_width = days_in_month * self.pixels_per_day
                    self.draw_rectangle(month_x, item.y, month_width, item.height, **options)
                    month_x += days_in_month * self.pixels_per_day
                    current_month = current_date.month
                    days_in_month = 1  # we start at one to capture first iteration

            elif item.interval == 'YEARS':
                if current_year == current_date.year:
                    days_in_year += 1
                else:
                    print(days_in_year)
                    year_width = days_in_year * self.pixels_per_day
                    self.draw_rectangle(year_x, item.y, year_width, item.height, **options)
                    year_x += days_in_year * self.pixels_per_day
                    current_year = current_date.year
                    days_in_year = 1

            else:
                raise ValueError(item.interval)

            current_date += datetime.timedelta(days=1)

    def draw_period_labels(self):
        pass

    def draw_period_label(self):
        pass

    # ROWS

    def draw_rows(self):
        pass

    def draw_row(self):
        pass

    def draw_row_names(self):
        pass

    def draw_row_name(self):
        pass

    # TASKS

    def draw_tasks(self):
        pass

    def draw_task(self, start, finish, **options):
        pass

    def draw_task_names(self):
        pass

    def draw_task_name(self):
        pass

    # MILESTONES

    def draw_milestones(self):
        pass

    def draw_milestone(self):
        pass

    def draw_milestone_names(self):
        pass

    def draw_milestone_name(self):
        pass

    # RELATIONSHIPS

    def draw_relationships(self):
        pass

    def draw_relationship(self):
        pass

    # CURTAINS

    def draw_curtains(self):
        pass

    def draw_curtain(self):
        pass

    # BARS

    def draw_bars(self):
        pass

    def draw_bar(self):
        pass
