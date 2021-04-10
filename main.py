#!/usr/bin/env python3

# TODO option for user to email error message back to me
# TODO better presentation on scroller (line spaces and titles)
# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO try statement for all processes so breaks gracefully
# TODO complete dataset module
# TODO try except statements for case where destination file open
# TODO finish exceptions function
# TODO work out why exceptions running multiple times

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
