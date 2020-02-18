import xlrd
import xlutils.copy

read_book = xlrd.open_workbook('xlsx_test.xlsx')

write_book = xlutils.copy.copy(read_book)

write_sheet = write_book.get_sheet(0)

write_sheet.write(1,1,'changed')

write_book.add_sheet('sheetnn2', cell_overwrite_ok = True)

write_book.save('savexl.xls')