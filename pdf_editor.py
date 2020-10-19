def merge_files():
    os.chdir(r'C:\Users\sonaw\OneDrive\Desktop\Projects\pdf-editor-with-python')
    # Extracting today's date so as that can be appended to the merged file
    date_ = datetime.datetime.now()
    year, month, day = date_.year, date_.month, date_.day
    merged_file_name = f"merged_file_{year}{month}{day}.pdf"
    print('Merging the files:')
    pdf_writer = PyPDF2.PdfFileWriter()

    for file_ in os.listdir():
        if file_.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfFileReader(file_, strict = False)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

    os.chdir(r'C:\Users\sonaw\OneDrive\Desktop\Projects\pdf-editor-with-python\merged_file')
    with open(merged_file_name, 'wb') as out:
        pdf_writer.write(out)

import PyPDF2
import os
import datetime

print('Instructions for using this program:')
print('1. Please keep the pdf files to merge in the same folder as that of this program')
print("2. Merged file will be found in 'merged_file' folder")
merge_files()
