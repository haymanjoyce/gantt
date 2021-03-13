#!/usr/bin/env python3

# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO rebuild environment
# TODO add checking module (may need to use openpxyl to test for merged cells)
# TODO select file, press select but don't select file, then run breaks it as file is None

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# pyinstaller


import interface


if __name__ == '__main__':
    app = interface.App()
