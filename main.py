#!/usr/bin/env python3

# TODO ditch Canvas, create SVG, save as image file (button) using Cairo, open file (option on save)
# TODO log file is saved to user defined directory and option to open on run (check box); remove from interface
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
# TODO redraw rows as lines, like separators
# TODO check for and clean blank cells (to avoid type errors)
# TODO check for and clean references to rows that do no exist
# TODO calibrate task baseline to be middle of row
# TODO remove option of row height - don't do this as users may want margin underneath rows for notes
# TODO rename pipes (e.g. to lines)
# TODO rename settings to chart and Chart
# TODO rename tags as layer in shapes parameters
# TODO prevent from_row being higher number than to_row in sections
# TODO interface option to show row y positions in pixels
# TODO save as svg button
# TODO convert svg to image file button

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript (C:\Program Files (x86)\gs\gs9.53.3\) (C:\Program Files (x86)\gs\gs9.54.0\bin)

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# ghostscript (interface to API)
# Pillow (fork of PIL; better maintained)
# tkcalendar (PyInstaller requires hidden import from Babel)
# attrs
# CairoSVG
# reportlab
# svglib

import logging
import interface
from filing import get_path


if __name__ == '__main__':
    filename = get_path('app.log')
    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(levelname)s - %(message)s')
    app = interface.App()
