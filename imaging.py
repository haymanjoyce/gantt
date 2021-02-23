#!/usr/bin/env python3

import loggers
from io import BytesIO
from PIL import Image
from settings import *


class Imaging(Image):
    def __init__(self, chart):
        super(Imaging, self).__init__()

        self.chart = chart
        self.settings = get_settings()
        self.open(self.to_bytecode())

    def clip_image(self):
        pass
        # take chart and resize to settings w and h

    def to_bytecode(self):
        to_postscript = self.chart.postscript()
        to_utf8 = to_postscript.encode('utf-8')
        return BytesIO(to_utf8)


cli = loggers.Stream()

