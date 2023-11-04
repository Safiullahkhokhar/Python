# marge pfd files with the help of PyPDF2 library
from PyPDF2 import PdfWriter
import os 

merage = PdfWriter()

files = [file for file in os.listdir() if file.endswith(".pdf")]
#Create a new list called files and add every file in the current directory to it, but only if the file name ends with the .pdf extension.
for pdf in files:
    merage.append(pdf)
merage.write("Marged_pdf.pdf") # name of the mearge file
merage.close()

# os.listdir()
#returns a list of all files and directories in the current directory.

# Write a program to manipulate pdf files using pyPDF. 
# Your programs should be able to merge multiple pdf files into a single pdf.
#  You are welcome to add more functionalities

# pypdf is a free and open-source pure-python PDF library capable of splitting,
#  merging, cropping, and transforming the pages of PDF files. It can also add
#  custom data, viewing options, and passwords to PDF files. pypdf can retrieve
#  text and metadata from PDFs as well.