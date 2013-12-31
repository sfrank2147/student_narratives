import sys
import os
import pdb
import xlrd
import data_handling

def main():
    book = xlrd.open_workbook('../sample_narratives.xlsx')
    sheet = book.sheet_by_index(0)
#     print data_handling.category_columns(sheet)
#     print data_handling.create_student(sheet.row(1), categories)
    
if __name__ == '__main__':
    main()