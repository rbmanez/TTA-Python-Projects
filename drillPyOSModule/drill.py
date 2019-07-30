#Drill:         script will check current folder on hard drive for '.txt'
#               files, print all '.txt' files and its corresponding mtime to
#               the console
#
#Requirements:  - use python 3 and os module
#               - listdir() to iterate through files
#               - path.join() to concatenate file name to file path to create
#               absolute path
#               - getmtime() to find latest date each text file has been created or modified


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
