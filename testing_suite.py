import unittest
import data_handling
import xlrd

class TestNarratives(unittest.TestCase):
    def setUp(self):
        self.sheet = \
             xlrd.open_workbook('sample_narratives.xlsx').sheet_by_index(0)
        
    
    def test_category_columns(self):
        categories = data_handling.category_columns(self.sheet)
        self.assertEqual(categories[0],'name')
        self.assertEqual(len(categories),5)
    
    def test_create_student(self):
        categories = data_handling.category_columns(self.sheet)
        student = data_handling.create_student(self.sheet.row(1),categories)
        self.assertEqual(student['name'],'John')
    
    def test_student_data(self):
        data = data_handling.student_data(self.sheet)
        self.assertEqual(data[0]['name'], 'John')
        self.assertEqual(data[1]['does homework?'],'no')