from tkinter import *

root = Tk()
root.title('asdf')
root.geometry("640x480")

Label(root, text = '출발어').pack()

startLang_var = StringVar()
btn_kor = Radiobutton(root, text = '한국어', value = 1, variable = startLang_var)
btn_eng = Radiobutton(root, text = '영어', value = 2, variable = startLang_var)
btn_ch = Radiobutton(root, text = '중국어', value =3, variable = startLang_var)
btn_jp = Radiobutton(root, text = '일본어', value = 4, variable = startLang_var)

btn_kor.pack()
btn_eng.pack()
btn_ch.pack()
btn_jp.pack()

def btncmd():
    print(startLang_var.get())

btn = Button(root, text = '선택', command = btncmd)
btn.pack()

root.mainloop()