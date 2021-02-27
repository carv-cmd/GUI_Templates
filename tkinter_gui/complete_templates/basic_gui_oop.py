# Adaptation of TkDocs 'first_example_class'
# https://tkdocs.com/tutorial/firstexample.html
######################################################
######################################################
from tkinter import *
from tkinter import ttk


class FeetToMeters:

    def __init__(self, root):

        root.title('Length Converter')

        mainframe = ttk.Frame(root, padding="12 12 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ######################################################
        ######################################################
        self.feet_in = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet_in)
        feet_entry.grid(column=2, row=1, sticky=(W, E))
        self.meters_out = StringVar()

        ttk.Label(mainframe, textvariable=self.meters_out).grid(column=2, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate Meters!", command=self.meter_calc).grid(column=2, row=4, sticky=W)

        ttk.Label(mainframe, text="Feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Is Equivalent To").grid(column=2, row=2, sticky=E)
        ttk.Label(mainframe, text="Meters").grid(column=3, row=3, sticky=W)

        ######################################################
        ######################################################
        self.meters_in = StringVar()
        meters_entry = ttk.Entry(mainframe, width=7, textvariable=self.meters_in)
        meters_entry.grid(column=4, row=1, sticky=(W, E))
        self.feet_out = StringVar()

        ttk.Label(mainframe, textvariable=self.feet_out).grid(column=4, row=3, sticky=(W, E))
        ttk.Button(mainframe, text="Calculate Feet!", command=self.feet_calc).grid(column=4, row=4, sticky=W)

        ttk.Label(mainframe, text="Meters").grid(column=5, row=1, sticky=W)
        ttk.Label(mainframe, text="Is Equivalent To").grid(column=4, row=2, sticky=E)
        ttk.Label(mainframe, text="Feet").grid(column=5, row=3, sticky=W)

        ######################################################
        ######################################################
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind("<Return>", self.meter_calc)
        feet_entry.forget()

        meters_entry.focus()
        root.bind("<Return>", self.feet_calc)
        meters_entry.forget()

    ######################################################
    ######################################################
    def meter_calc(self, *args):
        """ 1' = 0.3048 meters """
        try:
            value = float(self.feet_in.get())
            self.meters_out.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass

    def feet_calc(self, *args):
        """ 1 meter = 3.28084' """
        try:
            value = float(self.meters_in.get())
            self.feet_out.set(int(3.28084 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


######################################################
######################################################
root = Tk()
FeetToMeters(root)
root.mainloop()
