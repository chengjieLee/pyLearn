#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd

# def read_xslx():
#     workboox = xlrd.open_workbook('xlsx_test.xlsx')
#     s1 = workboox.sheet_by_name('HonorOfKings')
#     rows = s1.nrows
#     print(rows)
#     for index in range(1, rows):
#         print(index)
#         row = s1.row_values(index)
#         print(row)
#         hero_name, games, wins = row
#         print('已使用%s 苦战%s场 胜率达到惊人的%s %%' % (hero_name, games, wins) )

# if __name__ == '__main__':
#     read_xslx()

def read_xslx():
    xsl_data = xlrd.open_workbook('xlsx_test.xlsx')
    table = xsl_data.sheets()[0]
    nrows = table.nrows
    for i in range(1, nrows):
        print (table.row_values(i)[0:])

if __name__ == '__main__':
    read_xslx()