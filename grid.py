from tkinter import *

root = Tk()
root.title('asdf')
root.geometry('640x480')

b1 = Button(root, text = '(0, 0)')
b2 = Button(root, text = '(0, 1)', width = 20)
b3 = Button(root, text = '(0, 2)')

b4 = Button(root, text = '(1, 0)')
b5 = Button(root, text = '(1, 1)')
b6 = Button(root, text = '(1, 3)')

b7 = Button(root, text = '(2, 1)')
b8 = Button(root, text = '(2, 2)')
b9 = Button(root, text = '(2, 4)')

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0, rowspan = 2)
b5.grid(row = 1, column = 1, columnspan = 3)
b6.grid(row = 1, column = 3)

b7.grid(row = 2, column = 1, sticky = 'w')
b8.grid(row = 2, column = 2)
b9.grid(row = 2, column = 99)

root.mainloop()
