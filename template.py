#!/usr/bin/env python3

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font

from designs import *

GLOBALS = globals()

# SCALES = ('Placement', 'Interval', 'Scale Height', 'Date Format', 'Fill Color', 'Font Color', 'Font Size', 'Font Style')
# ROWS = ('Row Number', 'Height', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style')
# TASKS = ('Parent Row', 'ID', 'Start Date', 'Finish Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Text Layer', 'Bar Layer')
# MILESTONES = ('Parent Row', 'ID', 'Date', 'Fill Color', 'Text', 'Font Color', 'Font Size', 'Font Style', 'Text Anchor', 'Text Align', 'Text Adjust', 'Text Layer', 'Bar Layer')
# RELATIONSHIPS = ('Source Task', 'Destination Task', 'Line Width', 'Line Color')
# CURTAINS = ('Start Date', 'Finish Date', 'Fill Color')
# BARS = ('Date', 'Line Color', 'Line Width')
#
# DESIGNS = ('Scale', 'Row', 'Task', 'Milestone', 'Relationship', 'Curtain', 'Bar')
#
# SHEETS = {'Scales': SCALES,
#           'Rows': ROWS,
#           'Tasks': TASKS,
#           'Milestones': MILESTONES,
#           'Relationships': RELATIONSHIPS,
#           'Curtains': CURTAINS,
#           'Bars': BARS}

CLASSES = ('Scale', 'Row', 'Task', 'Milestone', 'Relationship', 'Curtain', 'Bar')


def create_template(field_name_dict):
    workbook = Workbook()
    workbook.remove(workbook.active)
    header = NamedStyle(name="header")
    header.font = Font(bold=True)
    for key, value in field_name_dict.items():
        workbook.create_sheet(key)
        workbook[key].append(value)
        for cell in workbook[key][1]:
            cell.style = header
    return workbook


def get_field_name_dict():
    """Enables template to auto match data classes"""
    field_name_dict = {}
    for class_name in CLASSES:
        new_object = GLOBALS.get(class_name)()  # globals builtin returns dict with variables in global namespace
        object_keys = ()
        for object_key in new_object.__dict__:
            object_key = object_key.replace("_", " ")
            object_key = object_key.capitalize()
            if object_key == "Id":
                object_key = object_key.upper()
            object_keys += object_key,
        sheet_name = class_name + 's'
        field_name_dict.setdefault(sheet_name, object_keys)
    return field_name_dict
