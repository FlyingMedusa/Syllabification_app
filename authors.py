import tkinter as tk
from tkinter import Label, Button, StringVar, PhotoImage


def authors():
    about = tk.Toplevel()
    about.geometry("350x350")
    about.title("AUTHORS")
    about.configure(background="#ffcce6")

    labelinfo = Label(about, text="Authors", foreground="#5c5c8a", font="System 19 bold", 
    background="#ffcce6")
    labelinfo.place(relx=0.35, rely=0.02)

    image = tk.PhotoImage(file="Vi.PNG")
    l1 = tk.Label(about, image=image, borderwidth=2)
    l1.image = image
    l1.pack()
    l1.place(relx=0.04, rely=0.15)

    image = tk.PhotoImage(file="Ma.PNG")
    l2 = tk.Label(about, image=image, borderwidth=2)
    l2.image = image
    l2.pack()
    l2.place(relx=0.52, rely=0.15)

    Label1 = tk.Label(master=about, text="↑Click on ponies to go to our github accounts↑  ", background="#ffcce6",
                               font="System 11", foreground="#5c5c8a")
    Label1.place(relx=0.001, rely=0.67, height=20, width=350)