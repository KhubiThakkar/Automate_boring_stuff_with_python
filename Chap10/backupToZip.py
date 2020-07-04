#! python3
#backupToZip.py - copies an entire and its contents into a ZIP file whose filename inrements
import zipfile,os

def backupToZip(folder):
    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number+=1
    
    print(f'Creating {zipFilename}...')
    
    backupZip = zipfile.ZipFile(zipFilename,'w')

    for foldername,subfolder,filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))

    backupZip.close()
    print('Done!!')


backupToZip('/home/khubithakkar/Desktop/noobie/Automate_boring_stuff_with_python/Chap9')