#!/usr/bin/env python3

import source

TEMPLATE = {'Bars': {'Date': {'COLUMN': 0, 'MANDATORY': True, 'NAMES': ('Date',)},
                     'Line Color': {'COLUMN': 1,
                                    'MANDATORY': True,
                                    'NAMES': ('LineColor', 'Line Color')},
                     'Line Width': {'COLUMN': 2,
                                    'MANDATORY': True,
                                    'NAMES': ('LineWidth', 'Line Width')}},
            'Curtains': {'Fill Color': {'COLUMN': 2,
                                        'MANDATORY': True,
                                        'NAMES': ('FillColor', 'Fill Color')},
                         'Finish Date': {'COLUMN': 1,
                                         'MANDATORY': True,
                                         'NAMES': ('Finish', 'Finish Date', 'FinishDate')},
                         'Start Date': {'COLUMN': 0,
                                        'MANDATORY': True,
                                        'NAMES': ('StartDate', 'Start', 'Start Date')}},
            'Milestones': {'Date': {'COLUMN': 1, 'MANDATORY': True, 'NAMES': ('Date',)},
                           'Fill Color': {'COLUMN': 2,
                                          'MANDATORY': True,
                                          'NAMES': ('FillColor', 'Fill Color')},
                           'Font Color': {'COLUMN': 4,
                                          'MANDATORY': True,
                                          'NAMES': ('FontColor', 'Font Color')},
                           'Font Size': {'COLUMN': 5,
                                         'MANDATORY': True,
                                         'NAMES': ('Font Size', 'FontSize')},
                           'Font Style': {'COLUMN': 6,
                                          'MANDATORY': True,
                                          'NAMES': ('FontStyle', 'Font Style')},
                           'Layer': {'COLUMN': 11, 'MANDATORY': True, 'NAMES': ('Layer',)},
                           'Parent Row': {'COLUMN': 0,
                                          'MANDATORY': True,
                                          'NAMES': ('Parent Row', 'ParentRow')},
                           'Task Number': {'COLUMN': 10,
                                           'MANDATORY': True,
                                           'NAMES': ('TaskNumber', 'Task Number')},
                           'Text': {'COLUMN': 3, 'MANDATORY': True, 'NAMES': ('Text',)},
                           'Text Adjust': {'COLUMN': 9,
                                           'MANDATORY': True,
                                           'NAMES': ('Text Adjust', 'TextAdjust')},
                           'Text Align': {'COLUMN': 8,
                                          'MANDATORY': True,
                                          'NAMES': ('TextAlign', 'Text Align')},
                           'Text Anchor': {'COLUMN': 7,
                                           'MANDATORY': True,
                                           'NAMES': ('Text Anchor', 'TextAnchor')}},
            'Relationships': {'Destination Task': {'COLUMN': 1,
                                                   'MANDATORY': True,
                                                   'NAMES': ('DestinationTask',
                                                             'Destination Task')},
                              'Line Color': {'COLUMN': 3,
                                             'MANDATORY': True,
                                             'NAMES': ('LineColor', 'Line Color')},
                              'Line Width': {'COLUMN': 2,
                                             'MANDATORY': True,
                                             'NAMES': ('LineWidth', 'Line Width')},
                              'Source Task': {'COLUMN': 0,
                                              'MANDATORY': True,
                                              'NAMES': ('Source Task', 'SourceTask')}},
            'Rows': {'Fill Color': {'COLUMN': 2,
                                    'MANDATORY': True,
                                    'NAMES': ('FillColor', 'Fill Color')},
                     'Font Color': {'COLUMN': 4,
                                    'MANDATORY': True,
                                    'NAMES': ('FontColor', 'Font Color')},
                     'Font Size': {'COLUMN': 5,
                                   'MANDATORY': True,
                                   'NAMES': ('Font Size', 'FontSize')},
                     'Font Style': {'COLUMN': 6,
                                    'MANDATORY': True,
                                    'NAMES': ('FontStyle', 'Font Style')},
                     'Row Height': {'COLUMN': 1,
                                    'MANDATORY': True,
                                    'NAMES': ('Row Height', 'RowHeight')},
                     'Row Number': {'COLUMN': 0,
                                    'MANDATORY': True,
                                    'NAMES': ('RowNumber', 'Row Number')},
                     'Text': {'COLUMN': 3, 'MANDATORY': True, 'NAMES': ('Text',)}},
            'Scales': {'Date Format': {'COLUMN': 3,
                                       'MANDATORY': True,
                                       'NAMES': ('DateFormat', 'Date Format')},
                       'Fill Color': {'COLUMN': 4,
                                      'MANDATORY': True,
                                      'NAMES': ('FillColor', 'Fill Color')},
                       'Font Color': {'COLUMN': 5,
                                      'MANDATORY': True,
                                      'NAMES': ('FontColor', 'Font Color')},
                       'Font Size': {'COLUMN': 6,
                                     'MANDATORY': True,
                                     'NAMES': ('Font Size', 'FontSize')},
                       'Font Style': {'COLUMN': 7,
                                      'MANDATORY': True,
                                      'NAMES': ('FontStyle', 'Font Style')},
                       'Interval': {'COLUMN': 1,
                                    'MANDATORY': True,
                                    'NAMES': ('Interval',)},
                       'Placement': {'COLUMN': 0,
                                     'MANDATORY': True,
                                     'NAMES': ('Placement',)},
                       'Scale Height': {'COLUMN': 2,
                                        'MANDATORY': True,
                                        'NAMES': ('Scale Height', 'ScaleHeight')}},
            'Tasks': {'Fill Color': {'COLUMN': 3,
                                     'MANDATORY': True,
                                     'NAMES': ('FillColor', 'Fill Color')},
                      'Finish Date': {'COLUMN': 2,
                                      'MANDATORY': True,
                                      'NAMES': ('Finish', 'Finish Date', 'FinishDate')},
                      'Font Color': {'COLUMN': 5,
                                     'MANDATORY': True,
                                     'NAMES': ('FontColor', 'Font Color')},
                      'Font Size': {'COLUMN': 6,
                                    'MANDATORY': True,
                                    'NAMES': ('Font Size', 'FontSize')},
                      'Font Style': {'COLUMN': 7,
                                     'MANDATORY': True,
                                     'NAMES': ('FontStyle', 'Font Style')},
                      'Layer': {'COLUMN': 12, 'MANDATORY': True, 'NAMES': ('Layer',)},
                      'Parent Row': {'COLUMN': 0,
                                     'MANDATORY': True,
                                     'NAMES': ('Parent Row', 'ParentRow')},
                      'Start Date': {'COLUMN': 1,
                                     'MANDATORY': True,
                                     'NAMES': ('StartDate', 'Start', 'Start Date')},
                      'Task Number': {'COLUMN': 11,
                                      'MANDATORY': True,
                                      'NAMES': ('TaskNumber', 'Task Number')},
                      'Text': {'COLUMN': 4, 'MANDATORY': True, 'NAMES': ('Text',)},
                      'Text Adjust': {'COLUMN': 10,
                                      'MANDATORY': True,
                                      'NAMES': ('Text Adjust', 'TextAdjust')},
                      'Text Align': {'COLUMN': 9,
                                     'MANDATORY': True,
                                     'NAMES': ('TextAlign', 'Text Align')},
                      'Text Anchor': {'COLUMN': 8,
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
    field_dict.setdefault("COLUMN", int(index))
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
        sheet_headers = source.get_sheet_headers(workbook[sheet_name])
        sheet_dict = create_sheet_dict(sheet_headers)
        wb_dict.setdefault(sheet_name, sheet_dict)
    return wb_dict
