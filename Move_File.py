import os
import shutil
from_dir = 'C:Admin\Downloads'
to_dir = 'D:\Ayantika\Grade 11\Comp sc\python.whjr\directories\Document_Files'
list_of_files = os.listdir(from_dir)
# print(list_of_files)
for x in list_of_files:
    root, extension = os.path.splitext(x) #to find out what type of file is present in folder
    if extension == ' ':
        break
    if extension == '.pdf' or x == '.txt' or x == '.doc' or x == 'docx':
        path1 = from_dir+'/'+x
        path2 = to_dir+'/' + x
        shutil.move(path1,path2) #moving file
        print(x) #verification if correct files have moved for me