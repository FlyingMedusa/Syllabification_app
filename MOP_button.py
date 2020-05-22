import tkinter as tk
from tkinter import Label, Button, StringVar


def about_MOP():
    # basic info about MOP
    about = tk.Tk()
    about.geometry("300x250+350+200")
    about.title("What's the MOP?")
    about.configure(background="#ffcce6")

    labelinfo = Label(about, text="MOP", foreground="#5c5c8a", font="Al-Aramco 19 bold", 
    background="#ffcce6")
    #labelinfo.grid(row=0, column=0)
    labelinfo.place(relx=0.4, rely=0.02)


