import PyPDF2
from os import path, listdir

def read_contents(this_pdf):
    pdfFileObj = open(this_pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    contents = ""
    page = 1
    while(page < pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        contents += pageObj.extractText()
        page += 1

    return contents

dir_path = path.dirname(path.realpath(__file__))
for f in listdir(dir_path+'/../PDFs'):
    print("reading: " + f)
    read_contents(dir_path + '/../PDFs/' + f)
