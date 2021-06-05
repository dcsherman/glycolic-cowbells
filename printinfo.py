"""
	[https://pymotw.com/2/zipfile/index.html]
"""

import datetime
import zipfile

def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print(info.filename)
        print('\tComment:\t', info.comment)
        print('\tModified:\t', datetime.datetime(*info.date_time))
        print('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print('\tZIP version:\t', info.create_version)
        print('\tCompressed:\t', info.compress_size, 'bytes')
        print('\tUncompressed:\t', info.file_size, 'bytes')
        print

if __name__ == '__main__':
    print_info('new.zip')

"""
	I can use this to get the information I need about the creation date of each file on the archive. Pull out the modified time, write it to a separate file along with the name, and use that file for each directory file to see if it should be archived or skipped.
"""
