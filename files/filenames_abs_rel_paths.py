#!/usr/bin/env python

import os

os.path.join()                      # cross-platform returns path of strings based on OS
os.sep                              # internal field separator (IFS)
os.getcwd()                         # current working directory (pwd)
os.chdir()                          # cd
os.path.abspath()                   # absolute path of relative file/directory
os.path.isabs()                     # boolean to check absolute path
os.path.relpath()                   # relative path based on working directory
os.path.dirname()                   # strip filename
os.path.basename()                  # strip all but number of fields (NF)
os.path.exists()                    # boolean to check path/file `-e`
os.path.isfile()                    # ... `-f`
os.path.isdir()                     # ... `-d`
os.path.getsize()                   # size in bytes as int `du -b`
os.listdir()                        # `ls`
os.makedirs()                       # `mkdir -p`

total_size = 0
cwd = os.getcwd()
for filename in os.listdir(cwd):
    if not os.path.isfile(os.path.join((cwd), filename)):
        continue
    total_size = total_size + os.path.getsize(os.path.join((cwd), filename))
