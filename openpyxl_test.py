import openpyxl

workbook = openpyxl.load_workbook('xlsx_test.xlsx')

s_name = workbook.sheetnames

