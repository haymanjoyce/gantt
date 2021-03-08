#!/usr/bin/env python3

import loggers
import pandas as pd


class Cleaner:
    def __init__(self, xls):
        self.xls = xls
        self.df_0 = pd.read_excel(self.xls, 0)
        self.df_1 = pd.read_excel(self.xls, 1)

    # def temp(self):
    #     writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')
    #
    #     # Write each dataframe to a different worksheet.
    #     df1.to_excel(writer, sheet_name='Sheet1')
    #     df2.to_excel(writer, sheet_name='Sheet2')
    #     df3.to_excel(writer, sheet_name='Sheet3')
    #
    #     # Close the Pandas Excel writer and output the Excel file.
    #     writer.save()

    def run(self):
        log.info("File cleaned.")
        return self.xls


cli = loggers.Stream()
log = loggers.File()

