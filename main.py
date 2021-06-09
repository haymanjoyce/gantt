#!/usr/bin/env python3

# TODO option to download as SVG file
# TODO option for user to email error message back to me
# TODO better presentation on scroller text (i.e. line spaces and titles)
# TODO loading Ghostscript with the programme (like https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO try except statement for all processes so breaks gracefully
# TODO try except statements for case where destination file already open
# TODO break gracefully if run fails
# TODO test spreadsheet for negative values
# TODO refactor use of settings in interface
# TODO handle case where total scale height exceeds chart and row height
# TODO form validation such that finish cannot be less than start
# TODO add options to scales (font color, font size, font type, alternating (e.g. black white))
# TODO apply date format used in Excel (interpret Excel to Python)
# TODO add more scale types (weeks, quarters, half years)
# TODO use polygon to create box rounding (like https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners)
# TODO debug case where user able to enter in settings finish date before start unchallenged
# TODO make default text size proportional to scale and row height
# TODO in Painter replace usage of create_text with draw_text
# TODO check for and clean blank rows
# TODO check for and clean blank cells (to avoid type errors)
# TODO check for and clean references to rows that do no exist
# TODO finish connectors, passing all args to draw_line
# TODO pipes
# TODO item layer

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# ghostscript (interface to API)
# Pillow (fork of PIL; better maintained)
# tkcalendar (PyInstaller requires hidden import from Babel)
# attrs

import logging
import interface
from filing import get_path


if __name__ == '__main__':
    filename = get_path('app.log')
    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(levelname)s - %(message)s')
    app = interface.App()
