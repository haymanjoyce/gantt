#!/usr/bin/env python3

import logging

from attr import attrs, attrib


FEATURES = ('Scale', 'Row', 'Task', 'Milestone', 'Relationship', 'Curtain')


@attrs
class Scale:

    type = attrib(default="scale")
    labels = attrib(default="")
    rank = attrib(default=0)
    start = attrib(default=None)
    finish = attrib(default=None)
    x = attrib(default=0)
    y = attrib(default=0)
    width = attrib(default=800)
    height = attrib(default=100)
    fill = attrib(default="red")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)
    _interval = attrib(default="days")

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

