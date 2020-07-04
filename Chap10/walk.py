import os
for foldername, subfolders, filenames in os.walk('/home/khubithakkar/Desktop/noobie/Automate_boring_stuff_with_python/Chap2'):
    print('the current folder is' + foldername)

    for subfolder in subfolders:
        print('subfolder of' + foldername +':' + subfolder)

    for filename in filenames:
        print('file inside'+foldername+':'+filename)
    
    print('')
