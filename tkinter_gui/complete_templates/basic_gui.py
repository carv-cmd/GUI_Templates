# CodeCopy and notes paraphrasing from https://tkdocs.com/tutorial/firstexample.html
#####################################################
#####################################################
# tkinter * imports to core library and eliminates the requirement to prefix the module name
# tkinter ttk submodule implements python bindings for 'themed widgets'
from tkinter import *
from tkinter import ttk


def calc(*args):
    """
    Notice how later we set the entry widget 'textvariable' to feet
    This means anytime the entry changes, Tk automatically updates the value of feet
    Similarly if we explicitly change the value of a textvariable associated with a widget
    (as were doing for meters) the widget will automatically update with the contents of the variable
    """
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Foot Fetish to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calc).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Feet").grid(column=3, row=1, stick=W)
ttk.Label(mainframe, text="Is Equivalent To").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()

root.bind("<Return>", calc)

root.mainloop()
