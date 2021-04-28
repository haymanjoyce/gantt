#!/usr/bin/env python3

import logging
import datetime

from attr import attrs, attrib, Factory

import filing


@attrs
class Chart:

    type = attrib(default="chart")
    settings = attrib(default=Factory(filing.get_config_data))
    x = attrib()
    y = attrib()
    width = attrib()
    height = attrib()
    start = attrib()
    finish = attrib()

    @x.default
    def default_x(self):
        return 0

    @y.default
    def default_y(self):
        return 0

    @width.default
    def default_width(self):
        if self.settings.get('width'):
            return int(self.settings['width'])
        else:
            return 800

    @height.default
    def default_height(self):
        if self.settings.get('height'):
            return int(self.settings['height'])
        else:
            return 600

    @start.default
    def default_start(self):
        if self.settings.get('start'):
            return datetime.datetime.strptime(self.settings['start'], '%Y/%m/%d')
        else:
            return datetime.datetime.today()

    @finish.default
    def default_finish(self):
        if self.settings.get('finish'):
            return datetime.datetime.strptime(self.settings['finish'], '%Y/%m/%d')
        else:
            return self.start + datetime.timedelta(20)
