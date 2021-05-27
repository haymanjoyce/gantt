#!/usr/bin/env python3

import logging
from datetime import datetime

from settings import Settings


class Cleaner:
    def __init__(self, data):
        self.items = data
        self.settings = Settings()
        self.clean_items()

    def clean_items(self):
        for item in self.items:
            if hasattr(item, 'start'):
                self.clean_start_value(item)
            if hasattr(item, 'finish'):
                self.clean_finish_value(item)
            if hasattr(item, 'row'):
                self.clean_row_value(item)
            if hasattr(item, 'layer'):
                self.clean_layer_value(item)

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
