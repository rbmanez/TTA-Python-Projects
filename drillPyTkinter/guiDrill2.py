#Drill:
#   - you will need to write a script that creates a GUI with a button widget
#   and a text widget. Your script will also include a function that when it
#   is called will invoke a dialog modal which will allow users with the
#   ability to select a folder directory from their system. Finally, your
#   script will show the user’s selected directory path into the text field
# 
#Requirements:
#   - Your script will need to use Python 3 and the Tkinter module.
#   - Your script will need to use the askdirectory() method from the Tkinter
#   module.
#   - Your script will need to have a function linked to the button widget
#   so that once the button has been clicked will take the user’s selected
#   file path retained by the askdirectory() method and print it within your
#   GUI’s text widget.

from tkinter import *
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #creating the GUI window
        self.master = master
        self.master.title("Check Files")
        self.master.geometry('530x170')

        #creating button
        self.btnBrowse1 = Button(self.master, text="Browse...", width=14, command=lambda: self.browse(1))
        self.btnBrowse1.grid(column=0, row=0, padx=(15, 0), pady=(40, 0))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=14, command=lambda: self.browse(2))
        self.btnBrowse2.grid(column=0, row=1, padx=(15, 0), pady=(10, 0))
        self.btnCheck = Button(self.master, text="Check for files...", height=2, width=14)
        self.btnCheck.grid(column=0, row=2, padx=(15, 0), pady=(10, 0))
        self.btnClose = Button(self.master, text="Close Program", height=2, width=14)
        self.btnClose.grid(column=1, row=2, sticky=E)

        #creating user input field
        self.txt1 = Entry(self.master, width=60)
        self.txt1.grid(column=1, row=0, padx=(25, 0), pady=(40, 0), sticky=N)
        self.txt2 = Entry(self.master, width=60)
        self.txt2.grid(column=1, row=1, padx=(25, 0), pady=(10, 0), sticky=N)

    #take user’s selected file path retained by askdirectory() method and
    #print it within GUI’s text widget
    def browse(self, btn_id):
        self.folder_selected = filedialog.askdirectory()
        if btn_id == 1:
            self.txt1.delete(0,END)
            self.txt1.insert(0,self.folder_selected)
        elif btn_id == 2:
            self.txt2.delete(0, END)
            self.txt2.insert(0, self.folder_selected)

if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()