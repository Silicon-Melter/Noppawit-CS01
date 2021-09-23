from tkinter import *

root = Tk()
root.title("First GUI")
ft = Label(text="MyName is",fg="blue",font=20).grid(row=0,column=0)
st = Label(text="Noppawit",fg="green",font=20).grid(row=1,column=1)
tt = Label(text="Chunram",fg="red",font=20).grid(row=2,column=2)
root.geometry("300x300")
root.mainloop()
