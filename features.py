#!/usr/bin/env python3

import logging

from attr import attrs, attrib


@attrs
class Scale:

    type = attrib(default="scale")
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


@attrs
class Interval:

    type = attrib(default="interval")
    date = attrib(default=None)
    x = attrib(default=0)
    y = attrib(default=0)
    width = attrib(default=800)
    height = attrib(default=100)
    fill = attrib(default="red")
    border_color = attrib(default="black")
    border_width = attrib(default=0.0)
    format = attrib(default="")


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


@attrs
class Label:

    type = attrib(default="label")
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
    layer = attrib(default=None)
    key = attrib(default=None)
    start = attrib(default="")
    finish = attrib(default="")
    fill = attrib(default="")


@attrs
class Group:

    type = attrib(default="group")
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
    layer = attrib(default=None)
    key = attrib(default=None)
    source = attrib(default="")
    destination = attrib(default="")
    width = attrib(default="")
    color = attrib(default="")
