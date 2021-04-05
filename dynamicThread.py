from tkinter import *
import tkinter.ttk as ttk
import threading, queue, time

root = Tk()
root.title('threading test')
root.geometry('640x480')

txt = Text(root, height = 1, width = 10)
txt.pack()

def getText():
    result = txt.get('1.0', 'end')
    print(result)

btn = Button(root, text = '읽기', command = getText)
btn.pack()

root.mainloop()