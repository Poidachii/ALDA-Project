from tkinter import ttk
from tkinter import *

class testing:
    def __init__(self, root):
        self.root = root
        self.create_main_window()

    def create_main_window(self):
        self.main_window = ttk.Frame(self.root)
        self.main_window.pack()

        button_to_new_window = ttk.Button(self.main_window, text="Go to New Window", command=self.show_new_window)
        button_to_new_window.pack()

    def create_new_window(self):
        self.new_window = ttk.Frame(self.root)
        self.new_window.pack()

        button_to_main_window = ttk.Button(self.new_window, text="Go to Main Window", command=self.show_main_window)
        button_to_main_window.pack()

    def show_new_window(self):
        self.main_window.pack_forget()
        self.create_new_window()

    def show_main_window(self):
        self.new_window.pack_forget()
        self.create_main_window()

root = Tk()
app = testing(root)

root.mainloop()