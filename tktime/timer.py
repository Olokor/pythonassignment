from tkinter import *
# from playsound import playsound
import time

#create the window
window = Tk()
window.title("Timer")
window.geometry("400x600")
window.config(bg="#000")
window.resizable(False, False)

heading = Label(master=window, text="Timer", font="arial 30 bold", fg="#ea3548")
heading.pack(pady=10)
Label(master=window, font=("arial 7 bold"), text="Current time: ", bg="papaya whip").place(x=65, y=100)
def clock():
    clock_time = time.strftime("%H:%M:%S:%p:")
    current_time.config(text=clock_time)
    current_time.after(1000, clock)
current_time = Label (master=window, font=("Arial ", 7, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=135, y=100)
clock ()

#timer
hrs = StringVar()
Entry(master=window, textvariable=hrs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=30, y=150)
hrs.set("00")

mins = StringVar()
Entry(master=window, textvariable=mins, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=170, y=150)
mins.set("00")

secs = StringVar()
Entry(master=window, textvariable=secs, width=2, font="arial 50", bg="#000", fg="#fff", bd=0).place(x=300, y=150)
secs.set("00")

Label(master=window, text="hour", font="arial 8 ", bg="#000", fg="#fff").place(x=100, y=150)

Label(master=window, text="mins", font="arial 8 ", bg="#000", fg="#fff").place(x=250, y=150)

Label(master=window, text="secs", font="arial 8 ", bg="#000", fg="#fff").place(x=380, y=150)

button = Button(master=window, text='Start', bg='#ea3548', fg="#fff", width=20, font="arial 10 bold")
button.pack(padx=5, pady=40, side=BOTTOM)

Image1 = PhotoImage(file="brush.png")
button1 = Button(master=window, image=Image1, bg="#000", bd=0)
button1.place(x=7, y=300)

Image2 = PhotoImage(file="eggs.png")
button1 = Button(master=window, image=Image2, bg="#000", bd=0)
button1.place(x=137, y=300)

Image3 = PhotoImage(file="face.png")
button1 = Button(master=window, image=Image3, bg="#000", bd=0)
button1.place(x=276, y=300)





window.mainloop()