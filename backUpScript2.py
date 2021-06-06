"""
Python Back-Up Script

I wrote this script to backup some important files. 
It backs up the files to a local folder as well as to an external hard drive. 
It creates a new subdirectory which has its name constructed with the current date and time. 
"""

import datetime
import os
import shutil

GOOGLE_DRIVE_DIRECTORY = 'C:\\Users\\Csherman\\Google Drive\\Archive'
MAIN_BACKUP_DIRECTORY = 'C:\\Users\\Csherman\\Desktop\\Archive_Backups\\md_backup_{0}'
EXTERNAL_DRIVE_DIRECTORY = 'F:\\Archive_Backups\\md_backup_{0}'

def get_backup_directory(base_directory):
    date = str(datetime.datetime.now())[:16]
    date = date.replace(' ', '_').replace(':', '')
    return base_directory.format(date)

def copy_files(directory):
    for file in os.listdir(GOOGLE_DRIVE_DIRECTORY):
        file_path = os.path.join(GOOGLE_DRIVE_DIRECTORY, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, directory)

def perform_backup(base_directory):
    backup_directory = get_backup_directory(base_directory)
    os.makedirs(backup_directory)
    copy_files(backup_directory)

def main():
    perform_backup(MAIN_BACKUP_DIRECTORY)
    perform_backup(EXTERNAL_DRIVE_DIRECTORY)

if __name__ == '__main__':
    main()
"""
python python-3.x file-system windows network-file-transfer


You can simplify paths using forward slashes:

GOOGLE_DRIVE_DIRECTORY = 'C:/Users/Csherman/Google Drive/Archive'
MAIN_BACKUP_DIRECTORY = 'C:/Users/Csherman/Desktop/Archive_Backups/md_backup_{0}'
EXTERNAL_DRIVE_DIRECTORY = 'F:/My Files/Archive_Backups/md_backup_{0}'

Instead of converting a date to a string, which may be locale dependent too, 
and then replacing characters in it, better to use strftime to generate exactly 
the format that you want:

def get_backup_directory(base_directory):
    date = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    return base_directory.format(date)

I don't really like global constants inside methods, so I would split copy_files like this:

def copy_files_to(srcdir, dstdir):
    for file in os.listdir(srcdir):
        file_path = os.path.join(srcdir, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dstdir)

def copy_files(dstdir):
    copy_files_to(GOOGLE_DRIVE_DIRECTORY, dstdir)

The advantage of this is that copy_files_to is easier to unit test. 
I think it's also good to use more specific names for the directory variables to 
clarify which one is a source and destination.



I typically create wrapper methods around anything that is specific 
to the target platform [aka, Windows™, Mac™, Linux™, Android™, etc]. I might use 
method names that look like setGoogleDriveDir( ), getExternDriveDir( ), learnBackupDir( ), 
etc. These methods may simply return the platform specific constants, but they may 
also do something complex to supply the needed value using platform specific components. 
For example, adding a system call that discovers the specific platform, then 
switch-case logic to compute appropriate return values. The better to anticipate the 
requirement to run these scripts on multiple platforms in future. 

Remember, "... No one will ever use more than 640 Kb of RAM ..."

"""