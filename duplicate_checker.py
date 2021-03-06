# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

# duplicate_checker.py - can find, list, and remove duplicate files that may have different names.
# Author: Trevor Foresta
# Date Last Modified: 09/24/2021

# -- Import Statements --#
import os, sys
import hashlib

# -- Function Definitions --#
def findDuplicate(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups


# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found: ')
        print('The content of the following files are identical: ')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
            Join = input('\n Remove duplicate(s)? (y/n) \n')
            if Join in ['y', 'Y']:
                print(str(subresult) + " Deleted\n")
                os.remove(subresult)
            elif Join in ['n', 'N']:
                continue
            else:
                print ("No Answer Given")

    else:
        print('No duplicate files found.')

# ---- Main ----#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDuplicate(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        printResults(dups)
    else:
        print('Usage: python duplicate_checker.py folder or python duplicate_checker.py folder1 folder2 folder3')
