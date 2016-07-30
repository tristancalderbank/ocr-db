from subprocess import check_output
import time
import pyPdf

import debug
from debug import logger

# flags
DELETE_BUFFER_FILES = False 
DEBUG_IMAGE_PROCESSING = True

if not DEBUG_IMAGE_PROCESSING:
    logger.setLevel(debug.logging.INFO)


def path_to_filename(path):
    """ Returns filename from path by keeping after last '\'

    """
    return path.split("\\")[-1]

class buffer_file:
    def __init__(self):
        pass

class image_magick:

    dpi = 600

    def __init__(self, input_file):
        self.input_file = input_file
        self.width = self.get_width()
        self.height = self.get_height()

    def get_width(self):
        return check_output('magick identify -format "%w" ' + self.input_file, shell=True)

    def get_height(self):
        return check_output('magick identify -format "%h" ' + self.input_file, shell=True)

    def crop(self, output_file, width, height, h_offset, v_offset):
        shell_command = 'magick -density {} {} -crop {}%x{}%+{}+{} {}'.format(self.dpi, self.input_file, width, height, h_offset, v_offset, output_file)
        logger.debug(shell_command)
        check_output(shell_command)

    def split(self, output_file, percent_width, percent_height):
        shell_command = 'magick -density {4} {0} -crop {1}%x{2}% -depth 8 {3}'.format(input_file.name, percent_width, percent_height, output_file, dpi)
        logger.debug(shell_command)
        check_output(shell_command)


class buffer_file:
    
    # different buffer files will be created for processing
    # this parent class lets them all delete
    # themselves automatically using the 'with' construct
     
    def __init__(self):
        pass

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if DELETE_BUFFER_FILES:
            try:
                os.remove(self.name)
            except WindowsError:
                print "Couldn't find buffer files to delete"


class pdf:
    """The actual pdf to be processed.

    May contain multiple pages
    
    Attributes:
        name (str): filename
        path (str): path to file
        
    """

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.number_of_pages = self.get_number_of_pages()

    def get_number_of_pages(self):
        with open(self.path, "rb") as input_file:
            pdf = pyPdf.PdfFileReader(input_file)
            return pdf.numPages

class pdf_page(buffer_file):

    name = "pdf_page_buffer.pdf"

    def __init__(self, input_pdf, page):
        input_file = pyPdf.PdfFileReader(open(input_pdf.name, "rb"))

        output = pyPdf.PdfFileWriter()
        output.addPage(inputpdf.getPage(page))    
        with open(self.name, "wb") as output_file:
            output.write(output_file)
   
class tif_crop(buffer_file):

    name = "tif_crop_buffer.tif"

    def __init__(self, input_pdf, width, height, h_offset, v_offset):
        image_editor = image_magick(input_pdf.name)
        image_editor.crop(self.name, width, height, h_offset, v_offset)



"""
class tif_page(buffer_file):

    name = "tif_page_buffer.tif"
    dpi = 600
     
    def __init__(self, input_path):
        self.input_path = input_path
        image_editor = image_magick(self.input_path)
        image_editor.convert_to_tiff(self.input_path, self.name, self.dpi)
     
        # get attributes
        image_editor = image_magick(self.name)
        self.width = image_editor.width
        self.height = image_editor.height
"""   











     
