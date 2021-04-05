from tkinter import *

def appendLnag():
    sel_resultLang.append(var1.get())
    sel_resultLang.append(var2.get())
    sel_resultLang.append(var3.get())

def btncmd():
    appendLnag()
    selCount = 0
    for i in sel_resultLang:
        if i == 1:
            set_resultLang.append(languageCode[selCount])
        selCount += 1
            
    print(sel_resultLang)
    print(set_resultLang)

root = Tk()
root.title('asdf')
root.geometry('640x480')

sel_resultLang = []
set_resultLang = []
languageCode = ['re', 'en', 'zh-CN', 'ja', 'es', 'fr', 'de', 'vi', 'id', 'lo', 'th', 'ru', 'all']

var1 = IntVar() 
var2 = IntVar() 
var3 = IntVar() 
check1 = Checkbutton(root, text = '1  ', variable = var1)
check2 = Checkbutton(root, text = '2  ', variable = var2)
check3 = Checkbutton(root, text = '3  ', variable = var3)
check1.pack()
check2.pack()
check3.pack()

btn = Button(root, text = '클릭', command = btncmd)
btn.pack()

#sel_resultLang.append()



root.mainloop()