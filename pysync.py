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
        # print json.loads(config.get('main', 'sourceDirectories')) # -> "value1"
        # print json.loads(config.get('main', 'targetDirectory')) # -> "value2"
        self.sourceDirectories = json.loads(config.get('main', 'sourceDirectories'))
        self.targetDirectory = json.loads(config.get('main', 'targetDirectory'))
        # self.filename = filename
        # self.sourceDirectories = ['/Volumes/Untitled', '/Users/Glen/Pictures', '/Volumes/NIKON D80', '/Volumes/Seagate 2TB Oct2015/photography']
        # self.targetDirectory = '/Volumes/glen4tb/rsync-dir'


def getPathTail(path):
    (drive, head) = os.path.splitdrive(path)
    while (head != os.sep):
        (head, tail) = os.path.split(head)
        return tail

def main():
    """ Main entry point of the app """
    print("Starting Now")
    cfg = Config("config-file.txt")
    sourcedirList = cfg.sourceDirectories
    targetdir = cfg.targetDirectory
    path = os.path.normpath(targetdir)
    folder_list = iter(path.split(os.sep))
    for folder in folder_list:
        if folder == "Volumes":
            drive = next(folder_list)
            drive = "/Volumes/" + drive
            break
    if (os.path.exists(drive)):
        for sourcedir in sourcedirList:
            if (os.path.isdir(sourcedir)):
                tail = getPathTail(sourcedir)
                newtargetdir = os.path.join(targetdir, tail)
                # print(newtargetdir)
                if not os.path.exists(newtargetdir):
                    os.makedirs(newtargetdir)
                options = {"verbose":True}
                sync(sourcedir, newtargetdir, "sync", **options)
    else:
        print ("Target disk is not mounted.")
    print("All Done!")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()



