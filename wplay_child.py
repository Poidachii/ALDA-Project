from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import main

class child_window():

    def __init__(self, root, decision):
        self.root = root
        self.window_flag = FALSE

        #use *args for multiple variables so they are in a tuple form

        option = { 0 : self.playwin_open,
                   1 : self.w_tonetune_open,
                   2 : self.w_set_open,
                   3 : self.w_exit}
        print(decision)
        option[decision]()

    def playwin_close(self, playwin):

        if self.window_flag is TRUE:
                self.root.deiconify()
                playwin.destroy()
                self.window_flag = FALSE
        else:
            pass

    def w_tonetune_close(self, w_tonetune):

        if self.window_flag is TRUE:
                self.root.deiconify()
                w_tonetune.destroy()
                self.window_flag = FALSE
        else:
            pass

    def w_set_close(self, w_set):
        print('test')
        if self.window_flag is TRUE:
                self.root.deiconify()
                w_set.destroy()
                self.window_flag = FALSE
        else:
            pass

    def w_exit(self):
    
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()  

    def playwin_open(self):
        self.root.withdraw()
        
        #playwin window creation
        playwin = Toplevel(self.root)
        playwin.title("ALDA: Learning a New Song")
        playwin.resizable(width=False,height=False)
        playwin.geometry('750x600') #rough estimated resolution 

        #Content Frame
        content = ttk.Frame(playwin, padding="2 2 2 2")
        content.grid(row=0,column=0)
        content.rowconfigure(0, weight=1)
        content.columnconfigure(0,weight=1)

        self.window_flag = TRUE
        playwin.protocol("WM_DELETE_WINDOW", lambda: self.playwin_close(playwin))
    
    def w_tonetune_open(self):
        self.root.withdraw()

        w_tonetune = Toplevel(self.root)
        w_tonetune.title("ALDA: Tuning my Guitar")
        w_tonetune.resizable(width=False,height=False)
        w_tonetune.geometry('750x600')
        
        self.window_flag = TRUE
        w_tonetune.protocol("WM_DELETE_WINDOW", lambda: self.w_tonetune_close(w_tonetune))


    def w_set_open(self):
  
        self.root.withdraw()

        w_set = Toplevel(self.root)
        w_set.title("ALDA: Setting")
        w_set.resizable(width=False,height=False)
        w_set.geometry('750x600')

        self.window_flag = TRUE
        w_set.protocol("WM_DELETE_WINDOW", lambda: self.w_set_close(w_set))