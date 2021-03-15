#!/usr/bin/env python3

import loggers
import utils


class Cleaner:
    def __init__(self, workbook):

        self.workbook = workbook
        self.sheet_names = self.workbook.get_sheet_names()

    def print_active_sheet(self):
        print(self.workbook.active)

    def run(self):
        self.print_active_sheet()
        return self.workbook


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))

