#!/usr/bin/env python3

# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO warning if not Windows OS
# TODO freezing the app and loading along with GhostScript
# TODO rebuild environment without pyinstaller
# TODO apply get_path() to all local resources
# TODO add checking module


# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# pyinstaller


import interface


if __name__ == '__main__':
    app = interface.App()
