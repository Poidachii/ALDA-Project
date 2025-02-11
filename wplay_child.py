from tkinter import *
from tkinter import ttk
import main

class child_window():

    def __init__(self, root, *args):
        self.root = root
        decision = int(*args)

        option = { 0 : self.playwin_open,
                   1 : self.w_tonetune_open,
                   2 : self.w_set_open,
                   3 : self.w_exit}
        
        option[decision]()

    def playwin_close(self):
            self.playwin = self.playwin_open()

            self.root.deiconify()
            self.playwin.destroy()

    def w_tonetune_close(self):
            self.w_tonetune = self.w_tonetune_open

            self.root.deiconify()
            self.w_tonetune.destroy()
    
    def w_set_close(self):
          self.w_set = self.w_set_open

          self.root.deiconify()
          self.w_set.destroy()
          
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

            playwin.protocol("WM_DELETE_WINDOW", lambda: self.playwin_close())

            return playwin
    
    def w_tonetune_open(self):
           self.root.withdraw()

           w_tonetune = Toplevel(self.root)
           w_tonetune.title("ALDA: Tuning my Guitar")
           w_tonetune.resizable(width=False,height=False)
           w_tonetune.geometry('750x600')

           return w_tonetune

    def w_set_open(self):
          self.root.withdraw()

          w_set = Toplevel(self.root)
          w_set.title("ALDA: Setting")
          w_set.resizable(width=False,height=False)
          w_set.geometry('750x600')
