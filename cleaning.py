#!/usr/bin/env python3

import loggers
import utils


class Cleaner:
    def __init__(self, workbook):

        self.workbook = workbook
        self.sheet_names = self.workbook.get_sheet_names()

    def clean_something(self):
        print("I am cleaning!")

    def run(self):
        self.clean_something()
        return self.workbook


cli = loggers.Widget()
log = loggers.File(utils.get_path("data.log"))

