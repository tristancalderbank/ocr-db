# ocr-db
Finds pdfs, strips out text using Google's Tesseract engine, stores in a searchable SQLite database.

I originally developed this while working a job that involved a large amount of scanned technical drawings. This was my attempt to make searching for specific text in these drawings easier. The idea of this project is not to actually use the text retrieved from OCR but to use it as meta-data for searching the documents.

### Features:
- Multipage support
- Adjustable quality (dpi)
- Experimental "moving crop" mode
- GUI

Note: This program was hacked together on a 32-bit windows computer and will probably not run on anything else without tweaking.

### Dependencies:
- Python 2.7
- [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
- [Ghostscript](http://ghostscript.com/download/gsdnld.html)
- [ImageMagick](http://www.imagemagick.org/script/binary-releases.php)
- [pyPdf](https://pypi.python.org/pypi/pyPdf/1.13)
- [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download)

### How to use
- Install all dependencies
- Make sure magick.exe and tesseract.exe are both included in your system PATH variable.
- Choose a folder and the program will search for PDF's and begin OCRing them. This make take a while depending on the quality settings. 
- You can then search the extracted contents using the search bar. 
- Double click a file name in the list to show the contents that were extracted from that file.

![Alt text](/screnshot/main window.png?raw=true "Optional Title")

### How it works
- First we use pyPDF to pull out a page from the PDF 
- We convert that page to a tif image using image magick 
- The image is then feeded into tesseract which outputs a txt file with the scanned contents
- The text from this file is then stored in the SQLite database

### Moving Crop Mode (Experimental)
I read somewhere that Tesseract works better with smaller images. To experiment with this I created a mode where rather than OCRing the whole document we iterate over it with a *moving crop window*. Each crop overlaps the previous one so as to not cut off any text. Using this approach you do end up with a bunch of duplicate text in the database due to the overlap. This didn't matter for my use case though because I only cared about using the text as metadata for seeing if a document contained a certain string or not.


### Future Improvements:
- Support for PDFs with text layers (you don't want to use OCR if the pdf already has a text layer, this would be easy to add using pyPDF)
- Some sort of multicore support as high quality mode (600dpi) is pretty slow 
