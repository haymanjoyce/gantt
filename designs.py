#!/usr/bin/env python3

import datetime
import logging
import math

from attr import attrs, attrib, Factory

import filing


DESIGNS = ('Scale', 'Row', 'Task', 'Milestone', 'Relationship', 'Curtain')  # excludes Chart


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


@attrs
class Scale:

    type = attrib(default="scale")
    labels = attrib(default="")
    width = attrib(default=800)
    _height = attrib(default=100)
    start = attrib(default=None)
    finish = attrib(default=None)
    _interval = attrib(default="days")
    rank = attrib(default=0)
    x = attrib(default=0)
    y = attrib(default=0)
    fill = attrib(default="red")
    border_color = attrib(default="black")
    _border_width = attrib(default=0.0)

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        value = str(value).lower()
        if value in ['days', 'day', 'd', '', 'none']:
            self._interval = 'DAYS'  # default interval
        elif value in ['weeks', 'week', 'wk', 'w']:
            self._interval = 'WEEKS'
        elif value in ['months', 'mon', 'month', 'm']:
            self._interval = 'MONTHS'
        elif value in ['quarters', 'quarts', 'qts', 'q']:
            self._interval = 'QUARTERS'
        elif value in ['halves', 'half', 'halfs', 'halve', 'h']:
            self._interval = 'HALVES'
        elif value in ['years', 'year', 'yrs', 'yr', 'y']:
            self._interval = 'YEARS'
        else:
            logging.error(f'Do not understand interval value, "{value}".')
            # raise ValueError(value)

    @property
    def border_width(self):
        return self._border_width

    @border_width.setter
    def border_width(self, value):
        """Outline width must be a bit less than half shortest rectangle dimension."""
        max_width = float(self.width) * 0.4
        max_height = float(self.height) * 0.4
        smallest = sorted([max_width, max_height])[0]
        if value > smallest:
            self._border_width = abs(int(smallest))
        else:
            self._border_width = abs(int(value))

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        """Must be high enough to accommodate outline and a bit of fill."""
        if value < 6:
            self._height = 6
        else:
            self._height = value


@attrs
class Row:

    type = attrib(default="row")
    labels = attrib(default="")
    row_number = attrib(default=0)
    height = attrib(default=20)
    fill = attrib(default="")
    text = attrib(default="")
    font_color = attrib(default="")
    font_size = attrib(default=10)
    font_style = attrib(default="")


@attrs
class Task:

    type = attrib(default="task")
    labels = attrib(default="")
    id = attrib(default=None)
    parent_row = attrib(default=None)
    start = attrib(default=None)
    finish = attrib(default=None)
    fill = attrib(default=None)
    text = attrib(default="")
    font_color = attrib(default="")
    font_size = attrib(default=10)
    font_style = attrib(default="")
    text_anchor = attrib(default="")
    text_align = attrib(default="")
    text_adjust = attrib(default="")
    bar_layer = attrib(default=None)
    text_layer = attrib(default=None)


@attrs
class Milestone:

    type = attrib(default="milestone")
    labels = attrib(default="")
    id = attrib(default=None)
    parent_row = attrib(default=None)
    date = attrib(default=None)
    fill = attrib(default=None)
    text = attrib(default="")
    font_color = attrib(default="")
    font_size = attrib(default=10)
    font_style = attrib(default="")
    text_anchor = attrib(default="")
    text_align = attrib(default="")
    text_adjust = attrib(default="")

    bar_layer = attrib(default=None)
    text_layer = attrib(default=None)


@attrs
class Relationship:

    type = attrib(default="relationship")
    labels = attrib(default="")
    source = attrib(default="")
    destination = attrib(default="")
    width = attrib(default="")
    color = attrib(default="")


@attrs
class Curtain:

    type = attrib(default="curtain")
    labels = attrib(default="")
    start = attrib(default="")
    finish = attrib(default="")
    fill = attrib(default="")


@attrs
class Bar:

    type = attrib(default="bar")
    labels = attrib(default="")
    date = attrib(default="")
    color = attrib(default="")
    width = attrib(default="")

