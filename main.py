from tkinter import *
from tkinter import ttk
import wplay_child

#formula blocks
def createwin(*args):

    try:
        wplay_child.child_window(*args)

    except ValueError:
        pass

#Main application Window    

root = Tk()
root.title("ALDA: Assistive Learning Device Attachment for Guitars")
root.resizable(width=False,height=False)
root.geometry('750x600') #rough estimated resolution 

#Style Themes
s = ttk.Style()
s.theme_use('clam')

#Content (the whole window inside the parent one)
content = ttk.Frame(root, padding="2 2 2 2")
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
play_button = ttk.Button(mainframe, text="Play", command=lambda: createwin(*args)).grid(column=2, row=3,sticky=S)
tt_button = ttk.Button(mainframe, text="Tone Tuning").grid(column=2,row=4)
set_button = ttk.Button(mainframe, text="Settings").grid(column=2,row=5)
exit_button = ttk.Button(mainframe, text="Exit").grid(column=2,row=6)

#polishing for widget distancing
for child in content.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", createwin)

#event loop 
root.mainloop()