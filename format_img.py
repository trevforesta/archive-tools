# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

#format_img.py - given an image or directory of images, this program changes their names to ISO 8601 format.
#TO DO - 
# make this program work with directories:
#  - name folder by year:day and year:earliestday-latestday if necessary.

import time, os
  
# Getting the path of the file
#f_path = "/location/to/gfg.png"
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
  
# Transforming the time object to a timestamp
# of ISO 8601 format
form_t = time.strftime("%Y-%m-%d %H:%M", t_obj)
  
# Since colon is an invalid character for a
# Windows file name Replacing colon with a
# similar looking symbol found in unicode
# Modified Letter Colon " " (U+A789)
form_t = form_t.replace(":", "꞉")
  
# Renaming the filename to its timestamp
os.rename(
    f_path, os.path.split(f_path)[0] + '/' + form_t + os.path.splitext(f_path)[1])