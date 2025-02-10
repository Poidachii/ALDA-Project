from tkinter import *
from tkinter import ttk

#root.geometry('350x200')

#formula block
def calculate(*args):
    try: 
        value = float(menu_name.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)

    except ValueError:
        pass
#Main application Window    
root = Tk()
root.title("ALDA: Assistive Learning Device Attachment for Guitars")

#Content Frame
content = ttk.Frame(root, padding="3 3 12 12")
frame = ttk.Frame(content, borderwidth=5, relief="ridge",width=200,height=100)
content.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Entry Widget
menu_name = StringVar()
menu_entry = ttk.Entry(content, width=7, textvariable=menu_name)
menu_entry.grid(column=2, row=1, sticky=(W, E))

#Other Widgets remaining
meters = StringVar()
ttk.Label(content, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(content, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(content, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(content, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(content, text="meters").grid(column=3, row=2, sticky=W)

#polishing for widget distancing
for child in content.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
menu_entry.focus()
root.bind("<Return>", calculate)

#event loop 
root.mainloop()