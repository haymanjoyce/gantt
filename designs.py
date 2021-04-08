#!/usr/bin/env python3

import datetime
import logging

from attr import attrs, attrib, Factory


@attrs
class Chart:

    name = attrib(default="chart")

    width = attrib(default=800)
    height = attrib(default=600)
    start = attrib(default=datetime.datetime.today())
    finish = attrib()

    @finish.default
    def default_finish(self):
        return self.start + datetime.timedelta(20)


@attrs
class Scale:

    name = attrib(default="scale")
    labels = attrib(default="")

    width = attrib(default=800)
    height = attrib(default=600)
    start = attrib(default=datetime.datetime.today())
    finish = attrib()
    _interval = attrib(default="days")

    @finish.default
    def finish(self):
        return self.start + datetime.timedelta(20)

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

    name = attrib(default="row")
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

    name = attrib(default="task")
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

    name = attrib(default="milestone")
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

    name = attrib(default="")
    labels = attrib(default="")

    source = attrib(default="")
    destination = attrib(default="")
    width = attrib(default="")
    color = attrib(default="")


@attrs
class Curtain:

    name = attrib(default="")
    labels = attrib(default="")

    start = attrib(default="")
    finish = attrib(default="")
    fill = attrib(default="")


@attrs
class Bar:

    name = attrib(default="")
    labels = attrib(default="")

    date = attrib(default="")
    color = attrib(default="")
    width = attrib(default="")

