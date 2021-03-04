from tkinter import *
from tkinter import ttk


def set_fields(*args):
    try:
        number = num_var.get()
        field_val.set(number)
        print(f'\nnumber type = {type(number)}\n')
    except AttributeError:
        print(f'Fields error')
        pass


######################################################
######################################################
root = Tk()
root.title('User Input GUI')

mainframe = ttk.Labelframe(root, text="Hypothesis Calculator", padding='6 6 12 12')
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

######################################################
######################################################
sub1 = ttk.Labelframe(mainframe, text='', padding='6 6 12 12')
sub1.grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Label(sub1, text="Select Number of Input Variables:").grid(column=1, row=1, sticky=(N, W))

num_var = IntVar()
num_entry = ttk.Combobox(sub1, width=7, textvariable=num_var)
num_entry.grid(column=2, row=1)
num_entry['values'] = (1, 2, 3, 4)
num_entry.state(["readonly"])

num_entry.focus()
num_entry.bind('<<ComboboxSelected>>', set_fields)
num_entry.selection_clear()

######################################################
######################################################
sub2 = ttk.Frame(mainframe, padding='6 6 12 12')
sub2.grid(column=0, row=1, sticky=(N, W, E, S))
ttk.Label(sub2, text="Enter Values for Prediction Function:").grid(column=1, row=2, sticky=(W, E))
field_val = IntVar()

######################################################
######################################################
# sub3 = ttk.Frame(mainframe, padding='6 6 12 12')
# sub3.grid(column=0, row=3, sticky=(N, W, E, S))

######################################################
######################################################
root.mainloop()
