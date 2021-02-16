#!/usr/bin/env python3

# TODO sketch out app (tkinter, canvas, postscript, convert postscript to other formats)
# TODO copying to clipboard
# TODO setting image dimensions and printing
# TODO freezing the app and loading along with GhostScript
# TODO reading multiple tabs in pandas
# TODO convert canvas data to Excel
# TODO scrollbars if canvas larger than window
# TODO move Excel export to Excel class

import loggers
import frames


if __name__ == '__main__':
    cli = loggers.Stream()
    cli.info(f"Logger initialised.")
    app = frames.App()

