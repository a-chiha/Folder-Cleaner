#!/usr/bin/env python
import os
from datetime import datetime
import time


folder_path = input("Enter the folder path (or press Enter to use the current directory): ").strip()


if not folder_path:
    folder_path = "C:\\Users\\achih\\Downloads"

min_time_alive = 3600 * 100  # 2 hours in seconds


file_list = os.listdir(folder_path)
for file in file_list:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):  
        check_date = os.path.getmtime(file_path)
        time_since_creation = datetime.fromtimestamp(check_date)
        elapsed_time = (datetime.now() - time_since_creation).total_seconds()

        # Check if the file is older than 2 hours
        
        if elapsed_time < min_time_alive:
            print(f"File '{file}' is not old enough. Not up for deletion.")
        else:
            print(f"File '{file}' is older than 4 days. Deleting...")
            #os.remove(file_path)
            print(f"File '{file}' has been deleted.")
print("Here are the files in Download",os.listdir(folder_path))
input("\nPress Enter to exit...")