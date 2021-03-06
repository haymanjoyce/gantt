#!/usr/bin/env python3

import loggers


class Cleaner:
    def __init__(self, df):
        self.df = df

    def run(self):
        log.info("File cleaned.")
        return self.df


class Processor:
    def __init__(self, df):
        self.df = df

    def run(self):
        log.info("File processed.")
        return self.df


cli = loggers.Stream()
log = loggers.File()

