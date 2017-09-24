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
from ConfigParser import SafeConfigParser
import json

__author__ = "Glen Goffin"
__version__ = "0.1.0"
__license__ = "MIT"

class Config(object):
    """ Manages the config file """
    def __init__(self, filename):
        config = SafeConfigParser()
        config.read('config.ini')
        print json.loads(config.get('main', 'sourceDirectories')) # -> "value1"
        print json.loads(config.get('main', 'targetDirectory')) # -> "value2"
        self.sourceDirectories = json.loads(config.get('main', 'sourceDirectories'))
        self.targetDirectory = json.loads(config.get('main', 'targetDirectory'))
        # self.filename = filename
        # self.sourceDirectories = ['/Volumes/Untitled', '/Users/Glen/Pictures', '/Volumes/NIKON D80', '/Volumes/Seagate 2TB Oct2015/photography']
        # self.targetDirectory = '/Volumes/glen4tb/rsync-dir'


def main():
    """ Main entry point of the app """
    print("Starting Now")
    cfg = Config("config-file.txt")
    sourcedirList = cfg.sourceDirectories
    targetdir = cfg.targetDirectory
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


