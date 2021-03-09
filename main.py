#!/usr/bin/env python3

# TODO sketch out app
# TODO freezing the app and loading along with GhostScript
# TODO warning if Ghostscript not installed
# TODO make export_data df agnostic

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (does not work on Mac)


import interface


if __name__ == '__main__':
    app = interface.App()
