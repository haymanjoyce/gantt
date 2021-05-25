#!/usr/bin/env python3

import logging


def clean_interval_fields(items):
    scales = [item for item in items if item.type == 'scale']
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
            logging.error(f'Do not understand interval value, "{value}".')
            # raise ValueError(value)
    return items
