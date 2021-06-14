#!/usr/bin/env python3

"""This module is for generating SVG from dataclass objects."""

import logging
import datetime

from operator import itemgetter

from settings import Settings
from shapes import Rectangle


class Generator:
    def __init__(self, items):
        self.items = items
        self.settings = Settings()
        self.elements = []
        self.svg = ""
        self.draw_elements()
        print(self.elements)

    def draw_elements(self):
        intervals = [item for item in self.items if item.type == 'interval']
        for item in intervals:
            self.draw_element(item)
        self.elements.sort(key=itemgetter(0))

    def draw_element(self, item):
        if item.type == 'interval':
            element = Rectangle(x=item.x, y=item.y, width=item.width, height=item.height)
        else:
            element = ''
        if hasattr(item, 'layer'):
            if item.layer:
                layer = item.layer
            else:
                layer = 1
        else:
            layer = 1
        self.elements += (layer, element),
