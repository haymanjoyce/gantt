#!/usr/bin/env python3

import io
from tkinter import filedialog
# from PIL import Image
# from cairosvg import svg2png
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM


def save_image(svg_filename):
    file_types = [
        # ('PDF file', '*.pdf'),
        # ('JPG file', '*.jpg'),
        ('PNG file', '*.png'),
        # ('BMP file', '*.bmp'),
        # ('TIFF file', '*.tif'),
    ]
    file = filedialog.asksaveasfile(mode="w",
                                    title="Save As",
                                    filetypes=file_types,
                                    defaultextension="*.pdf",
                                    initialfile="*.pdf"
                                    )
    if file:
        file_name = file.name.lower()
        if file_name.endswith(('.png', )):
            drawing = svg2rlg(svg_filename)
            renderPM.drawToFile(drawing, file_name, fmt="PNG")


# cairosvg.svg2png(
#     url="/path/to/input.svg", write_to="/tmp/output.png")
#
# cairosvg.svg2pdf(
#     file_obj=open("/path/to/input.svg", "rb"), write_to="/tmp/output.pdf")
#
# output = cairosvg.svg2ps(
#     bytestring=open("/path/to/input.svg").read().encode('utf-8'))

# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPM
# drawing = svg2rlg("my.svg")
# renderPM.drawToFile(drawing, "my.png", fmt="PNG")