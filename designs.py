#!/usr/bin/env python3

import datetime
import logging

from attr import attrs, attrib, Factory


@attrs
class Chart:

    type = attrib(default="chart")
    width = attrib(default=800)
    height = attrib(default=600)
    start = attrib(default=datetime.datetime.today())
    finish = attrib()

    @finish.default
    def default_finish(self):
        return self.start + datetime.timedelta(20)


@attrs
class Scale:

    type = attrib(default="scale")
    labels = attrib(default="")
    width = attrib(default=800)
    height = attrib(default=100)
    start = attrib(default=datetime.datetime.today())
    _finish = attrib(default=None)
    _interval = attrib(default="days")

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, value):
        if value:
            self.finish = value
        else:
            self._finish = self.start + datetime.timedelta(20)

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value):
        value = str(value).lower()
        if value in ['days', 'day', 'd', '']:
            self._interval = 'DAYS'
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

