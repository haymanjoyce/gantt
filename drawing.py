#!/usr/bin/env python3

import logging
import datetime

from tkinter import Canvas

from settings import Settings


class Drawing(Canvas):
    def __init__(self, parent, data):
        super(Drawing, self).__init__(parent)

        self.parent = parent
        self.items = data
        self.settings = Settings()
        self.config(width=self.settings.width, height=self.settings.height, background="#fff")
        self.pack()
        self.time_delta = (self.settings.finish - self.settings.start)
        self.total_days = self.time_delta.days + 1  # range inclusive of end dates
        self.pixels_per_day = self.settings.width / self.total_days
        self.first_row = self.draw_scales()  # y for first row
        self.remaining_space = self.settings.height - self.first_row
        self.max_row_height = self.remaining_space / self.settings.num_rows
        self.row_height = self.cap_row_height()
        self.row_locations = self.draw_rows()
        self.tasks = self.load_task_locations()
        self.draw_tasks()
        print(self.tasks)

    # SHAPES

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
        y = self.settings.y
        for item in items:
            item.y = y
            self.draw_scale(item)
            y += item.height
        return y

    def draw_scale(self, item):
        common_options = {'fill': item.fill, 'outline': item.border_color, 'width': item.border_width}
        common_tag = "scale_text"
        if item.interval == 'DAYS':
            self.draw_days(item, common_options, common_tag)
        elif item.interval == 'MONTHS':
            self.draw_months(item, common_options, common_tag)
        elif item.interval == 'YEARS':
            self.draw_years(item, common_options, common_tag)
        else:
            raise ValueError(item.interval)
        self.tag_raise(common_tag)  # raises all scale text above rectangles

    def draw_days(self, item, options, tag):
        current_date = item.start
        x = item.x
        height_offset = item.height / 2
        for day in range(1, self.total_days + 1):  # indexed from 1
            self.draw_rectangle(x, item.y, self.pixels_per_day, item.height, **options)
            text_y = item.y + height_offset
            label = current_date.strftime("%d")
            self.create_text(x, text_y, text=label, anchor="w", tag=tag)
            x += self.pixels_per_day
            current_date += datetime.timedelta(days=1)

    def draw_months(self, item, options, tag):
        current_date = item.start
        current_month = item.start
        days_in_month = 0
        x = item.x
        height_offset = item.height / 2
        for day in range(1, self.total_days + 1):  # indexed from 1
            if current_month.month == current_date.month:
                days_in_month += 1
            else:
                month_width = days_in_month * self.pixels_per_day
                self.draw_rectangle(x, item.y, month_width, item.height, **options)
                text_y = item.y + height_offset
                label = current_month.strftime("%m")
                self.create_text(x, text_y, text=label, anchor="w", tag=tag)
                x += days_in_month * self.pixels_per_day
                current_month = current_date
                days_in_month = 1  # we start at one to capture first iteration
            current_date += datetime.timedelta(days=1)

    def draw_years(self, item, options, tag):
        current_date = item.start
        current_year = item.start
        days_in_year = 0
        x = item.x
        height_offset = item.height / 2
        for day in range(1, self.total_days + 1):  # indexed from 1
            if current_year.year == current_date.year:
                days_in_year += 1
            else:
                year_width = days_in_year * self.pixels_per_day
                self.draw_rectangle(x, item.y, year_width, item.height, **options)
                text_y = item.y + height_offset
                label = current_year.strftime("%y")
                self.create_text(x, text_y, text=label, anchor="w", tag=tag)
                x += days_in_year * self.pixels_per_day
                current_year = current_date
                days_in_year = 1
            current_date += datetime.timedelta(days=1)

    # ROWS

    def cap_row_height(self):
        if self.settings.row_height > self.max_row_height:
            return self.max_row_height
        else:
            return self.settings.row_height

    def draw_rows(self):
        y = self.first_row
        count = 1
        row_locations = dict()
        for row in range(0, self.settings.num_rows):
            if self.settings.show_rows:
                self.draw_row(y)
            if self.settings.show_row_nums:
                self.draw_row_num(y, count)
            row_locations.setdefault(count, y)
            y += self.row_height
            count += 1
        return row_locations

    def draw_row(self, y):
        options = {'outline': 'grey', 'width': 0.5}
        self.draw_rectangle(self.settings.x, y, self.settings.width, self.row_height, **options)

    def draw_row_num(self, y, label):
        x = self.settings.x + 30
        offset = self.row_height / 2
        y += offset
        self.create_text(x, y, text=label, anchor="e")

    # TASKS

    def load_task_locations(self):
        tasks = [item for item in self.items if item.type == 'task']
        for task in tasks:
            if task.row in self.row_locations.keys():
                task.y = self.row_locations[task.row]
        return tasks

    def draw_tasks(self):
        pass

    def draw_task(self, start, finish, **options):
        pass

    def draw_task_names(self):
        pass

    def draw_task_name(self):
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

    # GROUPS

    def draw_groups(self):
        pass
