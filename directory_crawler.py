#import Image
import os
import glob
from subprocess import check_output

class crawler:
    
    master_pdf_list = []
    
    def __init__(self, root):
        self.root = root

    def crawl(self, path=None):

        if path == None:
            path = self.root
        
   	print path     
        os.chdir(path)
       
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

        return self.master_pdf_list
