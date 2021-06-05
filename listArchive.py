"""
	Date:     2017-09-24
	Refernce: Sweigart(2015), p.204
	Project:  joutsenet-muutavat
	Usage:    Possibly suitable to pull up a list of candidate files from which a list of backup-able files might be drawn. Is there a module to be imported to take care of that Unicode problem in the namelist() method?
"""
import zipfile, os
os.chdir('G:\\') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('2017-01-docs.zip')
manifest = exampleZip.namelist()
print(manifest)

"""

C:\tmp>y:\listArchive.py
Traceback (most recent call last):
  File "Y:\listArchive.py", line 5, in <module>
    print(manifest)
  File "C:\Python35\lib\encodings\cp437.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_map)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '\u2014' in position
1162: character maps to <undefined>

C:\tmp>
"""
