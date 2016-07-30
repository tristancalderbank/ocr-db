import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))
from image_processing import *

DELETE_BUFFER_FILES = True


class test_pdf(unittest.TestCase):
    def setUp(self):
        self.test_pdf = pdf("WL610-J-10052-28_R1A-CODE 1.pdf", "C:\\Users\\wwfield1509\\Desktop\\envelope\\ocr-db\\tests\\WL610-J-10052-28_R1A-CODE 1.pdf") 

class test_get_number_of_pages(test_pdf):
    def runTest(self):
        self.assertEqual(self.test_pdf.number_of_pages, 2, "wrong number of pages")

class test_pdf_page(test_pdf):
    def setUp(self):
        
        



if __name__ == '__main__':
    unittest.main()
