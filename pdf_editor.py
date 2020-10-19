import PyPDF2
import os

print('Instructions for using this program:')
print('Please keep the pdf files in the same folder as that of this program')
print('Operation Codes: ')
print('1 : Merge PDFs')

os.chdir(r'C:\Users\sonaw\OneDrive\Desktop\Projects\pdf-editor-with-python')

# Taking inputs from user for further processing
operation = input('Please provide which operation you intend to perform: ')

if operation == '1':
    first_file = input('Please provide name of 1st file: ')
    second_file = input('Please provide name of 2nd file: ')


file_list = [first_file, second_file]
pdf_writer = PyPDF2.PdfFileWriter()

for file_ in file_list:
    pdf_reader = PyPDF2.PdfFileReader(file_, strict = False)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
with open('merged_file.pdf', 'wb') as out:
    pdf_writer.write(out)