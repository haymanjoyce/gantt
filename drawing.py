#!/usr/bin/env python3

import logging

from tkinter import Canvas

from filing import get_config_data

from settings import Settings


class Drawing(Canvas):
    def __init__(self, parent, data):
        super(Drawing, self).__init__(parent)

        self.parent = parent
        self.items = data
        self.settings = Settings()
        self.draw_chart()

    def draw_chart(self):
        settings = get_config_data()
        self.config(width=self.settings.width, height=self.settings.height, background="#eee")
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

        # value = abs(int(value))  # ensure value is a positive integer
        # even_border_width = math.ceil(value / 2) * 2  # for tidy rendering we need even numbers
        # available_width = self.width - (even_border_width * 2)
        # available_height = self.height - (even_border_width * 2)
        # available_space = sorted([available_width, available_height])[0]
        # if even_border_width >= available_space:
        #     even_border_width = math.ceil(available_space / 2) * 2
        # if value < 1:  # under 1 treated as zero but outline still visible when 0 so hidden with fill color
        #     self._border_width = 2
        #     self.x += 1
        #     self.y += 1
        #     self.x0 = self.x + self.width - 2
        #     self.y0 = self.y + self.height - 2
        #     self.border_color = self.fill
        # else:
        #     self._border_width = even_border_width
        #     self.x += even_border_width / 2
        #     self.y += even_border_width / 2
        #     self.x0 = self.x + self.width - even_border_width
        #     self.y0 = self.y + self.height - even_border_width

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
