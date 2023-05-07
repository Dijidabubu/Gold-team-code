import os

def get_file_info(path="."):
    dict_list = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            last_modified = os.path.getmtime(file_path)
            file_dict = {
                "File name": file_name,
                "Path": file_path,
                "File size": file_size,
                "Last Modified": last_modified
            }
            dict_list.append(file_dict)
    return dict_list
