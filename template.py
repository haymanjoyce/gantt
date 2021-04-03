#!/usr/bin/env python3

import wb

TEMPLATE = {'Bars': {'Date': {'INDEX': 0, 'MANDATORY': True, 'NAMES': ('Date',)},
                     'Line Color': {'INDEX': 1,
                                    'MANDATORY': True,
                                    'NAMES': ('Line Color', 'LineColor')},
                     'Line Width': {'INDEX': 2,
                                    'MANDATORY': True,
                                    'NAMES': ('Line Width', 'LineWidth')}},
            'Curtains': {'Fill Color': {'INDEX': 2,
                                        'MANDATORY': True,
                                        'NAMES': ('Fill Color', 'FillColor')},
                         'Finish Date': {'INDEX': 1,
                                         'MANDATORY': True,
                                         'NAMES': ('Finish', 'Finish Date', 'FinishDate')},
                         'Start Date': {'INDEX': 0,
                                        'MANDATORY': True,
                                        'NAMES': ('Start Date', 'Start', 'StartDate')}},
            'Milestones': {'Date': {'INDEX': 1, 'MANDATORY': True, 'NAMES': ('Date',)},
                           'Fill Color': {'INDEX': 2,
                                          'MANDATORY': True,
                                          'NAMES': ('Fill Color', 'FillColor')},
                           'Font Color': {'INDEX': 4,
                                          'MANDATORY': True,
                                          'NAMES': ('Font Color', 'FontColor')},
                           'Font Size': {'INDEX': 5,
                                         'MANDATORY': True,
                                         'NAMES': ('FontSize', 'Font Size')},
                           'Font Style': {'INDEX': 6,
                                          'MANDATORY': True,
                                          'NAMES': ('FontStyle', 'Font Style')},
                           'Layer': {'INDEX': 11, 'MANDATORY': True, 'NAMES': ('Layer',)},
                           'Parent Row': {'INDEX': 0,
                                          'MANDATORY': True,
                                          'NAMES': ('Parent Row', 'ParentRow')},
                           'Task Number': {'INDEX': 10,
                                           'MANDATORY': True,
                                           'NAMES': ('TaskNumber', 'Task Number')},
                           'Text': {'INDEX': 3, 'MANDATORY': True, 'NAMES': ('Text',)},
                           'Text Adjust': {'INDEX': 9,
                                           'MANDATORY': True,
                                           'NAMES': ('Text Adjust', 'TextAdjust')},
                           'Text Align': {'INDEX': 8,
                                          'MANDATORY': True,
                                          'NAMES': ('Text Align', 'TextAlign')},
                           'Text Anchor': {'INDEX': 7,
                                           'MANDATORY': True,
                                           'NAMES': ('Text Anchor', 'TextAnchor')}},
            'Relationships': {'Destination Task': {'INDEX': 1,
                                                   'MANDATORY': True,
                                                   'NAMES': ('Destination Task',
                                                             'DestinationTask')},
                              'Line Color': {'INDEX': 3,
                                             'MANDATORY': True,
                                             'NAMES': ('Line Color', 'LineColor')},
                              'Line Width': {'INDEX': 2,
                                             'MANDATORY': True,
                                             'NAMES': ('Line Width', 'LineWidth')},
                              'Source Task': {'INDEX': 0,
                                              'MANDATORY': True,
                                              'NAMES': ('Source Task', 'SourceTask')}},
            'Rows': {'Fill Color': {'INDEX': 2,
                                    'MANDATORY': True,
                                    'NAMES': ('Fill Color', 'FillColor')},
                     'Font Color': {'INDEX': 4,
                                    'MANDATORY': True,
                                    'NAMES': ('Font Color', 'FontColor')},
                     'Font Size': {'INDEX': 5,
                                   'MANDATORY': True,
                                   'NAMES': ('FontSize', 'Font Size')},
                     'Font Style': {'INDEX': 6,
                                    'MANDATORY': True,
                                    'NAMES': ('FontStyle', 'Font Style')},
                     'Row Height': {'INDEX': 1,
                                    'MANDATORY': True,
                                    'NAMES': ('Row Height', 'RowHeight')},
                     'Row Number': {'INDEX': 0,
                                    'MANDATORY': True,
                                    'NAMES': ('RowNumber', 'Row Number')},
                     'Text': {'INDEX': 3, 'MANDATORY': True, 'NAMES': ('Text',)}},
            'Scales': {'Date Format': {'INDEX': 3,
                                       'MANDATORY': True,
                                       'NAMES': ('DateFormat', 'Date Format')},
                       'Fill Color': {'INDEX': 4,
                                      'MANDATORY': True,
                                      'NAMES': ('Fill Color', 'FillColor')},
                       'Font Color': {'INDEX': 5,
                                      'MANDATORY': True,
                                      'NAMES': ('Font Color', 'FontColor')},
                       'Font Size': {'INDEX': 6,
                                     'MANDATORY': True,
                                     'NAMES': ('FontSize', 'Font Size')},
                       'Font Style': {'INDEX': 7,
                                      'MANDATORY': True,
                                      'NAMES': ('FontStyle', 'Font Style')},
                       'Interval': {'INDEX': 1, 'MANDATORY': True, 'NAMES': ('Interval',)},
                       'Placement': {'INDEX': 0,
                                     'MANDATORY': True,
                                     'NAMES': ('Placement',)},
                       'Scale Height': {'INDEX': 2,
                                        'MANDATORY': True,
                                        'NAMES': ('Scale Height', 'ScaleHeight')}},
            'Tasks': {'Fill Color': {'INDEX': 3,
                                     'MANDATORY': True,
                                     'NAMES': ('Fill Color', 'FillColor')},
                      'Finish Date': {'INDEX': 2,
                                      'MANDATORY': True,
                                      'NAMES': ('Finish', 'Finish Date', 'FinishDate')},
                      'Font Color': {'INDEX': 5,
                                     'MANDATORY': True,
                                     'NAMES': ('Font Color', 'FontColor')},
                      'Font Size': {'INDEX': 6,
                                    'MANDATORY': True,
                                    'NAMES': ('FontSize', 'Font Size')},
                      'Font Style': {'INDEX': 7,
                                     'MANDATORY': True,
                                     'NAMES': ('FontStyle', 'Font Style')},
                      'Layer': {'INDEX': 12, 'MANDATORY': True, 'NAMES': ('Layer',)},
                      'Parent Row': {'INDEX': 0,
                                     'MANDATORY': True,
                                     'NAMES': ('Parent Row', 'ParentRow')},
                      'Start Date': {'INDEX': 1,
                                     'MANDATORY': True,
                                     'NAMES': ('Start Date', 'Start', 'StartDate')},
                      'Task Number': {'INDEX': 11,
                                      'MANDATORY': True,
                                      'NAMES': ('TaskNumber', 'Task Number')},
                      'Text': {'INDEX': 4, 'MANDATORY': True, 'NAMES': ('Text',)},
                      'Text Adjust': {'INDEX': 10,
                                      'MANDATORY': True,
                                      'NAMES': ('Text Adjust', 'TextAdjust')},
                      'Text Align': {'INDEX': 9,
                                     'MANDATORY': True,
                                     'NAMES': ('Text Align', 'TextAlign')},
                      'Text Anchor': {'INDEX': 8,
                                      'MANDATORY': True,
                                      'NAMES': ('Text Anchor', 'TextAnchor')}}}

VARIANTS = {
    'Start Date': ('Start',),
    'Finish Date': ('Finish',),
}


def get_variants(field_name):
    """We don't bother with case (because we convert all to lower case when reading)."""
    variants = (field_name.strip(), field_name.replace(" ", ""), " ".join(field_name.split()),)
    if field_name in VARIANTS:
        variants += VARIANTS.get(field_name)
    return variants


def create_field_dict(field_name, index):
    variants = get_variants(field_name)
    field_dict = dict()
    field_dict.setdefault("MANDATORY", True)
    field_dict.setdefault("NAMES", tuple(set((field_name,) + variants)))
    field_dict.setdefault("INDEX", int(index))
    return field_dict


def create_sheet_dict(sheet_headers):
    sheet_dict = dict()
    for index, field_name in enumerate(sheet_headers):
        field_dict = create_field_dict(field_name, index)
        sheet_dict.setdefault(field_name, field_dict)
    return sheet_dict


def create_workbook_dict(workbook):
    wb_dict = dict()
    for sheet_name in workbook.sheetnames:
        sheet_headers = wb.get_sheet_fieldnames(workbook[sheet_name])
        sheet_dict = create_sheet_dict(sheet_headers)
        wb_dict.setdefault(sheet_name, sheet_dict)
    return wb_dict


def get_sheet_dict(sheet_name):
    return TEMPLATE.get(sheet_name)


def get_field_dict(field_name):
    return TEMPLATE.get(field_name)


def get_mandatory(field_dict):
    return field_dict.get("MANDATORY")


def get_names(field_dict):
    return field_dict.get("NAMES")


def get_index(field_dict):
    return field_dict.get("INDEX")


def set_index(field_dict, index):
    field_dict["INDEX"] = index
