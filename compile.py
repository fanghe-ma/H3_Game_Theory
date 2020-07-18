import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge(source_paths, output_path):
    pdf_writer = PdfFileWriter()

    for path in paths: 
        pdf_reader = PdfFileReader(path) 
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    
    with open(output_path, "wb") as out:
        pdf_writer.write(out)
        print("compiled")

#pass argument 1 in command line for sorting in reverse order

if __name__ == '__main__':
    paths = []
    home = './' 
    for i in os.listdir(home):
        try:
            for j in os.listdir(home + i):
                if j[-3:] == 'pdf':
                    paths.append(home +  i + '/' + j)
        except:
            continue

    print("paths collected")
    merge(paths, './notes.pdf')


    


