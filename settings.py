#!/usr/bin/env python3

import datetime

from attr import attrs, attrib, Factory

import filing


@attrs
class Settings:

    config_data = attrib(default=Factory(filing.get_config_data))
    x = attrib()
    y = attrib()
    width = attrib()
    height = attrib()
    start = attrib()
    finish = attrib()
    num_rows = attrib()
    row_height = attrib()
    show_rows = attrib()
    show_row_nums = attrib()

    @x.default
    def default_x(self):
        return 0

    @y.default
    def default_y(self):
        return 0

    @width.default
    def default_width(self):
        if self.config_data.get('width'):
            return int(self.config_data['width'])
        else:
            return 800

    @height.default
    def default_height(self):
        if self.config_data.get('height'):
            return int(self.config_data['height'])
        else:
            return 600

    @start.default
    def default_start(self):
        if self.config_data.get('start'):
            return datetime.datetime.strptime(self.config_data['start'], '%Y/%m/%d')
        else:
            return datetime.datetime.today()

    @finish.default
    def default_finish(self):
        if self.config_data.get('finish'):
            return datetime.datetime.strptime(self.config_data['finish'], '%Y/%m/%d')
        else:
            return self.start + datetime.timedelta(20)

    @num_rows.default
    def default_num_rows(self):
        if self.config_data.get('num_rows'):
            return int(self.config_data.get('num_rows'))
        else:
            return 1

    @row_height.default
    def default_row_height(self):
        if self.config_data.get('row_height'):
            return int(self.config_data.get('row_height'))
        else:
            return 10

    @show_rows.default
    def default_show_rows(self):
        if self.config_data.get('show_rows'):
            return bool(self.config_data.get('show_rows'))
        else:
            return False

    @show_row_nums.default
    def default_show_row_nums(self):
        if self.config_data.get('show_row_nums'):
            return bool(self.config_data.get('show_row_nums'))
        else:
            return False
