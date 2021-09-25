# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

#get_random_file.py - returns a random file from the archives with a given extension
#TO DO - 
# create csv file
# append 'used' names to csv file (to ensure no repeats)
# wipe csv file when it reaches 365 names (starts over after a year)

import sys, random
from pathlib import Path

def get_random_files(ext, top="F:\OTA Backup (7-20-2020), (7-06-2020)\Photo & Video Archive\[2020]"): 
    file_list = list(Path(top).glob(f"**/*.{ext}"))
    if not len(file_list):
        return f"No files matched that extension: {ext}"
    rand = random.randint(0, len(file_list) - 1)
    return file_list[rand]

if __name__ == '__main__':
    extension = sys.argv[1] if len(sys.argv) > 1 else "*"
    print(get_random_files(extension))