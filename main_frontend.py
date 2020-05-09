import tkinter as tk
from tkinter import Label, Button, StringVar


class App1:

    def __init__(self, top):
        self.top = top
        top.title("Syllabification app")
        top.geometry("1028x500")
        top.configure(background="#ffcce6")  # background color

        # fonts
        font01 = "{Al-Aramco} 25 italic"
        font02 = "{Courier New} 12 bold"
        font03 = "{Segoe UI} 13 bold"
        font04 = "{Segoe UI} 15 bold"

        self.Label1 = tk.Label(master=top, text="Syllabification App", background="#ffcce6",
                               font=font01, foreground="#5c5c8a")
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=507)

        self.entry1 = tk.Entry(master=top, background="#f2f2f2", foreground="#800040",
                               selectbackground="#ff3399", font=font02)
        self.entry1.place(relx=0.046, rely=0.25, height=36, relwidth=0.350)

        # ___Entry Control Buttons___
        self.Button1 = tk.Button(master=top, text='UNDO', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.405, rely=0.25, height=36, width=70)
        self.Button1 = tk.Button(master=top, text='CLEAR', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.480, rely=0.25, height=36, width=70)
        self.Button1 = tk.Button(master=top, text='DONE', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.555, rely=0.25, height=36, width=125)

        # ___Main Control Buttons___
        self.Button1 = tk.Button(master=top, text='HELP', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.8, rely=0.25, height=36, width=150)
        self.Button1 = tk.Button(master=top, text='MOP', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.8, rely=0.35, height=36, width=150)
        self.Button1 = tk.Button(master=top, text='SSG', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.8, rely=0.45, height=36, width=150)
        self.Button1 = tk.Button(master=top, text='AUTHORS', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9",)
        self.Button1.place(relx=0.8, rely=0.55, height=36, width=150)
        self.Button1 = tk.Button(master=top, text='EXIT', background='#ffe6f2',
                                 font=font03, foreground="#5c5c8a", activebackground="#ffe6f9", 
                                 command=close_window)
        self.Button1.place(relx=0.8, rely=0.65, height=36, width=150)


        # ___IPA Buttons___
        # 1st row
        self.Button2 = tk.Button(master=top, text='''i''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.05, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɪ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.12, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''e''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.19, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''æ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.26, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ə''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.33, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʌ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.4, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɚ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.47, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''u''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.54, rely=0.42, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɔ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.61, rely=0.42, height=44, width=67)
        # 2nd row
        self.Button2 = tk.Button(master=top, text='''ʊ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.05, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɑ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.12, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''p''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.19, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''b''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.26, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''t''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.33, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''d''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.4, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''k''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.47, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''g''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.54, rely=0.55, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʔ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.61, rely=0.55, height=44, width=67)
        # 3rd row
        self.Button2 = tk.Button(master=top, text='''ʧ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.05, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʤ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.12, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''f''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.19, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''v''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.26, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''θ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.33, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ð''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.4, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''s''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.47, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''z''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.54, rely=0.68, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ʃ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.61, rely=0.68, height=44, width=67)
        # 4th row
        self.Button2 = tk.Button(master=top, text='''ʒ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.05, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''m''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.12, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''n''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.19, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ŋ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.26, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''r''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.33, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''l''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.4, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''ɾ''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.47, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''w''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.54, rely=0.81, height=44, width=67)
        self.Button2 = tk.Button(master=top, text='''j''', background="#ffe6f2", font=font04,
                                 foreground="#5c5c8a", activebackground="#ff3399", borderwidth='1')
        self.Button2.place(relx=0.61, rely=0.81, height=44, width=67)


def close_window():
    root.destroy()


root = tk.Tk()
my_gui = App1(root)
root.mainloop()
