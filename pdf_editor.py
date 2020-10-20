def merge_files():
    os.chdir(os.path.dirname(__file__))
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

    newdir = os.path.dirname(__file__) + '\\' + 'merged_folder'
    try:
        os.mkdir(newdir)
    except:
        None
    os.chdir(newdir)
    with open(merged_file_name, 'wb') as out:
        pdf_writer.write(out)

def remove_pages():
    os.chdir(os.path.dirname(__file__))
    file_name = input('Please enter pdf file name:')
    if file_name.endswith('.pdf') == False:
        print("Please enter file name including '.pdf' extension")
        return None
    if file_name not in os.listdir():
        print("File not found in the working directory")
        return None
        
    pdf_reader = PyPDF2.PdfFileReader(file_name, strict = False)
    num_pages = pdf_reader.getNumPages()

    pages_to_remove = input('Please enter page / range of pages to be removed: ')
    list_pages = pages_to_remove.split('-')
    if len(list_pages) > 2:
        print('Incorrect input for pages')
        return None
    if len(list_pages) == 2:
        try:
            int(list_pages[0])
            int(list_pages[1])
        except:
            print('Incorrect input for pages')
            return None
    if len(list_pages) == 2:
        if int(list_pages[0]) > int(list_pages[1]):
            print('Error, First number in the range is greater than second')
            print('Please provide the input again')
            return None
    if len(list_pages) == 2:
        if int(list_pages[0]) > num_pages or int(list_pages[1]) > num_pages:
            print('Error, Range of pages entered is greater than total number of pages')
            print('Please provide the input  again')
            return None

    if len(list_pages) == 1:
        try:
            int(list_pages[0])
        except:
            print('Incorrect input for pages')
            return None
    if len(list_pages) == 1:
        if int(list_pages[0]) > num_pages:
            print('Error, page number entered is greater than total number of pages')
            print('Please provide the input  again')
            return None

    if len(list_pages) == 2:
        list_of_pages = range(int(list_pages[0]) - 1, int(list_pages[1]))
    else:
        list_of_pages = [int(list_pages[0]) - 1]

    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer1 = PyPDF2.PdfFileWriter()

    for i in range(num_pages):
        if i in list_of_pages:
            pdf_writer.addPage(pdf_reader.getPage(i))
            continue
        pdf_writer1.addPage(pdf_reader.getPage(i))
    
    newdir = os.path.dirname(__file__) + '\\' + 'remove_folder'
    try:
        os.mkdir(newdir)
    except:
        None
    os.chdir(newdir)
    with open('removed pages.pdf', 'wb') as out:
        pdf_writer.write(out)
    with open('edited file.pdf', 'wb') as out:
        pdf_writer1.write(out)

import PyPDF2
import os
import datetime

print('Instructions for using this program:')
print('1. Please keep the pdf files to merge in the same folder as that of this program')
print("2. Merged file will be found in 'merged_file' folder")
print('3. For merge command, all .pdf files in the program directory will be meged together')
print("4. For merge command, the merged .pdf file will be found in the folder 'merged_file'")
print("5. For remove page/s command, please enter a single page number to be removed / enter range of pages to be removed e.g. 4-8 ")
user_input_string = '''Please select what you want to do:
1. Merge files
2. Remove page/s
3. Edit file (rotate pages)'''
user_input = input(user_input_string)
if user_input == '1':
    merge_files()
elif user_input == '2':
    remove_pages()