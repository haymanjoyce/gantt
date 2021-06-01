#!/usr/bin/env python3

"""This module is for cleaning data class attribute values."""

import logging
from datetime import datetime
from tkinter import LEFT, RIGHT, CENTER

from settings import Settings


class Cleaner:
    def __init__(self, data):
        self.items = data
        self.settings = Settings()
        self.clean_items()

    def clean_items(self):
        for item in self.items:
            if hasattr(item, 'interval'):
                self.clean_interval_value(item)
            if hasattr(item, 'start'):
                self.clean_start_value(item)
            if hasattr(item, 'finish'):
                self.clean_finish_value(item)
            if hasattr(item, 'row'):
                self.clean_row_value(item)
            if hasattr(item, 'layer'):
                self.clean_layer_value(item)
            if hasattr(item, 'justify'):
                self.clean_justify_value(item)

    @staticmethod
    def clean_interval_value(item):
        value = str(item.interval).strip().lower()
        if value in ['days', 'day', 'd', '', 'none']:
            item.interval = 'DAYS'  # default interval
        elif value in ['weeks', 'week', 'wk', 'w']:
            item.interval = 'WEEKS'
        elif value in ['months', 'mon', 'month', 'm']:
            item.interval = 'MONTHS'
        elif value in ['quarters', 'quarts', 'qts', 'q']:
            item.interval = 'QUARTERS'
        elif value in ['halves', 'half', 'halfs', 'halve', 'h']:
            item.interval = 'HALVES'
        elif value in ['years', 'year', 'yrs', 'yr', 'y']:
            item.interval = 'YEARS'
        else:
            logging.info(f'INTERVAL value in {item.type.upper()}S not recognised.')
            item.interval = 'DAYS'

    def clean_start_value(self, item):
        if not isinstance(item.start, datetime.today().__class__):
            item.start = self.settings.start
        if item.start < self.settings.start:
            item.start = self.settings.start
        if item.start > self.settings.finish:
            item.start = self.settings.finish

    def clean_finish_value(self, item):
        if not isinstance(item.finish, datetime.today().__class__):
            item.finish = self.settings.finish
        if item.finish < self.settings.start:
            item.finish = self.settings.start
        if item.finish > self.settings.finish:
            item.finish = self.settings.finish

    @staticmethod
    def clean_row_value(item):
        if not item.row:
            item.row = 1

    @staticmethod
    def clean_layer_value(item):
        if not item.layer:
            item.layer = 1

    @staticmethod
    def clean_justify_value(item):
        value = str(item.justify).upper().strip()
        if not value:
            item.justify = LEFT
        elif value in ['L', 'LT', 'LF', 'LFT', 'LEFT']:
            item.justify = LEFT
        elif value in ['R', 'RT', 'RGHT', 'RIGHT']:
            item.justify = RIGHT
        elif value in ['C', 'CT', 'CR', 'CTR', 'CNTR', 'CENTR', 'CENTER', 'CENTRE', 'M', 'MID', 'MIDL', 'MIDDLE']:
            item.justify = CENTER
        else:
            logging.info(f'JUSTIFY value in {item.type.upper()}S not recognised.')
            item.justify = LEFT
