#!/usr/bin/env python3

import logging

from settings import Settings

from features import Row


class Processing:
    def __init__(self, data):
        self.items = data
        self.settings = Settings()
        self.time_delta = (self.settings.finish - self.settings.start)
        self.total_days = self.time_delta.days + 1  # range inclusive of end dates
        self.pixels_per_day = self.settings.width / self.total_days
        self.first_row = self.set_scales()
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

    def get_row_height(self):
        row_space = self.settings.height - self.first_row
        max_height = row_space / self.settings.num_rows
        if self.settings.row_height > max_height:
            return max_height
        else:
            return self.settings.row_height

    def set_rows(self):
        height = self.get_row_height()
        y = self.first_row
        for i in range(0, self.settings.num_rows):
            row = Row()
            row.key = i + 1
            row.x = self.settings.x
            row.y = y
            row.width = self.settings.width
            row.height = height
            y += height

    def set_bars(self):
        bars = [item for item in self.items if item.type == 'bar']
        for bar in bars:
            # some of this might be better placed in cleaning
            if not isinstance(bar.start, self.settings.start.__class__):
                bar.start = self.settings.start
            if not isinstance(bar.finish, self.settings.start.__class__):
                bar.finish = self.settings.start
            if not int(bar.row):
                bar.row = 1
            if bar.start < self.settings.start:
                bar.start = self.settings.start
            if bar.start > self.settings.finish:
                bar.finish = self.settings.finish
            if bar.finish < self.settings.start:
                bar.finish = self.settings.start
            if bar.finish > self.settings.finish:
                bar.finish = self.settings.finish
        # factor in height
        # factor in nudge
        # x
        # y




    #
    # def load_task_locations(self):
    #     tasks = [item for item in self.items if item.type == 'task']
    #     unhomed = 0
    #     for task in tasks:
    #         if task.row in self.row_locations.keys():
    #             task.y = self.row_locations[task.row]
    #         else:
    #             task.y = self.first_row
    #             unhomed += 1
    #     if unhomed:
    #         logging.warning(f"{unhomed} unhomed task(s) assigned to first row.")
    #     return tasks
    #
    # def draw_tasks(self):
    #     for task in self.tasks:
    #         # args = (0, task.y, 100, self.row_height)
    #         self.draw_rectangle(0, task.y, 100, self.row_height, fill='red', tag='tasks')
    #     self.tag_lower('tasks')