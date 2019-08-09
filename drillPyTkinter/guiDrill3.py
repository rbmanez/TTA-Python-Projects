#Purpose:   - use listdir() method from OS module to iterate through all
#           files within a specific directory
#           - use path.join() method from OS module to concatenate the file
#           name to its file path, forming an absolute path
#           - use getmtime() method from OS module to find out the latest
#           date the file has been created or last modified
#           - create a database to record the qualifying file and
#           corresponding modified time-stamp
#           - print each file ending with a “.txt” file extension and its
#           corresponding mtime to the console
#           - use the move() method from the Shutil module to cut all
#           qualifying files and paste them within the destination directory
#Version:   - Python 3.7
#Google:    - python listdir, python path join,
#Notes:     -



from tkinter import *
from tkinter import filedialog
import os, time, sqlite3, shutil

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #creating the GUI window
        self.master = master
        self.master.title("Check Files")
        self.master.geometry('530x170')

        #creating buttons
        self.btnBrowse1 = Button(self.master, text="Starting Directory", width=14, command=lambda: self.start(1))
        self.btnBrowse1.grid(column=0, row=0, padx=(15, 0), pady=(40, 0))
        self.btnBrowse2 = Button(self.master, text="Ending Directory", width=14, command=lambda: self.end(1))
        self.btnBrowse2.grid(column=0, row=1, padx=(15, 0), pady=(10, 0))
        self.btnCheck = Button(self.master, text="Move .txt Files", height=2, width=14, command=lambda: self.move_files())
        self.btnCheck.grid(column=0, row=2, padx=(15, 0), pady=(10, 0),)
        self.btnClose = Button(self.master, text="Close Program", height=2, width=14, command=self.master.destroy)
        self.btnClose.grid(column=1, row=2, sticky=E)

        #creating user input field
        self.txt1 = Entry(self.master, width=60)
        self.txt1.grid(column=1, row=0, padx=(25, 0), pady=(40, 0), sticky=N)
        self.txt2 = Entry(self.master, width=60)
        self.txt2.grid(column=1, row=1, padx=(25, 0), pady=(10, 0), sticky=N)



    #take user’s selected initial folder path retained by askdirectory()
    #method and print it within GUI’s text widget
    def start(self, btn_id):
        self.initial_folder = filedialog.askdirectory()
        self.txt1.delete(0, END)
        self.txt1.insert(0, self.initial_folder)
        #create a list from initial folder directory
        self.directory = os.listdir(self.initial_folder)
        return self.directory, self.initial_folder

    #take user’s selected destination folder path retained by askdirectory()
    #method and print it within GUI’s text widget
    def end(self, btn_id):
        self.destination_folder = filedialog.askdirectory()
        self.txt2.delete(0, END)
        self.txt2.insert(0, self.destination_folder)
        return self.destination_folder

    #move .txt files from initial folder to destination folder and create db
    def move_files(self):
        txtdirectory = []
        timelist = []
        #iterate through starting directory list
        for file in self.directory:
            if file[-4:] == ".txt":
                full_path = "{}/{}".format(self.initial_folder, file)
                timestamp = time.ctime(os.path.getmtime(full_path))
                #print .txt file path and corresponding timestamp to console
                print("fullpath: {}".format(full_path))
                print("timestamp: {}".format(timestamp))
                #append .txt files to txtdirectory and .txt timestamps to timelist
                txtdirectory.append(full_path)
                timelist.append(timestamp)
                #move .txt to destination folder
                shutil.move(full_path, self.destination_folder)

        #create db table
        conn = sqlite3.connect('db.db')
        with conn:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE if not exists tbl_file
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                col_filename text,
                col_timestamp text)''')
        conn.close()

        #insert data into table
        conn = sqlite3.connect('db.db')
        with conn:
            #iterate through txtdirectory and timelist and insert them into table
            for file, ts in zip(txtdirectory, timelist):
                cur = conn.cursor()
                cur.execute('''INSERT INTO tbl_file
                    (col_filename, col_timestamp)
                    VALUES
                    (?, ?)''', (file, ts))
                conn.commit()
        conn.close()




if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()