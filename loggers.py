#!/usr/bin/env python3

import logging

# WARNING: beware importing * from module with initialised logger


class Stream(logging.Logger):
    def __init__(self):
        super(Stream, self).__init__(name='Stream', level='DEBUG')

        self.formatter = logging.Formatter('%(levelname)s - %(message)s')

        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(self.formatter)

        self.addHandler(self.handler)


class File(logging.Logger):
    def __init__(self, log_file):
        super(File, self).__init__(name='File', level='DEBUG')

        self.formatter = logging.Formatter('%(levelname)s - %(message)s')

        self.handler = logging.FileHandler(filename=log_file)
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(self.formatter)

        self.addHandler(self.handler)
