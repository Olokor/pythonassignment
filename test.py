import tkinter as tk
from tkinter import ttk

window = tk.Tk()

string_var = tk.StringVar()

label = ttk.Label(master=window, textvariable=string_var)
label.pack()
entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

window.mainloop()