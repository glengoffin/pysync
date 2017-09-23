#!/usr/bin/env python3
'''
Todo
- Commandline for target URL (with default)
- Deduplicate
'''

"""
Module Docstring
"""
from syncer import sync
import os

__author__ = "Glen Goffin"
__version__ = "0.1.0"
__license__ = "MIT"

def getSourceDirectories():
	list = ['/Volumes/Untitled', '/Users/Glen/Pictures', '/Volumes/NIKON D80', '/Volumes/Seagate 2TB Oct2015/photography']
	return list

def getTargetDir():
	return '/Volumes/glen4tb/rsync-dir'

def main():
    """ Main entry point of the app """
    print("Starting Now")
    # dirsync <sourcedir> <targetdir> [options]
    # sync(sourcedir, targetdir, action, **options)
    sourcedirList = getSourceDirectories()
    targetdir = getTargetDir()
    for sourcedir in sourcedirList:
    	if (os.path.isdir(sourcedir)):
    	    print(sourcedir)
            # sync(sourcedir, targetdir, "sync", -u --ctime --verbose)
            options = {"verbose":True}
            sync(sourcedir, targetdir, "sync", **options)
    print("All Done!")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

# https://pypi.python.org/pypi/dirsync/2.2.2


