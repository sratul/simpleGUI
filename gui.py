from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("")
# Set geometry (widthxheight)
root.geometry('400x100')
 

# function to display text when
# button is clicked


def disable_event():
    
    pass



class FirstWindow(Toplevel):
    def __init__(self, master = None):
        
        super().__init__(master = master)
        self.title("First Window")
    
        # sets the geometry of toplevel
        self.geometry("400x200")
        
        self.grab_set()
        # A Label widget to show in toplevel
        label1 = Label(self,
            text ="This is a first window").pack()

        newWindowButton = Button(self, text = "Close",
                fg = "red", command=self.destroy).pack()
        
        self.protocol("WM_DELETE_WINDOW", disable_event)


class SecondWindow(Toplevel):
    def __init__(self, master = None):
        
        super().__init__(master = master)
        self.title("Second Window")
    
        # sets the geometry of toplevel
        self.geometry("400x200")
        
        self.grab_set()
        # A Label widget to show in toplevel
        label1 = Label(self,
            text ="This is a Second window").pack()

        newWindowButton = Button(self, text = "Close",
                fg = "red", command=self.destroy).pack()
        
        self.protocol("WM_DELETE_WINDOW", disable_event)




btn_first = Button(root, text = "Open First Window" ,
             fg = "red")



btn_first.bind("<Button>", lambda e: FirstWindow(root))

# set Button grid
btn_first.grid(column=1, row=10)


btn_second = Button(root, text = "Open Second Window" ,
             fg = "green")

btn_second.bind("<Button>", lambda e: SecondWindow(root))

# set Button grid
btn_second.grid(column=3, row=10)


# not the solution we need
btn_system_tray = Button(root, text = "Minimize to System Tray", command= root.iconify)


btn_system_tray.grid(column = 2, row = 20)

# all widgets will be here
# Execute Tkinter
root.mainloop()