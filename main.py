#!/usr/bin/env python3

# TODO loading Ghostscript with the programme (ref: https://www.biopdf.com/guide/detecting_ghostscript.php)
# TODO warning if Ghostscript not installed
# TODO develop a Windows installer
# TODO warning if not Windows OS
# TODO freezing the app and loading along with GhostScript
# TODO rebuild environment without pyinstaller
# TODO apply get_path() to all local resources
# TODO add checking module
# TODO select file, press select but don't select file, then run breaks it as file is None
# TODO solve why data file created on execute; try putting it in log folder or MEIPASS
# TODO make more elegant solution to get_path circular relationship issue

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (note, does not work on Mac)
# pyinstaller


import interface


if __name__ == '__main__':
    app = interface.App()
