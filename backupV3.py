#!/usr/bin/env python
# coding=utf-8
# filename : backup_ver3.py
import os
import time

source='/home/csherman/python/'
target_dir='/home/archive/docs/'

today=target_dir+time.strftime('%Y%m%d')

now = time.strftime("%H%M")

comment=raw_input('Enter comment->')

if(comment==0):
    target=today+os.sep+now+'.zip'
else:
    target = today + os.sep+now +'_'+\
            comment.replace(' ','_')+'.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully create directory',today

zip_command="zip -qr '%s' %s" %(target,''.join(source))

if os.system(zip_command)==0:
    print 'Successful backup to',target
else:
    print 'Backup Failed!'