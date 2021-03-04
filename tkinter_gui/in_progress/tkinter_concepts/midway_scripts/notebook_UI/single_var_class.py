# from tkinter import *
# from tkinter import ttk
from ui_main import *


class SingleVar:

    def __init__(self, single):
        single_root = single
        single_root.minsize(300, 150)
        single_root.rowconfigure(0, weight=1)
        single_root.columnconfigure(0, weight=1)

        application = ttk.Frame(single_root, padding='6 8 8 6')
        application.grid(column=0, row=0, sticky=(N, S, E, W))
        application.rowconfigure(0, weight=1)
        application.columnconfigure(0, weight=1)

        directions = ttk.Label(single_root, width=25, text="Enter an X to predict it's Y:")
        directions.grid

