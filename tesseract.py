import os
from subprocess import check_output

import debug
from debug import logger


DELETE_BUFFER_FILES = True
DEBUG_TESSERACT = True

if not DEBUG_TESSERACT:
    logger.setLevel(debug.logging.INFO)


class tesseract:

    txt_buffer_name = "txt_buffer"


    def __init__(self, input_file, output_file_path=None):
        self.input_file_name = input_file.name
        self.input_file_path = None
        self.output_file_path = output_file_path

    def __enter__(self):
        return self

    def strip_text(self):
        with open(self.txt_buffer_name + ".txt", "rb") as input_file:
            text = input_file.read()
            logger.debug(text)
            return text

    def process_ocr(self):
        print check_output("tesseract " + self.input_file_name + " " + self.txt_buffer_name, shell=True)
        pdf_text = self.strip_text()
        return pdf_text
 
    def create_searchable_pdf(input_file_name, output_file_path):
        print check_output("tesseract " + self.input_file_path + " " + output_file_path + " pdf", shell=True)

    def cleanup(self):
	if DELETE_BUFFER_FILES:
	    try:
	        os.remove(self.txt_buffer_name + ".txt")
	    except WindowsError:
	        logger.debug("Tried to delete txt buffer and failed")

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup()


