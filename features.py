#!/usr/bin/env python3

import logging

from attr import attrs, attrib


@attrs
class Scale:

    type = attrib(default="scale")
    tags = attrib(default="")
    sheet_row = attrib(default="")
    layer = attrib(default=None)
    key = attrib(default=0)

    order = attrib(default=0)

    start = attrib(default=None)
    finish = attrib(default=None)
    _interval = attrib(default="days")

    x = attrib(default=0)
    y = attrib(default=0)

    width = attrib(default=800)
    height = attrib(default=100)

    fill = attrib(default="red")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)

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
    tags = attrib(default="")
    sheet_row = attrib(default=0)
    layer = attrib(default=None)
    key = attrib(default=0)

    height = attrib(default=20)
    fill = attrib(default="")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)


@attrs
class Bar:

    type = attrib(default="bar")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    row = attrib(default=None)
    start = attrib(default=None)
    finish = attrib(default=None)
    height = attrib(default=None)
    adjust = attrib(default=None)

    x = attrib(default=None)
    y = attrib(default=None)

    fill = attrib(default=None)
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)


@attrs
class Label:

    type = attrib(default="label")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    row = attrib(default=None)
    date = attrib(default=None)

    x = attrib(default=None)
    y = attrib(default=None)

    text = attrib(default="")

    x_nudge = attrib(default="")
    y_nudge = attrib(default="")

    color = attrib(default="")
    size = attrib(default=10)
    style = attrib(default="")
    weight = attrib(default="")

    anchor = attrib(default="")

    rotation = attrib(default="")

    width = attrib(default="")
    alignment = attrib(default="")


@attrs
class Connector:

    type = attrib(default="connector")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    from_row = attrib(default=None)
    from_date = attrib(default=None)
    from_adjust = attrib(default=None)
    from_arrow = attrib(default=None)

    to_row = attrib(default=None)
    to_date = attrib(default=None)
    to_adjust = attrib(default=None)
    to_arrow = attrib(default=None)

    from_x = attrib(default=None)
    from_y = attrib(default=None)
    to_x = attrib(default=None)
    to_y = attrib(default=None)

    width = attrib(default=0.0)
    color = attrib(default="black")


@attrs
class Pipe:

    type = attrib(default="bar")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    date = attrib(default="")

    width = attrib(default="")
    color = attrib(default="")


@attrs
class Line:
    pass


@attrs
class Curtain:

    type = attrib(default="curtain")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    start = attrib(default="")
    finish = attrib(default="")

    fill = attrib(default="")


@attrs
class Group:

    type = attrib(default="group")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    from_row = attrib(default=None)
    to_row = attrib(default=None)

    fill = attrib(default="")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)


@attrs
class Box:

    type = attrib(default="box")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    x = attrib(default=None)
    y = attrib(default=None)

    width = attrib(default=None)
    height = attrib(default=None)

    fill = attrib(default="")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)


@attrs
class Task:
    pass


@attrs
class Relationship:

    type = attrib(default="relationship")
    tags = attrib(default="")
    sheet_row = attrib(default=None)
    layer = attrib(default=None)
    key = attrib(default=None)

    source = attrib(default="")
    destination = attrib(default="")

    width = attrib(default="")
    color = attrib(default="")
