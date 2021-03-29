#!/usr/bin/env python3

"""This module is for defining dataclasses."""

import datetime

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
    pass


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
