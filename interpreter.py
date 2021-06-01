#!/usr/bin/env python3

"""This module is for interpreting attribute values provided by the user."""

import logging


class Interpreter:
    def __init__(self, data):
        self.items = data
        self.interpret_intervals()

    def interpret_intervals(self):
        scales = [item for item in self.items if item.type == 'scale']
        for scale in scales:
            value = str(scale.interval).lower()
            if value in ['days', 'day', 'd', '', 'none']:
                scale.interval = 'DAYS'  # default interval
            elif value in ['weeks', 'week', 'wk', 'w']:
                scale.interval = 'WEEKS'
            elif value in ['months', 'mon', 'month', 'm']:
                scale.interval = 'MONTHS'
            elif value in ['quarters', 'quarts', 'qts', 'q']:
                scale.interval = 'QUARTERS'
            elif value in ['halves', 'half', 'halfs', 'halve', 'h']:
                scale.interval = 'HALVES'
            elif value in ['years', 'year', 'yrs', 'yr', 'y']:
                scale.interval = 'YEARS'
            else:
                logging.error(f'Cannot interpret interval value, "{value}".')
                # raise ValueError(value)
