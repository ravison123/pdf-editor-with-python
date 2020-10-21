class PdfEditor:
    def __init__(self):
        self.dir = os.path.dirname(__file__)
        date_ = datetime.datetime.now()
        # Extracting today's date so as that can be appended to the merged file
        year, month, day = date_.year, date_.month, date_.day
        self.date_string = f'{year}{month}{day}.pdf'
        os.chdir(self.dir)
        self.list_pdf = []
        for file_ in os.listdir():
            if file_.endswith('.pdf'):
                self.list_pdf.append(file_)

    def merge_files(self):
        merged_file_name = f"merged_file_{self.date_string}"
        print('Merging the files:')
        pdf_writer = PyPDF2.PdfFileWriter()

        for file_ in self.list_pdf:
            pdf_reader = PyPDF2.PdfFileReader(file_, strict = False)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        newdir = self.dir + '\\' + 'merged_folder'
        try:
            os.mkdir(newdir)
        except:
            None
        os.chdir(newdir)
        with open(merged_file_name, 'wb') as out:
            pdf_writer.write(out)

        print('Files merged successfully!!')

    def remove_pages(self, file_name, page_range):
        pdf_reader = PyPDF2.PdfFileReader(file_name, strict = False)
        num_pages = pdf_reader.getNumPages()
        
        list_pages = page_range.split('-')

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
        
        newdir = self.dir + '\\' + 'remove_folder'
        try:
            os.mkdir(newdir)
        except:
            None
        os.chdir(newdir)
        removed_file_name = f'removed pages {self.date_string}'
        edited_file_name = f'edited file {self.date_string}'
        with open(removed_file_name, 'wb') as out:
            pdf_writer.write(out)
        with open(edited_file_name, 'wb') as out:
            pdf_writer1.write(out)

        print('Specified pages successfully removed from the file!!')

    def page_num_check(self, file_name, page_range):
        pdf_reader = PyPDF2.PdfFileReader(file_name, strict = False)
        num_pages = pdf_reader.getNumPages()

        list_pages = page_range.split('-')
        if len(list_pages) > 2:
            print('Incorrect input for pages')
            return None
        elif len(list_pages) == 2:
            try:
                int(list_pages[0])
                int(list_pages[1])
            except:
                print('Incorrect input for pages')
                return None
            if int(list_pages[0]) > int(list_pages[1]):
                print('Error, First number in the range is greater than second')
                print('Please provide the input again')
                return None
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
            if int(list_pages[0]) > num_pages:
                print('Error, page number entered is greater than total number of pages')
                print('Please provide the input  again')
                return None
        return True

    def file_name_check(self, file_name):
        if file_name not in self.list_pdf or file_name.endswith('.pdf') == False:
            print("Error, Please ensure that file name has '.pdf' extension and file is present in the program directory")
            return None
        return True

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
editor = PdfEditor()
if user_input == '1':
    editor.merge_files()
elif user_input == '2':
    while True:
        file_name = input('Please provide name of the pdf file: ')
        if editor.file_name_check(file_name) == True:
            break
    while True:
        page_range = input('Please enter page / range of pages to be removed: ')
        if editor.page_num_check(file_name, page_range) == True:
            break
    editor.remove_pages(file_name, page_range)