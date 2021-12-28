import tkinter
from tkinter import *

root = Tk()
root.title("Eng-Kor Bible")
root.geometry("1250x750")
root.resizable(False,False)

btn_search = Button(root, padx=15, pady=10, text='Search')
btn_search.pack()

root.mainloop()