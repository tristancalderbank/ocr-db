import os
import sys
import unittest
import test_image_processing as test_ip

sys.path.insert(0, os.path.abspath('..'))
import image_processing as ip
import tesseract

test_ip.ip.DELETE_BUFFER_FILES = False

class test_tesseract(test_ip.test_crop):
    def runTest(self):
        with tesseract.tesseract(self.crop) as ocr_processor:
                contents = ""
                contents = ocr_processor.process_ocr()
                print "tesseract contents:"
                print contents
                self.assertNotEqual(contents, "", "tesseract failed to produce data")


if __name__ == '__main__':
    unittest.main()
