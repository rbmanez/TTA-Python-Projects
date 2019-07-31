#Drill:   - Use python 3 and sqlite3
#         - Create db with 2 columns (id col and string col)
#         - Add all files from fileList ending with "txt" to db
#         - Print qualifying text files to console



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
