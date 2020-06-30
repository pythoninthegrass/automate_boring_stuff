#!/usr/bin/env python3

# SOURCES:
# https://www.udemy.com/course/automate/learn/lecture/3470622#overview
# https://stackoverflow.com/a/37104252

import glob
import os
import PyPDF2

# `cd` to directory with *.pdf
cwd = os.getcwd() + '/resources'
os.chdir(cwd)

# open pdf object
pdf_file = open('meetingminutes.pdf', 'rb')        # read-binary vs. read-only

# feed pdf to PyPDF2
reader = PyPDF2.PdfFileReader(pdf_file)
reader.numPages

# parse first page of pdf
page = reader.getPage(0)
page.extractText()

# read all pages in the pdf
for page_num in range(reader.numPages):
    print(reader.getPage(page_num).extractText())

# TODO: QA for loops to match video
# UGLY-INEFFICIENT
pdf_file1 = open('./meetingminutes.pdf')
pdf_file2 = open('./meetingminutes2.pdf')

writer = PyPDF2.PdfFileWriter()

reader1 = PyPDF2.PdfFileReader(pdf_file1)
reader2 = PyPDF2.PdfFileReader(pdf_file1)

for page_num in range(reader1.numPages):
    page = reader1.getPage(page_num)
    writer.addPager(page)

for page_num in range(reader2.numPages):
    page = reader2.getPage(page_num)
    writer.addPager(page)

out = open('combinedminutes.pdf', 'wb')             # write-binary
writer.write(out)

out.close()
pdf_file1.close()
pdf_file2.close()

# ELEGANT
# setup dictionary with filenames as keys
files = {}                                          # init dict
for fn in glob.iglob("./*minutes*.pdf"):
    print(fn)                                       # ./meetingminutes.pdf
    file_contents = open(fn, 'rb').read()
    files[fn] = file_contents
files.keys()                                        # dict_keys(['./meetingminutes.pdf', './meetingminutes2.pdf'])

# TODO: loop thru keys to scrape text > cat output file > close all files
for page_num in range(.num_pages):
    page = reader1.getPage(page_num)
    writer.addPager(page)

# TODO: compare ugly combo pdf w/elegant combo pdf