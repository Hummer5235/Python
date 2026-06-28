import zipfile,os
my_zip = zipfile.ZipFile('files.zip','w')

my_zip.write('New.txt')
my_zip.close()