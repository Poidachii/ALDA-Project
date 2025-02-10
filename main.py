from tkinter import *
from tkinter import ttk
import wplay_child

#Main application Window    
class w_main:
    def __init__(self, root):

        self.root = root
        self.root.title("ALDA: Assistive Learning Device Attachment for Guitars")
        self.root.resizable(width=False,height=False)
        self.root.geometry('750x600') #rough estimated resolution 
        self.main()

    
    def main(self):

        #Style Themes
        s = ttk.Style()
        s.theme_use('clam')

        #Content (the whole window inside the parent one)
        content = ttk.Frame(self.root, padding="2 2 2 2")
        content.grid(row=0,column=0)
        content.pack(expand=True)
        content.rowconfigure(0, weight=1)
        content.columnconfigure(0,weight=1)

        #Frame (sub-window inside the content)
        mainframe = ttk.Frame(content, padding="2 2 2 2", width=200,height=400)
        #Entry Widgets(Where the user can type on or display results)

        #Labels
        ttk.Label(mainframe, text="ALDA-G").grid(column=2,row=1,sticky=N)

        #Buttons
        play_button = ttk.Button(mainframe, text="Play", command=lambda: self.createwin("0")).grid(column=2, row=3,sticky=S)
        tt_button = ttk.Button(mainframe, text="Tone Tuning").grid(column=2,row=4)
        set_button = ttk.Button(mainframe, text="Settings").grid(column=2,row=5)
        exit_button = ttk.Button(mainframe, text="Exit").grid(column=2,row=6)

        #polishing for widget distancing
        for child in content.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.root.bind("<Return>", self.createwin)

    def createwin(self, *args):

        try:
            return wplay_child.child_window(self.root, *args)
        
        except ValueError:
            pass


def menu_root():
    root = Tk()
    mainwin = w_main(root)
    root.mainloop()

#event loop 
if __name__ == "__main__":
    menu_root()