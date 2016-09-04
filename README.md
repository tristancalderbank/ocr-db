# ocr-db
Finds pdfs, strips out text using Google's Tesseract engine, stores in a searchable SQLite database.

I originally developed this while working a job that involved a large amount of scanned technical drawings. This was my attempt to make searching for specific text in these drawings easier. 

Features:
- Multipage support
- Adjustable quality (dpi)
- GUI


Dependencies:
- Python 2.7
- [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
- [ImageMagick](http://www.imagemagick.org/script/binary-releases.php)
- [pyPdf](https://pypi.python.org/pypi/pyPdf/1.13)
- [PyQt4](https://www.riverbankcomputing.com/software/pyqt/download)

### How to use
Once you've installed all the dependencies, just choose a folder and the program will search for PDF's and begin OCRing them. This make take awhile depending on the quality settings. You can then search the extracted contents using the search bar. Double click a file name in the list to show the contents that were extracted from that file.

