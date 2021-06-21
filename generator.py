#!/usr/bin/env python3

"""This module is for generating SVG from dataclass objects."""

import logging
import datetime

from operator import itemgetter, attrgetter
from pprint import pprint as pp

from settings import Settings
from shapes import Rectangle


class Generator:
    def __init__(self, items):
        self.items = items
        self.settings = Settings()
        self.generate_elements()

    def generate_elements(self):
        items = [item for item in self.items]
        for item in items:
            self.generate_element(item)
        items.sort(key=attrgetter('layer'))
        pp(items)

    def generate_element(self, item):
        if item.type == 'interval':
            item.element = Rectangle(x=item.x, y=item.y, width=item.width, height=item.height)
        else:
            item.element = ''
