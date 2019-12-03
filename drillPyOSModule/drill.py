#Drill:     
#   - you will need to write a script that will check a specific folder on
#   the hard drive, verify whether those files end with a “.txt” file
#   extension and if they do, print those qualifying file names and their
#   corresponding modified time-stamps to the console
#
#Requirements: 
#   - Your script will need to use Python 3 and the OS module.
#   - Your script will need to use the listdir() method from the OS module to
#   iterate through all files within a specific directory.
#   - Your script will need to use the path.join() method from the OS module
#   to concatenate the file name to its file path, forming an absolute path.
#   - Your script will need to use the getmtime() method from the OS module
#   to find the latest date that each text file has been created or modified.
#   - Your script will need to print each file ending with a “.txt” file
#   extension and its corresponding mtime to the console.
# 
# Additional Setup Instructions:
#   - You will need to create a new directory on your system and then create
#   10 different files within this folder. The files that you create should
#   be a combination of any file types you would like just as long as you
#   include at least two that are text documents ending with a “.txt” file
#   extension. This directory will be the directory that your script will
#   need to iterate through to complete the drill.

import os
import time

#creates a list from the contents of current directory
directory = os.listdir(".")

path = "C:\\Users\\Robert\\Documents\\TTA\\projects\\tta-python-projects\\drillPyOSModule"
#iterates through directory:
for file in directory:
    #if file is .txt, open, read, print, close:
    if file.endswith(".txt"):
        f = open(file,"r")
        print(file + " content: ", f.read())
        f.close
        #concatinates path and file to create absolute path to get mtime,
        #then converts mtime to ctime (better readability) then prints it:
        abs_file_path = os.path.join(path,file)
        mtime = os.path.getmtime(abs_file_path)
        ctime = time.ctime(mtime)
        print(file + " time: ", ctime, "\n")
