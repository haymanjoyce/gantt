#!/usr/bin/env python3

# TODO option for user to email error message back to me
# TODO better presentation on scroller text (i.e. line spaces and titles)
# TODO loading Ghostscript with the programme (like https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO try except statement for all processes so breaks gracefully
# TODO try except statements for case where destination file already open
# TODO break gracefully if run fails
# TODO test spreadsheet for negative values
# TODO all homemade modules should be imported using "from x import y" pattern
# TODO refactor use of settings in interface
# TODO handle case where total scale height exceeds chart and row height
# TODO form validation such that finish cannot be less than start
# TODO add options to scales (font color, font size, font type, alternating (e.g. black white))
# TODO add ability to define custom date formats
# TODO improve scales such that they show end interval
# TODO add more scale types (weeks, quarters, half years)
# TODO use polygon to create box rounding (like https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners)
# TODO separate calculation from drawing; so all data class values calculated in processing module
# TODO separate text from tasks, changing tasks to bars
# TODO change label attribute to tag in data classes
# TODO recreate Row class

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
