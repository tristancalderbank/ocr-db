#import Image
import os
from subprocess import check_output

class tesseract:

    tiff_buffer_name = "tiff_buffer.tif"
    txt_buffer_name = "txt_buffer"

    def __init__(self, input_path, output_path, dpi=300):
        self.input_path = input_path
        self.output_path = output_path
        self.dpi = dpi

    def __enter__(self):
        return self

    def strip_text(self):
        with open(self.txt_buffer_name + ".txt", "rb") as input_file:
            return input_file.read()

    def process_ocr(self):
        print check_output("tesseract " + self.tiff_buffer_name + " " + self.txt_buffer_name, shell=True)

    def create_searchable_pdf(input_file_path, output_file_path):
        print check_output("tesseract " + self.input_path + " " + output_file_path + " pdf", shell=True)

    def pdf_to_text(self):
        self.convert_to_tiff()
        self.process_ocr()
        pdf_text = self.strip_text()
        text_filter = string_filter(pdf_text)
        pdf_text = text_filter.strip("single_quotes")
        return pdf_text
   

    def cleanup(self):
        try:
            os.remove(self.tiff_buffer_name)
            os.remove(self.txt_buffer_name + ".txt")
        except WindowsError:
            print "Couldn't find buffer files to delete"

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup()


