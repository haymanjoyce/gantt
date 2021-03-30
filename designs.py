#!/usr/bin/env python3

"""This module is for defining dataclasses."""

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

    name = attrib(default=None)
    labels = attrib(default="scale")
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
    pass


@attrs
class Task:
    pass


@attrs
class Milestone:
    pass


@attrs
class Relationship:
    pass


@attrs
class Curtain:
    pass


@attrs
class Bar:
    pass
