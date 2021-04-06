from tkinter import *
import tkinter.ttk as ttk
import threading, queue, time
from selenium import webdriver

class Worker(threading.Thread):
    def __init__(self, name, arrLangCode):
        super().__init__()
        self.name = name
        self.arrLangCode = arrLangCode            # thread 이름 지정

    def run(self):
        css_sel = '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb.BLojaf > div.dePhmb > div > div.J0lOec'
        url = 'https://translate.google.co.kr/?hl=' + sel_startL + '&sl=ko&tl=' + self.arrLangCode + '&text=' + combine_startL_sentence + '&op=translate'

        driver = webdriver.Chrome('./chromedriver')
        #driver.minimize_window()
        driver.get(url)  
        driver.implicitly_wait(10)
        rating = driver.find_element_by_css_selector(css_sel)
        time.sleep(3)

        arriveWord = rating.text
        sumWord = ''
        sep_result_TL = []
        for i in arriveWord:
            sumWord += i
            if i == '\n':
                sep_result_TL.append(sumWord)
                sumWord = ''

        #driver.quit()
        append_result_TL.append(sep_result_TL)
        print(sep_result_TL)
        #print("sub thread start ", threading.currentThread().getName())
        #print(self.arrLangCode)
        #time.sleep(3)
        #print("sub thread end ", threading.currentThread().getName())

def readSentenceFromExcel():
    startWord = 'startWord11'
    #combine_startL_sentence = '유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A헤시태그내용~~~%0A멍청이%0A목아프다%0A'

def startTL():
    readSentenceFromExcel()
    for i in range(radioval.get()):
        name = "thread {}".format(i)
        t1 = Worker(name, arrLangCode[i])
        t1.start()

def btncmd():
    #sel_startL = txt1.get('1.0', 'end')
    print(sel_startL)
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
    combine_startL_sentence = '유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A유튜브제목%0A유튜브제목%0A신원길%20멍청한놈%0A헤시태그내용~~~%0A멍청이%0A목아프다%0A'
    append_result_TL = []

    # varialbe
    sel_startL = 'ko'
    arrL_count = 0
    radioval = IntVar()
    arrLangCode = ['pt', 'en', 'zh', 'ja', 'es']

    txt1 = Text(root, height = 1, width = 10)
    check1 = Radiobutton(root, text = '1', value = '1', variable = radioval)
    check2 = Radiobutton(root, text = '2', value = '2', variable = radioval)
    check3 = Radiobutton(root, text = '3', value = '3', variable = radioval)
    check4 = Radiobutton(root, text = '4', value = '4', variable = radioval)
    check5 = Radiobutton(root, text = '5', value = '5', variable = radioval)

    btn = Button(root, text = '시작', command = btncmd)

    main()
    root.mainloop()
















