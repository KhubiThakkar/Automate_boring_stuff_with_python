import os
os.chdir('/home/khubithakkar/Desktop/OnlineClass/femh1dd')

for f in os.listdir():
    filename,fileext = os.path.splitext(f)
    file_name = filename[5:7]
    newname = 'std6{}'.format(file_name)
    os.rename(f,newname)