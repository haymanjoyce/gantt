#!/usr/bin/env python3

import logging
import utils


class Checker:
    def __init__(self, workbook):

        self.workbook = workbook
        self.sheet_names = self.workbook.get_sheet_names()

    def check_merged_cells(self):
        for sheet_name in self.sheet_names:
            if bool(self.workbook[sheet_name].merged_cells.ranges):
                logging.error(f"Merged cells found in {sheet_name} sheet.")

    def run(self):
        self.check_merged_cells()
        return self.workbook
