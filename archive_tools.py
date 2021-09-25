# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

# archive_tools.py - "main" program that is used to launch other functions
# Author: Trevor Foresta
# Date Last Modified: 09/24/2021

# -- Import Statements --#
import time
import duplicate_checker, format_img, get_random_file

# Constructor
def __init__(self, path):
    self.path = path  

def intro():
    print('___________________')
    print('\n* Archive Tools *')
    print('___________________')
    time.sleep(1)
    print('\nAvailable Tools: ')
    time.sleep(.1)
    print('• Duplicate Checker (d)')
    time.sleep(.1)
    print('• Format to ISO 8601 (f)')
    time.sleep(.1)
    print('• Get Metadata (m)')
    time.sleep(.1)
    print('• Random File (r)')
    time.sleep(1)
    self.path = input('\n Set Archive Path: ')

if __name__ == '__main__':
    intro()
  
