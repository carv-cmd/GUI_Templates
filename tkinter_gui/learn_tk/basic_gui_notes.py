# CodeCopy and notes paraphrasing from https://tkdocs.com/tutorial/firstexample.html
#####################################################
#####################################################
# tkinter * imports to core library and eliminates the requirement to prefix the module name
# tkinter ttk submodule implements python bindings for 'themed widgets'
from tkinter import *
from tkinter import ttk


#################################
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


#################################
# Define the main application window, as well as titling it
root = Tk()
root.title("Foot Fetish to Meters")

#################################
# Creating a 'Content Frame' (parent_widget)
# i.e.- Create a frame widget, which will hold the contents of the user interface
# after creation, '.grid' places it directly inside main application window
# column/row_configure tell frame to expand and fill any space is window's resized
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#################################
# Creating an 'Entry Widget' where users can input the value for conversion (child_widget)
# Need to, 1). 'Create' the widget itself & 2). 'Place' it onscreen
# Need to also specify its parent: i.e.- the widget its nested within (here the 'content frame')
# In Python the parent is passed as the first parameter when instantiating a widget object
# We can optionally provide 'config_options' like the 'entry width' and 'textvariable'
# '.grid()' places the widget object relative to the other widgets (think CSS grid layout-ish)
# 'sticky' option defines how the widget should line up within the grid cell, using compass directions
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

#################################
# For all following widgets:
# First create, then place onscreen in the appropriate cell in the grid
#################################
# Create a widget to display the output from our calculation
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Widget button to press and execute the calculation
ttk.Button(mainframe, text="Calculate", command=calc).grid(column=3, row=3, sticky=W)

# 3 static text labels for application guidance
ttk.Label(mainframe, text="Feet").grid(column=3, row=1, stick=W)
ttk.Label(mainframe, text="Is Equivalent To").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Meters").grid(column=3, row=2, sticky=W)

#################################
# First part adds padding to each of the widgets within the content frame
# Could've added in .grid() but this is a nice shortcut
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Second part tells Tk to focus on the entry widget. Cursor automatically starts in entry field
feet_entry.focus()

# Third part tells Tk to bind the 'Enter" key to call the calculate routine
root.bind("<Return>", calc)

#################################
# Start the event loop. Light the fireworks
root.mainloop()
