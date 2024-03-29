#!/usr/bin/env python3

"""
This module enables feature data to be stored as dataclass objects.
Attributes should be vector graphic language agnostic.
"""

from attr import attrs, attrib


@attrs
class Scale:
    type = attrib(default="scale")
    layer = attrib(default=None)
    start = attrib(default=None)
    finish = attrib(default=None)
    interval = attrib(default="days")
    x = attrib(default=0)
    y = attrib(default=0)
    width = attrib(default=800)
    height = attrib(default=100)
    fill = attrib(default="red")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)
    element = attrib(default='')


@attrs
class Interval:
    type = attrib(default="interval")
    layer = attrib(default=1)
    date = attrib(default=None)
    x = attrib(default=0)
    y = attrib(default=0)
    width = attrib(default=800)
    height = attrib(default=100)
    fill = attrib(default="red")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)
    format = attrib(default="")
    element = attrib(default='')


@attrs
class Row:
    type = attrib(default="row")
    layer = attrib(default=None)
    key = attrib(default=0)
    x = attrib(default=0)
    y = attrib(default=0)
    width = attrib(default=800)
    height = attrib(default=20)
    fill = attrib(default="")
    border_color = attrib(default="grey")
    border_width = attrib(default=0.5)
    element = attrib(default='')


@attrs
class Bar:
    type = attrib(default="bar")
    layer = attrib(default=None)
    key = attrib(default=None)
    row = attrib(default=None)
    start = attrib(default=None)
    finish = attrib(default=None)
    width = attrib(default=40)
    height = attrib(default=10)
    x = attrib(default=None)
    y = attrib(default=None)
    nudge = attrib(default=None)
    fill = attrib(default=None)
    border_color = attrib(default="black")
    border_width = attrib(default=0.5)
    element = attrib(default='')


@attrs
class Label:
    type = attrib(default="label")
    layer = attrib(default=None)
    row = attrib(default=None)
    date = attrib(default=None)
    text = attrib(default=None)
    x = attrib(default=None)
    y = attrib(default=None)
    x_nudge = attrib(default=None)
    y_nudge = attrib(default=None)
    anchor = attrib(default=None)
    width = attrib(default=None)
    justify = attrib(default=None)
    rotation = attrib(default=None)
    font = attrib(default=None)
    color = attrib(default='black')
    size = attrib(default=12)
    bold = attrib(default=False)
    italic = attrib(default=False)
    underline = attrib(default=False)
    strikethrough = attrib(default=False)
    element = attrib(default='')


@attrs
class Connector:
    type = attrib(default="connector")
    layer = attrib(default=None)
    from_row = attrib(default=None)
    from_date = attrib(default=None)
    from_nudge = attrib(default=None)
    to_row = attrib(default=None)
    to_date = attrib(default=None)
    to_nudge = attrib(default=None)
    arrow_head = attrib(default=None)
    shaft_nudge = attrib(default=None)
    from_x = attrib(default=None)
    from_y = attrib(default=None)
    to_x = attrib(default=None)
    to_y = attrib(default=None)
    shaft_x = attrib(default=None)
    width = attrib(default=0.0)
    color = attrib(default="black")
    element = attrib(default='')


@attrs
class Pipe:
    type = attrib(default="pipe")
    layer = attrib(default=1)
    date = attrib(default=None)
    width = attrib(default=1)
    color = attrib(default='black')
    x0 = attrib(default=0)
    y0 = attrib(default=0)
    x1 = attrib(default=0)
    y1 = attrib(default=0)
    element = attrib(default='')


@attrs
class Curtain:
    type = attrib(default="curtain")
    layer = attrib(default=None)
    start = attrib(default="")
    finish = attrib(default="")
    color = attrib(default="")
    x = attrib(default=None)
    y = attrib(default=None)
    width = attrib(default=None)
    height = attrib(default=None)
    element = attrib(default='')


@attrs
class Separator:
    type = attrib(default="separator")
    row = attrib(default=None)
    layer = attrib(default=1)
    width = attrib(default=1)
    color = attrib(default='black')
    x0 = attrib(default=0)
    y0 = attrib(default=0)
    x1 = attrib(default=0)
    y1 = attrib(default=0)
    element = attrib(default='')


@attrs
class Section:
    type = attrib(default="section")
    layer = attrib(default=1)
    from_row = attrib(default=1)
    to_row = attrib(default=1)
    color = attrib(default='')
    border_color = attrib(default='')
    border_width = attrib(default=0)
    x = attrib(default=None)
    y = attrib(default=None)
    width = attrib(default=None)
    height = attrib(default=None)
    element = attrib(default='')


@attrs
class Box:
    type = attrib(default="box")
    layer = attrib(default=1)
    fill_color = attrib(default='')
    border_color = attrib(default='black')
    border_width = attrib(default=1)
    x = attrib(default=None)
    y = attrib(default=None)
    width = attrib(default=None)
    height = attrib(default=None)
    element = attrib(default='')


@attrs
class Note:
    type = attrib(default="note")
    layer = attrib(default=None)
    text = attrib(default=None)
    x = attrib(default=None)
    y = attrib(default=None)
    anchor = attrib(default=None)
    width = attrib(default=None)
    justify = attrib(default='')
    rotation = attrib(default=None)
    font = attrib(default=None)
    color = attrib(default='black')
    size = attrib(default=12)
    bold = attrib(default=False)
    italic = attrib(default=False)
    underline = attrib(default=False)
    strikethrough = attrib(default=False)
    element = attrib(default='')


@attrs
class Task:
    pass


@attrs
class Relationship:
    type = attrib(default="relationship")
    layer = attrib(default=None)
    key = attrib(default=None)
    source = attrib(default="")
    destination = attrib(default="")
    width = attrib(default="")
    color = attrib(default="")
    element = attrib(default='')
