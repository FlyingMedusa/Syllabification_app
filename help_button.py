
import tkinter as tk
from tkinter import Label, StringVar, Scrollbar


def about_help():
    about = tk.Tk()
    about.title("Help me pls")
    about.configure(background="#ffcce6")


    S = tk.Scrollbar(about)
    T = tk.Text(about, height=10, width=35, 
                font="{Segoe UI} 19 bold", foreground="#5c5c8a", background="#ffcce6")
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """ This is the Syllabification App.
            To use it you have to type the word
            of your choice into the textbox and click 
            on the MOP button. If you want to check
            wether the previously put to the stage 1:
            MOP syllabification is well-formed or
            ill-formed in terms of sonority
            click on the SSG button. Use the keyboard
            provided. """ 
    

    
    T.insert(tk.END, quote)
    tk.mainloop()