from tkinter import *
import tkinter.ttk as ttk
import threading, queue, time

class Worker(threading.Thread):
    def __init__(self, name, arrLangCode):
        super().__init__()
        self.name = name
        self.arrLangCode = arrLangCode            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        print(self.arrLangCode)
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())

def readSentenceFromExcel():
    startWord = 'startWord11'
    combine_data = 'combine_data11'

def startTL():
    readSentenceFromExcel()
    for i in range(radioval.get()):
        name = "thread {}".format(i)
        t1 = Worker(name, arrLangCode[i])
        t1.start()

def btncmd():
    startL_count = txt1.get('1.0', 'end')
    print(startL_count)
    print(radioval.get())

    t = threading.Thread(target = startTL)
    t.start()
    
def main():
    txt1.pack()
    check1.pack()
    check2.pack()
    check3.pack()
    check4.pack()
    check5.pack()
    btn.pack()

if __name__ == '__main__':
    root = Tk()
    root.title('threading test')
    root.geometry('640x480')

    # TLV
    startWord = ''
    combine_data = ''

    # varialbe
    startL_count = ''
    arrL_count = 0
    radioval = IntVar()
    arrLangCode = ['re', 'en', 'zh', 'ja', 'es']

    txt1 = Text(root, height = 1, width = 10)
    check1 = Radiobutton(root, text = '1', value = '1', variable = radioval)
    check2 = Radiobutton(root, text = '2', value = '2', variable = radioval)
    check3 = Radiobutton(root, text = '3', value = '3', variable = radioval)
    check4 = Radiobutton(root, text = '4', value = '4', variable = radioval)
    check5 = Radiobutton(root, text = '5', value = '5', variable = radioval)

    btn = Button(root, text = '시작', command = btncmd)

    main()
    root.mainloop()
















