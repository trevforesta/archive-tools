# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

#pic_of_the_day.py - displays "Archive Pic of the Day", a new random picture each day from the archives
#TO DO - 
# create csv file
# append 'used' names to csv file (to ensure no repeats)
# wipe csv file when it reaches 365 names (starts over after a year)

import random, os
path = "C:\\Users\Trevor\Desktop\Move to Desk\Organize"

random_filename = ""
while(random_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) is False):
    random_filename = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])
else:

    print(random_filename)