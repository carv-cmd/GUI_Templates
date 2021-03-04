from tkinter import *
from tkinter import ttk
import re

# try:
#     from lin_reg_vectorized import *
# except FileNotFoundError:
#     pass

###############################################
###############################################
root = Tk()
root.title('SingleVariable')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(300, 150)


################################################################
################################################################
def get_hypothesis(*args):
    try:
        hype = y = m * x + b
        hypothesis.set('asshole')
    except NameError or ValueError:
        hypothesis.set('*Some hypothesis')


###############################################
###############################################
def valid_entry(*args):
    x = user_entry.getdouble(user_input)
    if x:
        user_button.config(state='normal')
    else:
        user_button.config(state='disabled')


def check_entry(user_entry):
    return re.match('^[0-9]*$', user_entry) is not None and len(user_entry) <= 6


check_wrapper = (root.register(check_entry), '%P')


def prediction(*args):
    try:
        lin_reg = m * user_input.get() + b
        result.set(f'Given:(x={user_input.get()}) ~~ Resulting:(y={lin_reg}')
    except NameError or ValueError:
        result.set(user_input.get() ** 2)


single_root = ttk.Frame(root, padding='4 8 4 6')

directions = ttk.Label(single_root, width=25, text="Enter an X to predict it's Y:")

hypothesis = StringVar(root)
hype_msg = ttk.Label(single_root, width=15, text='Hypothesis:')
current_hypo = ttk.Label(single_root, width=10, textvariable=hypothesis)
sep1 = ttk.Separator(single_root, orient=HORIZONTAL)

user_input = DoubleVar(root)
user_input.set('')
user_entry = ttk.Entry(single_root, width=16, textvariable=user_input, validate='key', validatecommand=check_wrapper)
user_button = ttk.Button(single_root, text='Calculate!', command=prediction)
sep2 = ttk.Separator(single_root, orient=HORIZONTAL)

result = StringVar(root)
res_info = ttk.Label(single_root, width=20, text="Resulting Y:")
result_out = ttk.Label(single_root, width=20, textvariable=result)

###############################################
###############################################
single_root.grid(column=0, row=0, padx=6, pady=2, ipadx=4, ipady=1, sticky=(W, E))
# single_root.grid_anchor('center')

hype_msg.grid(column=0, row=0, sticky=W)
current_hypo.grid(column=3, row=0, ipadx=5, ipady=7, sticky=W)
sep1.grid(column=0, row=1, columnspan=4, pady=8, sticky=(N, S, E, W))

directions.grid(column=0, row=2, sticky=W)
user_entry.grid(column=3, row=2, padx=2, pady=2, ipadx=5, ipady=2)
user_button.grid(column=0, row=3, columnspan=2, padx=1, pady=4, ipadx=2, ipady=1)
sep2.grid(column=0, row=4, columnspan=4, pady=8, sticky=(N, S, E, W))

res_info.grid(column=0, row=5, pady=4, sticky=W)
result_out.grid(column=3, row=5, sticky=W)

###############################################
single_root.rowconfigure(0, weight=1)
single_root.columnconfigure(0, weight=1)
single_root.columnconfigure(1, weight=1)

hype_msg.rowconfigure(1, weight=1)
hype_msg.columnconfigure(0, weight=1)
current_hypo.rowconfigure(1, weight=1)
current_hypo.columnconfigure(1, weight=1)
sep1.rowconfigure(1, weight=1)
sep1.columnconfigure(0, weight=1)

directions.rowconfigure(2, weight=1)
directions.columnconfigure(0, weight=1)
user_entry.rowconfigure(2, weight=1)
user_entry.columnconfigure(1, weight=1)
user_button.rowconfigure(3, weight=2)
user_button.columnconfigure(1, weight=1)
sep1.rowconfigure(4, weight=1)
sep1.columnconfigure(0, weight=1)

res_info.rowconfigure(4, weight=1)
res_info.columnconfigure(0, weight=1)
result_out.rowconfigure(4, weight=1)
result_out.columnconfigure(0, weight=1)

###############################################
###############################################
user_entry.focus()

user_input.trace('w', valid_entry)

# root.bind("<Return>", prediction)

################################################################
################################################################
if __name__ == '__main__':
    root.mainloop()

