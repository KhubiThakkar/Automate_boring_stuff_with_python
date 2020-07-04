import zipfile
newZip = zipfile.ZipFile('new.zip','w')
newZip.write('notes.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()