#!/usr/bin/env python3

import logging

from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font

from designs import *

GLOBALS = globals()

DESIGNS = ('Scale', 'Row', 'Task', 'Milestone', 'Relationship', 'Curtain')


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
    field_name_dict = {}
    try:
        for class_name in DESIGNS:
            data_class_instance = GLOBALS.get(class_name)()
            field_names = get_field_names(data_class_instance)
            sheet_name = class_name + 's'
            field_name_dict.setdefault(sheet_name, field_names)
    except TypeError:
        logging.debug("Trying to call class that does not exist.")
    return field_name_dict


def get_field_names(data_class_instance):
    field_names = ()
    instance_attributes = data_class_instance.__dict__
    exceptions = get_exceptions(instance_attributes)
    for field_name in instance_attributes:
        field_name = field_name.replace("_", " ")
        field_name = field_name.strip()
        field_name = field_name.capitalize()
        if field_name == "Id":
            field_name = field_name.upper()
        if field_name not in exceptions:
            field_names += field_name,
    return field_names


def get_exceptions(instance_attributes):
    exceptions = ('Type', 'Labels', )
    design_type = instance_attributes.get('type').lower()
    try:
        if design_type == DESIGNS[0].lower():
            exceptions += ('Width', )
        elif design_type == DESIGNS[1].lower():
            exceptions += ()
        elif design_type == DESIGNS[2].lower():
            exceptions += ()
        elif design_type == DESIGNS[3].lower():
            exceptions += ()
        elif design_type == DESIGNS[4].lower():
            exceptions += ()
        elif design_type == DESIGNS[5].lower():
            exceptions += ()
        else:
            pass
    except IndexError:
        logging.debug(f"Called item in DESIGNS that does not exist.")
    return exceptions
