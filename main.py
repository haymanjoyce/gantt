#!/usr/bin/env python3

# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO try statement for all processes so breaks gracefully
# TODO option for user to email error message back to me
# TODO create sample spreadsheet programmatically
# TODO create drawing from spreadsheet
# TODO scroller defaults to bottom so always shows last entry
# TODO check chart can receive data
# TODO workbook to dataclass mapping
# TODO build data objects
# TODO complete build_export
# TODO use factory method to build chart
# TODO put all data objects into dict, not list
# TODO put col header numbers in dict (name: index)
# TODO map wb headers to data objects
# TODO saves as template with default filename
# TODO in check fieldnames, suggest misspellings
# TODO add check workbook button
# TODO check if log has changed

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
    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(levelname)s - %(message)s')  # Set to INFO for production
    app = interface.App()
