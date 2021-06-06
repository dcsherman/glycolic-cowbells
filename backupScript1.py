#--------------------------------------------------
# Desc:    Script to copy files and subfolders, compress them  to a separate ZIP file
# Author:  D. C. Sherman
#--------------------------------------------------

""" 
	Python Back-Up Script
	
	This script preserves directory structure on both Linux and 
    Windows platforms. It uses the shell commands directly in each case, 
    increasing speed compared to normal file operations.
	
"""

import os, os.path
import subprocess
import time
def backUpDir(path):

 """
    Creates backup of the passed old dir and creates a new dir. The backed up dir gets the date and time as the name of the new backed up file.
	
    On success, returns a list consising of two values:
        0: to signify the success
        None: means no error occurred.

    On error, return a list consisting of two values:
        -1 : to signify the failure
        error string: the exact error string
"""

    if os.path.exists(path) == True:
        #dir exists then backup old dir and create new
        backupDir = path + time.strftime('-%Y-%m-%d-%Hh%Mm%Ss')
        
        if os.name == "nt":
            #NT Sysyem  - used the DOS Command 'move' to rename the folder
            cmd = subprocess.Popen(["mov", path, backupDir], \
                                    shell = True, \
                                    stdout = subprocess.PIPE, \
                                    stdin = subprocess.PIPE, \
                                    stderr = subprocess.PIPE)
        elif os.name == "posix":
            #POSIX System - use the appropriate POSIX command to rename the folder.
            cmd=subprocess.Popen(["mv", path, backupDir], \
                                    shell = True, \
                                    stdout = subprocess.PIPE, \
                                    stdin = subprocess.PIPE, \
                                    stderr = subprocess.PIPE)
            pass
        else:
            # Not supported on other platforms
            return [-1, "Not supported on %s platform" %(os.name)]
        (out, err) = cmd.communicate()
        if len(err) != 0:
            return [-1, err]
        else:
            os.mkdir(path)
            return [0, None]
    else:
        #create new dir
        os.mkdir(path)
        return [0, None]
