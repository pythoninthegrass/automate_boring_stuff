#!/usr/bin/env python3

import glob
import os
import shutil

# cp ./resources/hello.txt ~/Downloads
os.getcwd()                                                                     # pwd
shutil.copy('./resources/hello.txt', '../../Downloads')                         # cp
os.listdir('../../Downloads')                                                   # ls
os.remove('../../Downloads/hello.txt')                                          # rm

# cp ./resources/hello.txt ~/Downloads/hello.txt && mv hello.txt hellohello.txt
shutil.copy('./resources/hello.txt', '../../Downloads/hellohello.txt')          # cp/mv (rename)
os.listdir('../../Downloads')                                                   # ls
os.remove('../../Downloads/hellohello.txt')                                     # rm

# cp -r ./resources ~/Downloads
shutil.copytree('./resources', '../../Downloads', dirs_exist_ok=True)           # cp -r
os.listdir('../../Downloads')                                                   # ls

# mkdir -p ~/Downloads/temp
try:
    os.makedirs('../../Downloads/temp')
except FileExistsError as exists:
    print('Folder already exists')

# mv ~/Downloads/* ~/Downloads/temp
# files = glob.glob('../../Downloads/*', recursive=False)                       # doesn't exclude temp/
files = [fn for fn in glob.glob('../../Downloads/*', recursive=False)
        if not os.path.basename(fn).startswith('temp')]
# print(files)
for f in files:
    shutil.move(f, '../../Downloads/temp')
os.listdir('../../Downloads')
os.listdir('../../Downloads/temp')

# mv ~/Downloads/temp ~/Downloads/resources (rename dir)
shutil.move('../../Downloads/temp', '../../Downloads/resources')
os.listdir('../../Downloads')
os.listdir('../../Downloads/resources')

# rm ~/Downloads/resources/bacon.txt
os.unlink('../../Downloads/resources/bacon.txt')
os.listdir('../../Downloads/resources')

# rm -rf ~/Downloads/resources
# shutil.rmtree('../../Downloads/resources')                                    # DANGER ZONE
for fn in os.listdir('../../Downloads/resources'):
    if fn.endswith('.txt'):
        print(fn)
        # os.unlink(fn)
