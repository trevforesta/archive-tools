# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

# format_img.py - given an image or directory of images, this program changes their names to ISO 8601 format.
# Author: Trevor Foresta
# Date Last Modified: 10/07/2021

#TO DO - 
# make this program work with directories:
#  - name folder by year:day and year:earliestday-latestday if necessary.

# -- Import Statements --#
import os, time

#path of file(s)
f_path  = str("C:\\Users\\Trevor\\Desktop\\cats")
#str(input('\n Set Archive Path: '))
os.chdir(f_path)

def format_img(f_path):

    for image in os.listdir(f_path):
        t = os.path.getctime(image)
        t_str = time.ctime(t)
        t_obj = time.strptime(t_str)
        form_t = time.strftime("%Y-%m-%d %H.%M", t_obj)
        image.replace(image, os.path.split(image)[0] + form_t + os.path.splitext(image)[1])

    '''
    # Obtaining the creation time, rename to ISO 8601
    t = os.path.getctime(f_path)
    t_str = time.ctime(t)
    t_obj = time.strptime(t_str)
    form_t = time.strftime("%Y-%m-%d %H:%M", t_obj)
    
    # Replace colon with a similar unicode symbol
    # Modified Letter Colon " " (U+A789)
    form_t = form_t.replace(":", "꞉")
    
    # Renaming the filename to its timestamp
    os.rename(f_path, os.path.split(f_path)[0] + '/' + form_t + os.path.splitext(f_path)[1])
'''
    
format_img(f_path)