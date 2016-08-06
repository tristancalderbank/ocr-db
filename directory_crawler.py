#import Image
import os
import glob
from subprocess import check_output

import debug
from debug import logger

DEBUG_DIRECTORY_CRAWLER = True

if not DEBUG_DIRECTORY_CRAWLER:
    logger.setLevel(debug.logging.INFO)


class crawler:
    """ Recursively crawls a directory looking for files with a given extension.
    """   
 
    matches = []
    extension = '*.pdf'
    
    def __init__(self, root):
        self.root = root

    def crawl(self, path=None):

        if path == None:
            path = self.root
        
        os.chdir(path)
       
        current_dir_contents = os.listdir(path)
        
        directories = []

        for item in current_dir_contents:
            if os.path.isdir(path + "\\" + item):
                directories.append(item)

        if directories != []:
            for folder in directories:
                self.crawl(path + "\\" + folder)

        os.chdir(path)       
        current_dir_matches = glob.glob(self.extension)
        for match in current_dir_matches:
            self.matches.append(path + "\\" + match)

        logger.debug("Directory crawler found a total of %d pdfs." % len(self.matches))
        return self.matches
