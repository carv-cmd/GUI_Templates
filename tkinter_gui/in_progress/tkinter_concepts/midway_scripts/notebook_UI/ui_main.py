from tkinter import *
from tkinter import ttk
from single_var_class import *


class HomeIndex:

    def __init__(self, root):
        root = root
        root.minsize(450, 300)
        root.grid(column=0, row=0, sticky=(N, S, E, W))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mf = ttk.Frame(root, padding='6 6 18 18')
        notebook = ttk.Notebook(mf, width=400, height=200, padding='6 6 18 18')

        single = ttk.Frame(notebook, borderwidth=3, relief='ridge', padding='6 6 12 12')
        multi = ttk.Frame(notebook, borderwidth=3, relief='ridge', padding='6 6 12 12')

        notebook.add(single, text="SingleVar")
        notebook.add(multi, text='Multivariate')




if __name__ == "__main__":
    root = Tk()
    main_api = HomeIndex(root)
    root.mainloop()

