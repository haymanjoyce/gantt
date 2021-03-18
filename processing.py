#!/usr/bin/env python3

import logging
import utils


class Processor:
    def __init__(self, workbook):

        self.workbook = workbook
        self.sheet_names = self.workbook.get_sheet_names()

    def process_something(self):
        print("I am processing!")

    def run(self):
        self.process_something()
        return self.workbook
