from tkinter import *
from tkinter import ttk
import main
class child_window():

    def __init__(self, root, *args):
        self.root = root
        decision = int(*args)
        option = { 0 : self.playwin_open,
                   1 : self.w_tonetune_open}
        option[decision]()

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

            playwin.protocol("WM_DELETE_WINDOW", self.playwin_close)

    def playwin_close(self):
            self.root.deiconify()
            self.playwin.destroy()

    def w_tonetune_open(self):
           
           self.root.withdraw()

           w_tonetune = Toplevel(self.root)
           w_tonetune.title("ALDA: Tuning my Guitar")
           w_tonetune.resizable(width=False,height=False)
           w_tonetune.geometry('750x600')