# A simple GUI for cleaner user input into programs
# The basic widgets can be found at: https://tkdocs.com/tutorial/widgets.html

######################################################
######################################################
from tkinter import *
from tkinter import ttk


class UserInput:

    def __init__(self, root):

        root.title('User Input GUI')

        mainframe = ttk.Frame(root, padding='6 6 12 12')
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ######################################################
        ######################################################
        sub1 = ttk.Frame(mainframe, padding='6 6 12 12')
        sub1.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(sub1, text="Select Number of Input Variables:").grid(column=1, row=1, sticky=(N, W))

        ######################################################
        ######################################################
        sub2 = ttk.Frame(mainframe, padding='6 6 12 12')
        sub2.grid(column=0, row=1, sticky=(N, W, E, S))
        ttk.Label(sub2, text="Enter Values for Prediction Function:").grid(column=1, row=2, sticky=(W, E))

        self.user_in1 = IntVar()
        user_entry1 = ttk.Entry(sub2, width=7, textvariable=self.user_in1)
        user_entry1.grid(column=2, row=2, sticky=(W, E), padx=3)
        self.user1 = IntVar()

        self.user_in2 = IntVar()
        user_entry2 = ttk.Entry(sub2, width=7, textvariable=self.user_in2)
        user_entry2.grid(column=3, row=2, sticky=(W, E), padx=3)
        self.user2 = IntVar()

        self.user_in3 = IntVar()
        user_entry3 = ttk.Entry(sub2, width=7, textvariable=self.user_in3)
        user_entry3.grid(column=4, row=2, sticky=(W, E), padx=3)
        self.user3 = IntVar()

        self.user_in4 = IntVar()
        user_entry4 = ttk.Entry(sub2, width=7, textvariable=self.user_in4)
        user_entry4.grid(column=5, row=2, sticky=(W, E), padx=3)
        self.user4 = IntVar()

        ######################################################
        ######################################################
        sub3 = ttk.Frame(mainframe, padding='6 6 12 12')
        sub3.grid(column=0, row=3, sticky=(N, W, E, S))
        ttk.Label(sub3, text="Press to Calculate:").grid(column=1, row=3, sticky=(W, E))
        ttk.Button(sub3, text="Click Here!").grid(column=3, row=3)
        # root.bind("<Return>", self.prediction)

        ######################################################
        ######################################################
        sub4 = ttk.Frame(mainframe, padding='6 6 12 12')
        sub4.grid(column=0, row=4, sticky=(N, W, E, S))
        ttk.Label(sub4, text=f"Hypothesis Result: {'f_in_chat'}").grid(column=1, row=4, sticky=(W, E))

        def prediction(self, *args):
            try:
                pass
            except ValueError:
                pass


root = Tk()
UserInput(root)
root.mainloop()
