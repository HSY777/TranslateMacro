import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('asdf')
root.geometry('640x480')

def info():
    msgbox.showinfo('알림', '예매완료')

def retrycancel():
    response = msgbox.askretrycancel('재시도 / 취소', '일시적 오류 재시도?')
    if response == 1:
        print('재시도')
    elif response == 0:
        print('취소')

def yesno():
    response = msgbox.askyesno('예/ 아니오', '역방향인데 ㄱ?')
    if response == 1:
        print('예')
    elif response == 0:
        print('아녀')


def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = '예매 내역 저장 x 끔??')
    print('응답', response)
    if response == 1:
        print('예')
    elif response == 0:
        print('아녀')
    else:
        print('취소')

Button(root, command = info, text = '알림').pack()
Button(root, command = retrycancel, text = '재시도').pack()
Button(root, command = yesno, text = '예아녀').pack()
Button(root, command = yesnocancel, text = '예아녀취소').pack()

root.mainloop()