#Purpose:   - Create GUI with tkinter
#           - Use askdirectory() from tkinter's filedialog module
#           - Create a function linked to browse button widgets so if button
#           is clicked, it will take user’s selected file path retained by
#           askdirectory() method and print it within GUI’s text widget
#Version:   - Python 3.7



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