#--------------------------------------------------
# Desc:    Script to copy files, compress them  to a separate ZIP file
# Author:  D. C. Sherman
# Version: Written in Python 2.7
#--------------------------------------------------

import os
import zipfile
import shutil

#copy files and folder and compress into a zip file
def doprocess(source_folder, target_zip):
    zipf = zipfile.ZipFile(target_zip, "w")
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            print (os.path.join(subdir, file))
            zipf.write(os.path.join(subdir, file))

    print ("Created ", target_zip)

#copy files to a target folder 
#def docopy(source_folder, target_folder):
#   for subdir, dirs, files in os.walk(source_folder):
#       for file in files:
#           print (os.path.join(subdir, file))
#           shutil.copy2(os.path.join(subdir, file), target_folder)

if __name__ =='__main__':
    print ('Starting execution')

#compress to zip
    source_folder = 'C:\\temp'
    source_files = 'C:\\temp\\*.*'
    target_zip = 'C:\\incoming\\dummydata.zip'
    doprocess(source_folder, target_zip)   

#copy to backup folder
#   source_folder = 'D:\\data\\mp3files'
#   target_folder = 'e:\\backups\\mp3backup'
#   docopy(source_folder, target_folder)

    print ('Ending execution')
	
""" 
	Code ZIP's up the folder containing the target files. Rewrite so only the 
    files are archived, without the folder structure. And make sure subfolders, 
    if any, are excluded. 

"""


