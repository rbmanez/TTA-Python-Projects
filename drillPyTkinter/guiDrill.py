#Purpose:   - Create GUI with tkinter
#Version:   - Python 3.7



from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        #creating the GUI window
        self.master = master
        self.master.title("Check Files")
        self.master.geometry('530x170')

        #creating button
        self.btnBrowse1 = Button(self.master, text="Browse...", width=14)
        self.btnBrowse1.grid(column=0, row=0, padx=(15, 0), pady=(40, 0))
        self.btnBrowse2 = Button(self.master, text="Browse...", width=14)
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



if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()