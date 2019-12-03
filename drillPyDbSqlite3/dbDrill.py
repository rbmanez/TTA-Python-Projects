#Drill:   
#   - you will need to write a script that creates a database and adds new
#   data into that database
# 
#Requirements:
#   - Your script will need to use Python 3 and the sqlite3 module.
#   - Your database will require 2 fields, an auto-increment primary integer
#   field and a field with the data type of string.
#   - Your script will need to read from the supplied list of file names at
#   the bottom of this page and determine only the files from the list which
#   ends with a “.txt” file extension.
#   - Next, your script should add those file names from the list ending with
#   “.txt” file extension within your database.
#   - Finally, your script should legibly print the qualifying text files to
#   the console.
#
#Additional Setup Instructions:
#   - The following is the list of file names to use for this drill:
#   fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

import sqlite3

fileList = ('info.docx','hello.txt','myImg.png','myMovie.mpg','world.txt','data.pdf','myPhoto.jpg')

#creating db
conn = sqlite3.connect("dbDrill.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file ("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                "col_file_name TEXT)")
    conn.commit()
conn.close()

#iterating through fileList and adding all files ending with 'txt' into db
conn = sqlite3.connect("dbDrill.db")

with conn:
    cur = conn.cursor()
    for item in fileList:
        if item[-3:] == "txt":
            cur.execute("INSERT INTO tbl_file\
                (col_file_name)\
                VALUES\
                (?)", (item,))
            conn.commit()
conn.close()

#printing everything from db
conn = sqlite3.connect("dbDrill.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_file")
    rows = cur.fetchall()
    print("Data for All Text Files:")
    for row in rows:
        print(row)
