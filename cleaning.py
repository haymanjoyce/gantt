#!/usr/bin/env python3

import logging
import utils


class Cleaner:
    def __init__(self, workbook):

        self.workbook = workbook
        self.sheet_names = self.workbook.get_sheet_names()

    def clean_something(self):
        pass

    def run(self):
        self.clean_something()
        return self.workbook

