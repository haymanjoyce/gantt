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
    rows = attrib()
    show_rows = attrib()

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

    @rows.default
    def default_rows(self):
        if self.config_data.get('rows'):
            return int(self.config_data.get('rows'))
        else:
            return 1

    @show_rows.default
    def default_show_rows(self):
        if self.config_data.get('show_rows'):
            return bool(self.config_data.get('show_rows'))
        else:
            return False
