#!/usr/bin/env python3

# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO create drawing from spreadsheet
# TODO test PyInstaller with tkcalendar addition
# TODO validate settings data
# TODO debug break on blank dimension fields

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# ghostscript (interface to API)
# Pillow (imaging library)
# tkcalendar (check docs when using PyInstaller)

import interface


if __name__ == '__main__':
    app = interface.App()
