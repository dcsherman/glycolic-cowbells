#--------------------------------------------------
# Desc:    Script to copy files, compress them  to a separate ZIP file
# Author:  D. C. Sherman
# Version: Python 2.7
#--------------------------------------------------



"""
    It should check if the directories actually exist.
    It should ask for confirmation before doing anything
    I needed the script to backup the specified folder to the specified location.
    It should delete unnecessary files before backing up
    Employs rsync functionality

Writing the script

Check if directory exists

Python actually already has a function that checks if a directory exists: os.path.exists

So all I had to do was to use the built-in function and put it in my own little function, that performs the checks and prints an error-message and exits, if the directory does not exist.

def check_dir_exist(os_dir):
if not os.path.exists(os_dir):
print os_dir, "does not exist."
exit(1)

Confirm on actions

I wanted to let the user confirm or back out of actions before execution.

confirm() was written to ask for confirmation and if the answer is “yes”,
 the variable “exit_condition” should be 0, otherwise it is 1. So when the  function is executed, depending on what status the variable took, I can decide  on how to continue in the script.

def confirm():  
    gogo = raw_input("Continue? yes/no\n")  
    global exit_condition  
    if gogo == 'yes':  
        exit_condition = 0  
        return exit_condition  
    elif gogo == "no":  
        exit_condition = 1  
        return exit_condition  
    else:  
    print "Please answer with yes or no."  
confirm()

Defining backup paths

This one’s simple. The script just asks for user input on the paths for what to 
backup and where to put it. Afterwards there’s the existence-check.

# Specify what and where to backup.  
backup_path = raw_input("What should be backed up today?\n")
check_dir_exist(backup_path)
print "Okay", backup_path, "will be saved."  
time.sleep(3)  
backup_to_path = raw_input("Where to backup?\n")  
check_dir_exist(backup_to_path)

Delete files

I created two functions to delete unnecessary files like temporary or backup files before doing the backup. The first functions takes an argument (file extensions, in this case) as input, searches in the backup path for matching files and deletes them.

def delete_files(ending):
    os.chdir(backup_path)
    for r, d, f in os.walk(backup_path):
        for files in f:
            if files.endswith("." + ending):
                os.remove(os.path.join(r, files))

delete_files() consists of a for-loop that iterates through the file endings, each time asking the user if they wants to delete the files.

# Delete files first
print "First, let's cleanup unnecessary files in the backup path."
file_types = ["tmp", "bak", "dmp"]
for file_type in file_types:
    print "Delete", file_type, "files?"
    confirm()
    if exit_condition == 0:
        delete_files(file_type)

At last, the trash can of the user executing the script is emptied. shutil.rmtree() simply deletes the trash-can directory, which is recreated when a new file is moved to the trash. os.path.expanduser just expands the “~” to the user’s home directory.

# Empty trash can
print "Empty trash can?"
confirm()
if exit_condition == 0:
    print "Emptying!"
    shutil.rmtree(os.path.expanduser("~/.local/share/Trash/files"))

Backing up the files

This is the important part of the script. I searched for an rsync alternative in Python to mimic the desired behavior but I didn’t find anything that was easy to understand, capable of what it should do and not outdated. That is, until I found Rsyncbackup: a Python script “to perform automatic backups using the rsync command”. It does exactly what it says it does, so I included it in my script, in combination with sh. Sh let’s me execute any program as if it were python native.

rsync("-auhv", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc",
  "--exclude=/mnt", "--exclude=/dev", "--exclude=/backup", backup_path, backup_to_path)

Here’s the whole script put together:
"""

#!/usr/bin/env python

import os
import shutil
import time

from sh import rsync

# Functions

def check_dir_exist(os_dir):
    if not os.path.exists(os_dir):
        print os_dir, "does not exist."
        exit(1)

def confirm():
    gogo = raw_input("Continue? yes/no\n")
    global exit_condition
    if gogo == 'yes':
        exit_condition = 0
        return exit_condition
    elif gogo == "no":
        exit_condition = 1
        return exit_condition
    else:
        print "Please answer with yes or no."
        confirm()

def delete_files(ending):
    for r, d, f in os.walk(backup_path):
        for files in f:
            if files.endswith("." + ending):
                os.remove(os.path.join(r, files))

# Specify what and where to backup.
backup_path = raw_input("What should be backed up today?\n")
check_dir_exist(backup_path)
print "Okay", backup_path, "will be saved."
time.sleep(3)

backup_to_path = raw_input("Where to backup?\n")
check_dir_exist(backup_to_path)

# Delete files first
print "First, let's cleanup unnecessary files in the backup path."
file_types = ["tmp", "bak", "dmp"]
for file_type in file_types:
    print "Delete", file_type, "files?"
    confirm()
    if exit_condition == 0:
        delete_files(file_type)

# Empty trash can
print "Empty trash can?"
confirm()
if exit_condition == 0:
    print "Emptying!"
    shutil.rmtree(os.path.expanduser("~/.local/share/Trash/files"))

# Do the actual backup
print "Doing the backup now!"
confirm()
if exit_condition == 1:
        print "Aborting!"
        exit(1)

rsync("-auhv", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc",
  "--exclude=/mnt", "--exclude=/dev", "--exclude=/backup", backup_path, backup_to_path)

