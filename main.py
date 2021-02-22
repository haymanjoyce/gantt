#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO copying to clipboard
# TODO setting image dimensions and printing
# TODO freezing the app and loading along with GhostScript

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)


import loggers
import frames


if __name__ == '__main__':
    cli = loggers.Stream()
    cli.info(f"Logger initialised.")
    app = frames.App()

