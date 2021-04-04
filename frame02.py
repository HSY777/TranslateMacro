from tkinter import *

root = Tk()
root.title('asdf')
root.geometry('640x480')

b1 = Button(root, text = 'top')
b1_1 = Button(root, text = 'top - 1')

b2 = Button(root, text = 'bottom')
b2_1 = Button(root, text = 'bottom - 1')

b3 = Button(root, text = 'left')
b3_1 = Button(root, text = 'left - 1')

b4 = Button(root, text = 'right')
b4_1 = Button(root, text = 'right - 1')

b5 = Button(root, text = 'center', bg = 'red')

b1.pack(side = 'top')
b1_1.pack(side = 'top', fill = 'x') # fill : 할당된 공간에 대한 크기 맞춤 (none: 안맞춤, x,y :x축 또는 y축 맞춤, both: xy축 모두 맞춤)

b2.pack(side = 'bottom')
b2_1.pack(side = 'bottom', anchor = 'nw') # anchor: 할당된 공간 내에서 위치 지정: center, n, e, s, w, ne, nw, se, sw

b3.pack(side = 'left')
b3_1.pack(side = 'left', fill = 'y')

b4.pack(side = 'right')
b4_1.pack(side = 'right', anchor = 's')

b5.pack(expand = True, fill = 'both') # expand: 미사용공간 확보

root.mainloop()