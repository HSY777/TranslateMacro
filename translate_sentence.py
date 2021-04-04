import pandas as pd
from selenium import webdriver
import time
import threading, queue
from tkinter import *

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
    t = threading.Thread(target = startTL)
    t.start()
    label1.config(text = '번역중')

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