#!/usr/bin/env python3

import logging


class Workbook:
    """Extra methods for Openpyxl workbook objects.  Unable to extend class."""
    def __init__(self, workbook):

        self.workbook = workbook

    def check_merged_cells(self):
        for sheet_name in self.workbook.sheet_names:
            if bool(self.workbook[sheet_name].merged_cells.ranges):
                logging.error(f"Merged cells found in {sheet_name} sheet.")

    def check_headers_row_exists(self):
        pass

    def check_headers_exist(self):
        pass

    def run_all_checks(self):
        self.check_merged_cells()
