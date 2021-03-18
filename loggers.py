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


class Widget(logging.Logger):
    def __init__(self, widget=None):
        super(Widget, self).__init__(name='Stream', level='DEBUG')

        self.widget = widget

        self.formatter = logging.Formatter('%(levelname)s - %(message)s')

        self.handler = WidgetHandler(widget=None)
        self.handler.setLevel(logging.DEBUG)
        self.handler.setFormatter(self.formatter)

        self.addHandler(self.handler)


class WidgetHandler(logging.StreamHandler):
    def __init__(self, widget):
        super(WidgetHandler, self).__init__()

        self.widget = widget

    def emit(self, record):
        print(record)
        print(self.format(record))
        print(self.widget)  # insert message into widget


# logger = logging.getLogger(name=__name__)
# logger.setLevel(logging.DEBUG)
#
# simple_format = logging.Formatter(style='{', fmt='{levelname} - {message}')
#
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# stream_handler.setFormatter(simple_format)
#
# file_handler = logging.FileHandler(filename="data.log")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(simple_format)
#
# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)
#
# logger.debug("Debug level message.")
# logger.info("Info level message.")
