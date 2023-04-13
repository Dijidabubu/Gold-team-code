#!/usr/bin/env python3.7

# import the os information
import os

#retrieving the current working directory
current_dir = os.getcwd()

#creating our empty list of dictionaries
dict_list = []

#our for loop to iterate over the items in our directory, extract the info and create the list
for file_name in os.listdir(current_dir):
    file_path = os.path.join(current_dir, file_name)
    file_size = os.path.getsize(file_path)
    last_modified = os.path.getmtime(file_path)
    file_dict = {
        "File name": file_name,
        "Path": file_path,
        "File size": file_size,
        "Last Modified": last_modified
    }
    
    dict_list.append(file_dict)



print(dict_list, sep="\n")