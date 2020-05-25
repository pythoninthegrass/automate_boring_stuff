#!/usr/bin/env python3

# SOURCE
# https://www.udemy.com/course/automate/learn/lecture/3470598
# https://realpython.com/read-write-files-python/
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

import os
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code                                                         # 200
res.raise_for_status()                                                  # empty if 200 response; 404 not found
len(res.text)
print(res.text[:500])                                                   # print first 500 words

# download then write file
dl_dir = os.getcwd() + '/resources'
play_file = open(f"{dl_dir}/rj.txt", 'wb')                              # write-binary unicode encoding
for chunk in res.iter_content(100000):
    play_file.write(chunk)
fn = open(f"{dl_dir}/rj.txt")
print(fn.read(500))                                                     # output in bytes
print(fn.read().split()[:500])                                          # list of first 500 words
play_file.close()