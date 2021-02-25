#!/usr/bin/env python3

import loggers
from io import BytesIO
from PIL import Image
from settings import *

# we create canvas in TopLevel as it would appear as image (including margins for example)
# we create this class in chart module
# we need not show TopLevel - hidden
# the out put is output = Image.open(bytecode)
# this can be used to save files or paste to clipboard
# you can strip out code from save_image dialogue and just give it the prepared Image object
# this could become class in dialogues and Chart could become class in frames


# class Image(Toplevel):
#     def __init__(self, parent):
#         super(Image, self).__init__(parent)
#
#         self.parent = parent
#
#         self.settings = get_settings()
#         self.width = eval(self.settings['width'])
#         self.height = eval(self.settings['height'])
#
#         # self.config(scrollregion=(0, 0, self.width, self.height))
#
#         # self.pack(side=LEFT, anchor="nw")
#
#     def draw(self):
#         pass
#
#     def render(self):
#         pass


# def resize_chart(self):
#     settings = get_settings()
#     width = settings['width']
#     height = settings['height']
#     print(width, height)
#
#
# def to_bytecode(self):
#     to_postscript = self.parent.viewer.chart.postscript()
#     to_utf8 = to_postscript.encode('utf-8')
#     return BytesIO(to_utf8)


cli = loggers.Stream()

