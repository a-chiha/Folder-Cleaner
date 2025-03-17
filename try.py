import os
import random
import datetime
from pathlib import Path
import time
import shutil
#https://realpython.com/python-gui-tkinter/
print("Hello, this program is written by Ahmad Chiha.\n")
print("The points of this program is to help you keep your pc as optimized as possible.\n")
print("This is done by deleting the files that is downloaded to save space.\n")
deletfolder="C:\\Users\\achih\\Desktop\\test\\" #erstat med ønskede folder
files = os.listdir(deletfolder)
minimumtime_alive = 25.0* 60.0
#files = [f for f in os.listdir(deletfolder) if os.path.isfile(f)]
#print(files)
folder_path = Path(deletfolder)
# if file if folder
for f in files:
    file_path = folder_path / f
    path = file_path.resolve()
    print(path)
    creationtime=os.path.getctime(path)
    current_time=time.time()
    elapsed_time=current_time - creationtime
    print("This file has been created at:",time.ctime(creationtime))
    # tjek internet for validering om det er fil eller mappe og lav til if statement brug contine.
    if elapsed_time < minimumtime_alive:
        print("file is too new to securly delete please wait!")
        continue
    if os.path.exists(deletfolder):
        print("The folder exsists:")
        print("Beginning to delete unused files:")
        #shutil.rmtree(path) #ignore_errors=True if its readonly
        os.remove(path)
        print("File has been deleted")
    else:
        print("file has not been deleted")
#lav validering på om det er en mappe eller fil
#recursion i forhold til at slette elemente

