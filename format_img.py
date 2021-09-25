# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

# format_img.py - given an image or directory of images, this program changes their names to ISO 8601 format.
# Author: Trevor Foresta
# Date Last Modified: 09/24/2021

#TO DO - 
# make this program work with directories:
#  - name folder by year:day and year:earliestday-latestday if necessary.

# -- Import Statements --#
import os, time

def format_img(): 
    #path of file(s)
    f_path  = "./img.jpg"
    
    # Obtaining the creation time (in seconds)
    # of the file/folder (datatype=int)
    t = os.path.getctime(f_path)
    
    # Converting the time to an epoch string
    # (the output timestamp string would
    # be recognizable by strptime() without
    # format quantifers)
    t_str = time.ctime(t)
    
    # Converting the string to a time object
    t_obj = time.strptime(t_str)
    
    # Transforming the time object to a ISO 8601 timestamp
    form_t = time.strftime("%Y-%m-%d %H:%M", t_obj)
    
    # Replace colon with a similar unicode symbol
    # Modified Letter Colon " " (U+A789)
    form_t = form_t.replace(":", "꞉")
    
    # Renaming the filename to its timestamp
    os.rename(f_path, os.path.split(f_path)[0] + '/' + form_t + os.path.splitext(f_path)[1])