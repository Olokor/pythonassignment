import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("time convert")
window.geometry('350x150')

# create a title label
title_label  = ttk.Label(master=window, text="hours to sceonds ", font='calibri 24 bold')
title_label.pack()
def convert():
    hours = entry.get()
    seconds = int(hours) * 3600
    output_int.set(seconds)


# create a frame widget
input_frame = ttk.Frame(master=window)
# create entry field
# input_int = tk.IntVar()
entry = ttk.Entry(master=input_frame)
# create a button widget
button = ttk.Button(master=input_frame, text="convert", command=convert)
entry.pack(side='left')
button.pack(side='left', padx='5')
input_frame.pack()

# output
output_int = tk.IntVar()
output = ttk.Label(master=window, textvariable=output_int)
output.pack()

tk.mainloop()