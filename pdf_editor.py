import PyPDF2
import os

print('Instructions for using this program:')
print('Please keep the pdf files in the same folder as that of this program')
print('Operation Codes: ')
print('1 : Merge PDFs')


# Taking inputs from user for further processing
file_name = input('Please provide pdf file name: ')
operation = input('Please provide which operation you intend to perform: ')

if operation == '1':
    first_file = input('Please provide name of 1st file: ')
    second_file = input('Please provide name of 2nd file: ')



