from tkinter import *
from tkinter import ttk


class FeetToMeters:
    def __init__(self, root):

        root.title('Length Converter')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # self.feet_in = StringVar()
        # feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet_in)
        # feet_entry = ttk.grid
