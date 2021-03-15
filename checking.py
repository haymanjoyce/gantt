#!/usr/bin/env python3

import loggers
import utils
from openpyxl import load_workbook


class Checker:
    def __init__(self, filename):

        self.workbook = load_workbook(filename)
        self.sheet_names = self.workbook.get_sheet_names()
        self.run()

    def check_merged_cells(self):
        for sheet_name in self.sheet_names:
            if bool(self.workbook[sheet_name].merged_cells.ranges):
                print("Merged cells found.")

    def run(self):
        self.check_merged_cells()
        log.info("File checked.")


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))
