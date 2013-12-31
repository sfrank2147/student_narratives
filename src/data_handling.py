import xlrd

#global constants to help analyze data
EMPTY = 0   #empty string u''
TEXT = 1    #unicode string
NUMBER = 2  #float
DATE = 3    #float
BOOLEAN = 4 #int - 1 for True, 0 for False
ERROR = 5



def category_columns(sheet):
    '''
    Return a dictionary mapping each column to its category
    Categories should be lower case strings
    If not, ignore that category
    
    Parameter is a Sheet object
    '''
    first_row = sheet.row(0)
    category_cols = {}
    for col_number, cell in enumerate(first_row):
        if cell.ctype == TEXT:
            category_cols[col_number] = cell.value.lower()
    return category_cols

def create_student(row, categories):
    '''
    Return a dictionary with all the info for a student
    
    input is a row object from the spreadsheet and a dictionary
    mapping columns to categories
    '''
    student_dict = {}
    for column, entry in enumerate(row):
        category = categories[column]
        student_dict[category] = entry.value
    return student_dict

def student_data(sheet):
    '''Return list of student dictionaries'''
    categories = category_columns(sheet)
    return [create_student(sheet.row(x),categories) for x in range(1,sheet.nrows)]