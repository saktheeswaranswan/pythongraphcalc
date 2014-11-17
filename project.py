"""Project PSIT Startup at 11/11/2557
Author :    Nathawut Worakijlawan 
            Amita Mongkhonpreedarchai
"""
from Tkinter import *

class mainWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        #menu bar
        self.master.title("MathPro Alpha Version (build 00011) **Name non official**")
        self.master.geometry("840x550")
        self.menubar = Menu(self, tearoff=False)
        self.optionmenu = Menu(self.menubar, tearoff=0)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Save As...', command=saveimage)
        self.filemenu.add_command(label='Exit', command=quit)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=popup_about)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.optionmenu, label="Options")
        self.menubar.add_cascade(menu=self.helpmenu, label="Help")
        self.master.config(menu=self.menubar)
        self.pack()
        
        ####bymimimimi###

        #label for input
        self.text_input = StringVar()
        self.frame_input = LabelFrame(root, text='Enter what you want to calculate', padx=5, pady=2)        
        self.label_frame_input = Entry(self.frame_input, width=100, textvariable = self.text_input)
        self.frame_input.pack(padx=10, pady=10, anchor=NW)
        self.label_frame_input.pack(fill=BOTH, anchor=NW)
        
        #checkbutton for output
        self.var_in = IntVar()
        self.var_graph = IntVar()
        self.var_equa = IntVar()
        self.var_sol = IntVar()
        self.var_int_sol = IntVar()

        self.chck_input = Checkbutton(master, text="Input", variable=self.var_in, command=self.cb_input)
        self.chck_input.pack(anchor=NW)
        self.chck_graph = Checkbutton(master, text="Graph", variable=self.var_graph, command=self.cb_graph)
        self.chck_graph.pack(anchor=NW)
        self.chck_equa = Checkbutton(master, text="Equation", variable=self.var_equa, command=self.cb_equa)
        self.chck_equa.pack(anchor=NW)
        self.chck_sol = Checkbutton(master, text="Solution", variable=self.var_sol, command=self.cb_sol)
        self.chck_sol.pack(anchor=NW)
        self.chck_int_sol = Checkbutton(master, text="Integer Solution", variable=self.var_int_sol, command=self.cb_int_sol)
        self.chck_int_sol.pack(anchor=NW)

        
        #button
        self.b_submit = Button(master, text="Submit", command=self.submit, padx=5, pady=2).pack(side=LEFT)
        self.b_reset = Button(master, text="Reset", command=reset, padx=5, pady=2).pack(side=LEFT)

    
    #function with check button for output 
    #return 1 when check
    #return 0 when don't check
    def cb_input(self):
        print "variable1 is", self.var_in.get()

    def cb_graph(self):
        print "variable2 is", self.var_graph.get()

    def cb_equa(self):
        print "variable3 is", self.var_equa.get()

    def cb_sol(self):
        print "variable4 is", self.var_sol.get()

    def cb_int_sol(self):
        print "variable5 is", self.var_int_sol.get()


    def submit(self):
        '''get input'''
        input = self.text_input.get()
        print input

    



def reset():
    '''for reset button'''
    print 'Reset'

def saveimage():
    '''for save as on file.menubar'''
    print 'saveimage'

def popup_about():
    '''popup in help on menubar'''
    top = Toplevel()
    top.title("About MathPro")
    top.geometry("250x300")

    about_message = 'Hello World'

    msg = Message(top, text=about_message)
    msg.pack()

    button = Button(top, text="Close", command=top.destroy)
    button.pack()  
    
        

root = Tk()
windows = mainWindow(root)
root.mainloop()
