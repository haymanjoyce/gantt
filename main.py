#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO freezing the app and loading along with GhostScript
# TODO adding page margin when printing to PDF (saving image)
# TODO setting image size when saving
# TODO copy to clipboard
# TODO create chart in TopLevel for creation of Image object
# TODO draw method will call Draw class
# TODO Imager becomes class in dialogues and Chart becomes class in frames
# TODO consider getting rid of top and left margin
# TODO Re-home save button to Preview it
# TODO Add Save as Postscript button
# TODO Label warning if Ghostscript not installed
# TODO Redesign GUI to avoid generating two canvases
# TODO Lift all mainframe vars to app level as toplevels need access
# TODO move Log to interface module and put log into Controls
# TODO display chart under Controls

# MANUAL OS ENVIRONMENT INSTALLS
# ghostscript

# MANUAL PYTHON ENVIRONMENT INSTALLS
# openpyxl (xlrd only does xls)
# pywin32 (does not work on Mac)


import loggers
import interface


if __name__ == '__main__':
    cli = loggers.Stream()
    cli.info(f"Logger initialised.")
    app = interface.App()

