#import Image
import os
import glob
import pytesseract
from subprocess import check_output
import matplotlib.pyplot as plt
import time
from pdfdatabase import *
import pyPdf


class crawler:
    
    master_pdf_list = []
    protected_directories = []
    
    def __init__(self, root):
        self.root = root

    def crawl(self, path=None):

        if path == None:
            path = self.root
        
        try:
            os.chdir(path)
        except WindowsError:
            print "Could not access directory: " + path
            protected_directories.append(path)
            return

        current_contents = os.listdir(path)
        
        directories = []

        for item in current_contents:
            if os.path.isdir(path + "\\" + item):
                directories.append(item)

        if directories != []:
            for folder in directories:
                self.crawl(path + "\\" + folder)

        os.chdir(path)       
        pdfs = glob.glob('*.pdf')
        for pdf in pdfs:
            self.master_pdf_list.append(path + "\\" + pdf)

        return self.master_pdf_list, self.protected_directories

class pdf_processor:

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

    def pdf_text_filter(self, input_string):
        return input_string.replace("'", "")


    def number_of_pages(self):

        inputpdf = pyPdf.PdfFileReader(open(self.input_path, "rb"))
        return inputpdf.numPages    

    def cleanup(self):
        try:
            os.remove(self.tiff_buffer_name)
            os.remove(self.txt_buffer_name + ".txt")
        except WindowsError:
            print "Couldn't find buffer files to delete"

    def __exit__(self, exc_type, exc_value, traceback):
        self.cleanup()


# may need more complex filtering in the future
class string_filter:

    filters = {"special_chars": [";", '"', "'", "(", ")"],\
               "single_quotes": ["'"]}
    
    def __init__(self, input_string):
        self.input_string = input_string
    
    def strip(self, filter_name):
        for item in self.filters[filter_name]:
            self.input_string = self.input_string.replace(item, "")

        return self.input_string



root = ""
new_crawler = crawler(root)
pdfs, protected = new_crawler.crawl()

failed_to_read = 0

print "Doing processing in folder: " + os.getcwd()
with database() as new_database:

    print str(len(pdfs)) + " PDFs found, processing..."
    number_processed = 0
    for pdf in pdfs:
        try:
            with pdf_processor(pdf, "yolo", 300) as processor:
                file_name = pdf.split("\\")[-1]
                print file_name
                number_of_pages = processor.number_of_pages()
                print str(number_of_pages)
                if not number_of_pages > 1:
                    
                    if not new_database.check_if_exists("PDF", "FILE_NAME", file_name):
                        contents = processor.pdf_to_text()
                        path = pdf
                        new_database.insert_row("PDF", file_name, contents, path)
                    else:
                        print "Found duplicate file: " + file_name
                        print "ignoring..."

                number_processed = number_processed + 1
                print "Processed " + str(number_processed) + " out of " + str(len(pdfs)) + " pdfs..."
                percent_complete = round(float(number_processed) / float(len(pdfs)) * 100, 2)
                print str(percent_complete) + "% complete."
        except pyPdf.utils.PdfReadError:
            print "Oh no! EOF marker not found"
            failed_to_read = failed_to_read + 1
            print "Failed to read " + str(failed_to_read) + " files"
            pass

