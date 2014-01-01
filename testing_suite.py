import unittest
import data_handling
import xlrd
import narratives

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
    
    def test_yes_value(self):
        self.assertEqual(narratives.yes_value('Yes'),True)
        self.assertEqual(narratives.yes_value('y'),True)
        self.assertEqual(narratives.yes_value('No'),False)
        self.assertEqual(narratives.yes_value('n'),False)
        self.assertEqual(narratives.yes_value('hi'),None)
    
    def test_gender(self):
        words = ['boy','Male','Girl','female']
        test_responses = [narratives.gender(word) for word in words]
        male_result = {'subject':'he','object':'him', 'possessive':'his'}
        female_result = {'subject':'she','object':'her', 'possessive':'her'}
        self.assertEqual(test_responses, [male_result,male_result,female_result,female_result])