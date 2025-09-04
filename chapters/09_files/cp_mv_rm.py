#!/usr/bin/env python

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

# tree (walk directory)
os.getcwd()
for dir_name, sub_dirs, fn in os.walk('.'):
    # OG (str cat)
    # print('The folder is ' + dir_name)
    # print('The subfolders in ' + dir_name + ' are: ' + str(sub_dirs))
    # print('The filenames in ' + dir_name + ' are: ' + str(fn))
    # print()

    # MYNE (f-strings)
    print(f'The folder is {dir_name}')
    print(f'The subfolders in {dir_name} are: {sub_dirs}')
    print(f'The filenames in {dir_name} are: {fn}\n')

    # find . -name "fish" -type d -exec rm {} \;
    # for sub_dir in sub_dirs:
    #     if 'fish' in sub_dir:
    #         os.rmdir(sub_dir)
    #         print('rm -rf on' + sub_dir)

    # find . -name "*.py" -type f -exec cp {}{,.bak} \;
    # for f in fn:
    #     if f.endswith('.py'):
    #         shutil.copy(os.join(dir_name, f), os.join(dir_name, f + '.bak'))
