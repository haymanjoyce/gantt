#!/usr/bin/env python3

# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO create drawing from spreadsheet
# TODO get logging to work with Pyinstaller (using --runtime-hook logging, for example)
# TODO try replacing _MEIPASS reference in script to same reference in --workpath in batch file

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# ghostscript (interface to API)
# Pillow (imaging library)
# tkcalendar (PyInstaller requires hidden import from Babel)

import logging
import interface
from utils import get_path


if __name__ == '__main__':
    filename = get_path('app.log')
    logging.basicConfig(filename=filename, level=logging.INFO, format='%(levelname)s - %(message)s')
    app = interface.App()
