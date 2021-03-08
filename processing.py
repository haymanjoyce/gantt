#!/usr/bin/env python3

import loggers


class Processor:
    def __init__(self, xls):
        self.xls = xls

    def run(self):
        log.info("File processed.")
        return self.xls


cli = loggers.Stream()
log = loggers.File()
