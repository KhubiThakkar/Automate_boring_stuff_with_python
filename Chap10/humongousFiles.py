import os
folder = '/home/khubithakkar/Desktop/noobie/Automate_boring_stuff_with_python/Chap9'
folder = os.path.abspath(folder)

for foldername, subfolders, filenames in os.walk(folder):
    
    for filename in filenames:
        pathfilename = os.path.join(foldername,filename)
        size = os.path.getsize(pathfilename)
        size = size/1000
        if size >= 1:
            print(f'The file/folder to be deleted is {filename}')