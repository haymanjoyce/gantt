#!/usr/bin/env python3

import loggers
import utils


class Cleaner:
    def __init__(self, df_dict):
        self.df_dict = df_dict

    def check_df(self, name):
        return name in self.df_dict.keys()

    def print_df(self, name):
        print(self.df_dict['name'])

    def run(self):
        log.info("File cleaned.")
        return self.df_dict


cli = loggers.Stream()
log = loggers.File(utils.get_path("data.log"))

