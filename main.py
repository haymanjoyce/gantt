#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO freezing the app and loading along with GhostScript
# TODO Label warning if Ghostscript not installed
# TODO prove processing and export
# TODO pull button states out and handle separately

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (does not work on Mac)


import interface


if __name__ == '__main__':
    app = interface.App()
