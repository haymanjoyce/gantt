#!/usr/bin/env python3

import loggers


class Processor:
    def __init__(self, df):
        self.df = df

    def run(self):
        log.info("File processed.")
        return self.df


cli = loggers.Stream()
log = loggers.File()