import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import threading, queue
from tkinter import *

class TLprocessor:
    def __init__(self):

    def readSentenceFromExcel(self):
        data = pd.read_excel('./input_sentence.xlsx')
        startWord = data.startSentence.values  # <class 'numpy.ndarray'>
        combine_data = ''
        for i in range(len(startWord)):
            combine_data = combine_data + startWord[i]
            combine_data = combine_data + '%0A'

        return startWord, combine_data

    def getResultFromGooleTL(self, add_url):
        css_sel = '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb.BLojaf > div.dePhmb > div > div.J0lOec'
        url = 'https://translate.google.co.kr/?hl=ko&sl=ko&tl=en&text=' + add_url + '&op=translate'

        driver = webdriver.Chrome('./chromedriver')
        driver.minimize_window()
        driver.get(url)  
        driver.implicitly_wait(10)
        rating = driver.find_element_by_css_selector(css_sel)
        time.sleep(3)

        arriveWord = rating.text
        list_arriveWord = []
        sumWord = ''
        for i in arriveWord:
            sumWord += i
            if i == '\n':
                list_arriveWord.append(sumWord)
                sumWord = ''

        #driver.quit()
        return list_arriveWord

    def writeSentenceOnExecl(self, startWord, list_arriveWord):
        df = pd.DataFrame({'startSentence': startWord, 'arriveSentence': list_arriveWord})
        df.to_excel('input_sentence.xlsx', sheet_name='new_name', index=False, header=True)
        label1.config(text = '완료')

class StartTL(thraeding.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        df = pd.DataFrame({'startSentence': startWord, 'arriveSentence': list_arriveWord})
        df.to_excel('input_sentence.xlsx', sheet_name='new_name', index=False, header=True)
        label1.config(text = '완료')

class Myapp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.label1 = Label(self, text = '대기중')
        self.label1.pack()
        self.btn1 = Button(self, text = '번역시작', command = btncmd)

    def btncmd(self):
        StartTL.start()
        self.label1.config(text = '번역중')

if __name__ == '__main__':
    root = Myapp()
    root.mainloop()

startWord, combine_data = readSentenceFromExcel()
    list_arriveWord = getResultFromGooleTL(combine_data)
    writeSentenceOnExecl(startWord, list_arriveWord)














def startTL():
    startWord, combine_data = readSentenceFromExcel()
    list_arriveWord = getResultFromGooleTL(combine_data)
    writeSentenceOnExecl(startWord, list_arriveWord)

def readSentenceFromExcel():
    data = pd.read_excel('./input_sentence.xlsx')
    startWord = data.startSentence.values  # <class 'numpy.ndarray'>
    combine_data = ''

    for i in range(len(startWord)):
        combine_data = combine_data + startWord[i]
        combine_data = combine_data + '%0A'
    return startWord, combine_data

def getResultFromGooleTL(add_url):
    css_sel = '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.P6w8m.BDJ8fb.BLojaf > div.dePhmb > div > div.J0lOec'
    url = 'https://translate.google.co.kr/?hl=ko&sl=ko&tl=en&text=' + add_url + '&op=translate'

    driver = webdriver.Chrome('./chromedriver')
    driver.minimize_window()
    driver.get(url)  
    driver.implicitly_wait(10)
    rating = driver.find_element_by_css_selector(css_sel)
    time.sleep(3)

    arriveWord = rating.text
    list_arriveWord = []
    sumWord = ''
    for i in arriveWord:
        sumWord += i
        if i == '\n':
            list_arriveWord.append(sumWord)
            sumWord = ''

    #driver.quit()
    return list_arriveWord

def writeSentenceOnExecl(startWord, list_arriveWord):
    df = pd.DataFrame({'startSentence': startWord, 'arriveSentence': list_arriveWord})
    df.to_excel('input_sentence.xlsx', sheet_name='new_name', index=False, header=True)
    label1.config(text = '완료')

def btncmd():
    label1.config(text = '번역중')
    startTL()
    

def main():    
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title('Translate Macro')
    root.geometry('640x480')
    label1 = Label(root, text = '대기중')
    label1.pack()
    btn1 = Button(root, text = '번역시작', command = btncmd)
    btn1.pack()

    main()