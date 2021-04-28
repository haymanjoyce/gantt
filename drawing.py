#!/usr/bin/env python3

import logging

from tkinter import Canvas


class Drawing(Canvas):
    def __init__(self, parent, **data):
        super(Drawing, self).__init__(parent)

        self.parent = parent
        self.chart = data.get('chart')
        self.items = data.get('features')
        self.draw_chart()

    def draw_chart(self):
        self.config(width=self.chart.width, height=self.chart.height, background="#eee")
        self.pack()
        self.draw_scales()

    # PRIMITIVES

    def draw_text(self):
        pass

    def draw_rectangle(self, x, y, rect_width, rect_height, **options):  # parameter "width" reserved for defining border width
        border_width = options.get('width')
        half_border_width = border_width / 2
        x = x + half_border_width
        y = y + half_border_width
        x1 = x + rect_width - border_width
        y1 = y + rect_height - border_width
        self.create_rectangle(x, y, x1, y1, options)

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
        self.draw_rectangle(item.x, item.y, item.width, item.height, fill=item.fill, outline=item.border_color, width=item.border_width)

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
