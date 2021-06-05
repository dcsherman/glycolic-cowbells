#!/usr/bin/env python
# coding=utf-8
# filename : backup_ver1.py

import os
import time

# set the file you need backup
source='/home/grace/python/'

# set the dir you store the backup file
target_dir='/home/grace/test/'

# backup filename 
target=target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'

# set zip command 
zip_command="zip -qr '%s' %s" %(target,''.join(source))

#Run the zip_command
if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup Failed!'