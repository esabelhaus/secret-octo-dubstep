import PyPDF2
from tempfile import mkstemp
from os import path, listdir, rename

def read_contents(this_pdf, file_name):
    pdfFileObj = open(this_pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted:
        try:
            pdfReader.decrypt('')
            print('File Decrypted (PyPDF2)')
        except:
            print('giving up on ' + this_pdf)
            rename(this_pdf, this_pdf.replace(file_name, '../encrypted_PDFs/' + file_name))
            return ""
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
    processed = open(dir_path + '/../processed/' + f.replace('.pdf', '.txt'), 'w+')
    processed.write(read_contents(dir_path + '/../PDFs/' + f, f))
    processed.close()
