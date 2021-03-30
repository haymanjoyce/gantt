#!/usr/bin/env python3

import logging
from PIL import Image
from io import BytesIO
import win32clipboard as clipboard


def copy_to_clipboard(chart):
    chart_as_postscript = chart.postscript()
    chart_as_utf = chart_as_postscript.encode('utf-8')
    chart_as_bytecode = BytesIO(chart_as_utf)

    chart_as_bitmap = BytesIO()
    Image.open(chart_as_bytecode).save(chart_as_bitmap, "BMP")

    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(clipboard.CF_DIB, chart_as_bitmap.getvalue()[14:])  # [14:] removes header
    clipboard.CloseClipboard()

    chart_as_bytecode.close()
    chart_as_bitmap.close()

    logging.info("Image copied to clipboard.")
