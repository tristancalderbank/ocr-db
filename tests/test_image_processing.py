import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))
import image_processing as ip

ip.DELETE_BUFFER_FILES = True


class test_pdf(unittest.TestCase):
    def setUp(self):
        self.test_pdf = ip.pdf("two-page-pdf.pdf", "two-page-pdf.pdf") 

class test_get_number_of_pages(test_pdf):
    def runTest(self):
        self.assertEqual(self.test_pdf.number_of_pages, 1, "wrong number of pages")

class test_pdf_page(test_pdf):
    def setUp(self):
        super(test_pdf_page, self).setUp()
        self.page = ip.pdf_page(self.test_pdf, 0)

class test_page_creation(test_pdf_page):
    def runTest(self):
        self.assertEqual(os.path.isfile(self.page.name), True, "pdf buffer page not created")

class test_page_deletion(test_pdf):
    def runTest(self):
        with ip.pdf_page(self.test_pdf, 0) as page:
            pass
        self.assertEqual(os.path.isfile(page.name), False, "pdf buffer not deleted")


class test_crop(test_pdf_page):
    def setUp(self):
        super(test_crop, self).setUp()
        
        crop_width = 100
        crop_height = 20
        crop_h_offset = 0
        crop_v_offset = 0
        self.crop = ip.tif_crop(self.page, crop_width, crop_height, crop_h_offset, crop_v_offset)

class test_crop_creation(test_crop):
    def runTest(self):
        self.assertEqual(os.path.isfile(self.crop.name), True, "crop buffer not created")


if __name__ == '__main__':
    unittest.main()
