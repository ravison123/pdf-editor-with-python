class PdfEditor:
    def __init__(self):
        # Extracting absolute path to be used in self.dir instance
        application_path = os.path.dirname(os.path.abspath(__file__))
        self.dir = application_path
        # Extracting today's date so as that can be appended to the merged file
        date_ = datetime.datetime.now()
        year, month, day = date_.year, date_.month, date_.day
        self.date_string = f'{year}{month}{day}.pdf'
        os.chdir(self.dir)
        # list_pdf : List of all pdf files in the current working directory
        self.list_pdf = []
        for file_ in os.listdir():
            if file_.endswith('.pdf'):
                self.list_pdf.append(file_)

    def merge_files(self, merge_input):
        merged_file_name = f"merged_file_{self.date_string}"
        pdf_writer = PyPDF2.PdfFileWriter()

        # merge_file_list : List of pdf files to be merged
        # 1. All pdf files in the crrent working directory to be merged
        # 2. Provide list of pdf files as input
        if merge_input == '1':
            merge_file_list = self.list_pdf
        else:
            merge_file_list = editor.pdf_file_list()
        print('Merging the files...')
        for file_ in merge_file_list:
            pdf_reader = PyPDF2.PdfFileReader(file_, strict = False)
            for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Create new directory 'merged_folder'
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
        
        # list_pages: list of 1 or 2 integers
        # 1 integer in case of single page to be removed
        # 2 integer in case of range of pages to be removed
        list_pages = page_range.split('-')

        # list_of_pages: Actual list of pages to be removed
        # Formed from list_pages
        # e.g. list_pages = [4, 8], then list_of_pages = [4, 5, 6, 7, 8]
        if len(list_pages) == 2:
            list_of_pages = range(int(list_pages[0]) - 1, int(list_pages[1]))
        else:
            list_of_pages = [int(list_pages[0]) - 1]

        # pdf_writer: pdf writer for removed pages
        # pdf_writer1: pdf writer for edite file (with pages removed)
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
        # If this function returns True, then page numbers provided by user are correct
        # If return value is None, input by user is incorrect
        pdf_reader = PyPDF2.PdfFileReader(file_name, strict = False)
        num_pages = pdf_reader.getNumPages()

        list_pages = page_range.split('-')
        # If input is not in the form of "'page 1' - 'page 2'"
        if len(list_pages) > 2:
            print('Incorrect input for pages')
            return None
        elif len(list_pages) == 2:
            # Checking for non integer values
            try:
                int(list_pages[0])
                int(list_pages[1])
            except:
                print('Incorrect input for pages')
                return None
            # If first number is greater than second
            if int(list_pages[0]) > int(list_pages[1]):
                print('Error, First number in the range is greater than second')
                print('Please provide the input again')
                return None
            # If either number is greater than total number of pages
            if int(list_pages[0]) > num_pages or int(list_pages[1]) > num_pages:
                print('Error, Range of pages entered is greater than total number of pages')
                print('Please provide the input  again')
                return None

        if len(list_pages) == 1:
            # Checking for non integer values
            try:
                int(list_pages[0])
            except:
                print('Incorrect input for pages')
                return None
            # If the number is greater than total number of pages
            if int(list_pages[0]) > num_pages:
                print('Error, page number entered is greater than total number of pages')
                print('Please provide the input  again')
                return None
        return True

    def file_name_check(self, file_name):
        # If this function returns True, then file name provided by user is correct
        # Otherwise the file name is incorrect
        if file_name not in self.list_pdf or file_name.endswith('.pdf') == False:
            print("Error, Please ensure that file name has '.pdf' extension and file is present in the program directory")
            return None
        return True

    def edit_file(self, file_name, page_range, angle):
        pdf_reader = PyPDF2.PdfFileReader(file_name, strict = False)
        num_pages = pdf_reader.getNumPages()
        
        list_pages = page_range.split('-')

        # list_pages: list of 1 or 2 integers
        # 1 integer in case of single page to be edited
        # 2 integer in case of range of pages to be edited

        # list_of_pages: Actual list of pages to be removed
        # Formed from list_pages
        # e.g. list_pages = [4, 8], then list_of_pages = [4, 5, 6, 7, 8]

        if len(list_pages) == 2:
            list_of_pages = range(int(list_pages[0]) - 1, int(list_pages[1]))
        else:
            list_of_pages = [int(list_pages[0]) - 1]

        angle = int(angle)

        pdf_writer = PyPDF2.PdfFileWriter()

        for page in range(num_pages):
            if page in list_of_pages:
                new_page = pdf_reader.getPage(page).rotateClockwise(angle)
                pdf_writer.addPage(new_page)
                continue
            pdf_writer.addPage(pdf_reader.getPage(page))

        newdir = self.dir + '\\' + 'edited_folder'
        try:
            os.mkdir(newdir)
        except:
            None
        os.chdir(newdir)

        edited_file_name = f'edited file {self.date_string}'
        with open(edited_file_name, 'wb') as out:
            pdf_writer.write(out)

        print('The file has been edited successfully!!')

    def angle_check(self, angle):
        # If this function returns True, then angle input provided by user is correct
        angle_list = [0, 90, 180, 270, 360]
        try:
            angle = int(angle)
        except:
            print('Error, Please input integer values for angle')
            return None
        if abs(int(angle)) not in angle_list:
            print('Error, Incorrect input for angle')
            print('Please input angle in multiples of 90 degrees. i.e. 90, 180, 270, 360 etc.')
            return None
        return True

    def pdf_file_list(self):
        # This method takes input from user and returns a list of files
        while True:
            num_of_files = input('Please input number of files to merge: ')
            try:
                num_of_files = int(num_of_files)
            except:
                print('Error, please input an integer value')
                continue
            if int(num_of_files) > len(self.list_pdf):
                print('Error, number provided is greater than total number of pdf files present in program directory')
                continue
            break
        count = 1
        files_list = []
        while count <= num_of_files:
            file_ = input('Please enter name of file num {} '.format(count))
            if file_ not in self.list_pdf:
                print('Error, file not found in program directory')
                print('Ensure that file input has ".pdf" extension')
                continue
            count = count + 1
            files_list.append(file_)
        return files_list

import PyPDF2
import os
import datetime
import sys

print('Instructions for using this program:')
print('1. Please keep the pdf files to merge in the same folder as that of this program (program directory)')
print("2. For Merge files command, merged file will be found in 'merged_file' folder. 'merged_file' folder will be created if not present in the program directory")
print('3. For merge command, if merge all files in program directory is selected; all pdf files in that directory will be merged alphabetically')
print("4. For remove page/s command, please enter a single page number / range of pages to be removed e.g. 1 or 4-8 ")
print("5. For remove page/s command, two files (edited file and remove pages file) will be created in 'remove_folder' folder")
print("6. For edit file command, angle of rotation shall be provided in multiples of 90 degree (max. angle can be provided is 360 degrees)")
print("7. For edit file command, enter positive value of angle for clockwise rotation e.g. +90")
print("8. For edit file command, enter negative value of angle for anti-clockwise rotation e.g. -90")
while True:
    user_input_string = '''Please select what you want to do:
    1. Merge files
    2. Remove page/s
    3. Edit file (rotate pages)
    Press "Enter" to exit: '''
    editor = PdfEditor()
    user_input = input(user_input_string)
    if user_input == "":
        break 
    if user_input == '1':
        merge_string = '''Please select one of the following option:
        1. Merge all files in program directory
        2. Provide a list of files and then merge: '''
        while True:
            merge_input = input(merge_string)
            if merge_input in ['1', '2']:
                break
            print('Error, Incorrect Input. Please enter again')
        editor.merge_files(merge_input)
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
    elif user_input == '3':
        while True:
            file_name = input('Please provide name of the pdf file: ')
            if editor.file_name_check(file_name) == True:
                break
        while True:
            page_range = input('Please enter page / range of pages to be edited: ')
            if editor.page_num_check(file_name, page_range) == True:
                break
        while True:
            angle = input('Please enter angle of rotation: ')
            if editor.angle_check(angle) == True:
                break
        editor.edit_file(file_name, page_range, angle)