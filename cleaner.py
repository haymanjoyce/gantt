#!/usr/bin/env python3

"""This module is for cleaning data class fields."""

import logging
from datetime import datetime
from tkinter import LEFT, RIGHT, CENTER

from settings import Settings

SETTINGS = Settings()


class Cleaner:
    def __init__(self, data):
        self.items = data
        self.assignments = {
            'interval': self.clean_interval_value,
            'start': self.clean_start_value,
            'finish': self.clean_finish_value,
            'row': self.clean_row_value,
            'layer': self.clean_layer_value,
            'justify': self.clean_justify_value,
        }
        self.clean_items()

    def clean_items(self):
        for item in self.items:
            for field, cleaner in self.assignments.items():
                if hasattr(item, field):
                    cleaner(item)

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

    @staticmethod
    def clean_start_value(item):
        if not isinstance(item.start, datetime.today().__class__):
            item.start = SETTINGS.start
        if item.start < SETTINGS.start:
            item.start = SETTINGS.start
        if item.start > SETTINGS.finish:
            item.start = SETTINGS.finish

    @staticmethod
    def clean_finish_value(item):
        if not isinstance(item.finish, datetime.today().__class__):
            item.finish = SETTINGS.finish
        if item.finish < SETTINGS.start:
            item.finish = SETTINGS.start
        if item.finish > SETTINGS.finish:
            item.finish = SETTINGS.finish

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
