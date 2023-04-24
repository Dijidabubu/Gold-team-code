#!/usr/bin/env python3.7
# import the os information
import os

#retrieving the current working directory
current_dir = os.getcwd()

#creating our empty list of dictionaries
l_of_dictionaries = []

#to list all the files and directories in the cwd
dir_contents = os.listdir(current_dir)

print(dir_contents)