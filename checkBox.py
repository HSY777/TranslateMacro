from tkinter import *

root = Tk()
root.title("asdf")
root.geometry("640x480")


label1 = Label(root, text = '도착어')

chkvar = IntVar()
chkbox = Checkbutton(root, text = '', variable = chkvar)
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = '일주일 보지 않기', variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root,text='클릭', command = btncmd)
btn.pack()

root.mainloop()