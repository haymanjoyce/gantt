#!/usr/bin/env python3

import loggers
import utils


class Processor:
    def __init__(self, df_dict):
        self.df_dict = df_dict

    def run(self):
        log.info("File processed.")
        return self.df_dict


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))
