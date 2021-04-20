#!/usr/bin/env python3

import logging

from tkinter import Canvas


class Drawing(Canvas):
    def __init__(self, parent, **data):
        super(Drawing, self).__init__(parent)

        self.parent = parent
        self.chart = data.get('chart')
        self.items = data.get('items')
        self.draw_chart()

    def draw_chart(self):
        self.draw_placeholder()
        self.pack()

    def draw_placeholder(self):
        width = 800
        height = 600
        self.config(width=width, height=height)
        self.create_rectangle(0, 0, width, height, fill="#ff0000")
        self.create_rectangle(0, 0, width // 2, height // 2, fill="#0000ff")
        self.create_rectangle(0, 0, width // 3, height // 3, fill="#00ff00")
        self.create_rectangle(0, 0, width // 4, height // 4, fill="#ff0000")

    # PRIMITIVES

    def draw_text(self):
        pass

    def draw_rectangle(self, x1, y1, x2, x3, **options):
        print(options)
        self.create_rectangle(x1, y1, x2, x3, options)

    def draw_diamond(self):
        pass

    def draw_circle(self):
        pass

    def draw_line(self):
        pass

    def draw_arrow(self):
        pass

    # SCALES

    def draw_scale(self):
        pass

    def draw_scales(self):
        pass

    def draw_period_label(self):
        pass

    def draw_period_labels(self):
        pass

    # ROWS

    def draw_row(self):
        pass

    def draw_row_name(self):
        pass

    def draw_rows(self):
        pass

    def draw_row_names(self):
        pass

    # TASKS

    def draw_task(self, start, finish, **options):
        pass

    def draw_tasks(self):
        pass

    def draw_task_name(self):
        pass

    def draw_task_names(self):
        pass

    # MILESTONES

    def draw_milestone(self):
        pass

    def draw_milestones(self):
        pass

    def draw_milestone_name(self):
        pass

    def draw_milestone_names(self):
        pass

    # RELATIONSHIPS

    def draw_relationship(self):
        pass

    def draw_relationships(self):
        pass

    # CURTAINS

    def draw_curtain(self):
        pass

    def draw_curtains(self):
        pass

    # BARS

    def draw_bar(self):
        pass

    def draw_bars(self):
        pass
