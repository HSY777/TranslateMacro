import pandas as pd
from selenium import webdriver
from tkinter import *
import tkinter.ttk as ttk
import threading, queue, time

'''
def btncmd():
    for i in range(1, 101):
        time.sleep(0.01)

        p_var.set(i)
        progressbar.update()
        print(p_var.get())
'''        

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

    driver.quit()
    return list_arriveWord

def writeSentenceOnExecl(startWord, list_arriveWord):
    df = pd.DataFrame({'startSentence': startWord, 'arriveSentence': list_arriveWord})
    df.to_excel('input_sentence.xlsx', sheet_name='new_name', index=False, header=True)
    progress_label.config(text = '완료')

def maching_TLcode():
    selCount = 0

    for i in sel_resultLang:
        if i == 1:
            set_resultLnag.append(arrLangCode[selCount])
        selCount += 1
    
    print(sel_resultLang)
    print(set_resultLnag)

def set_option():
    appendLnag()
    maching_TLcode()
    startLangCode = startLang_var.get()
    print(startLangCode)

def btncmd():
    set_option()
    #t = threading.Thread(target = startTL)
    #t.start()
    #progress_label.config(text = '번역중')

def appendLnag():
    sel_resultLang.append(arrLang_var_reTL.get())
    sel_resultLang.append(arrLang_var_Eng.get())
    sel_resultLang.append(arrLang_var_Ch.get())
    sel_resultLang.append(arrLang_var_Jp.get())
    sel_resultLang.append(arrLang_var_Spain.get())
    sel_resultLang.append(arrLang_var_France.get())
    sel_resultLang.append(arrLang_var_Germany.get())
    sel_resultLang.append(arrLang_var_Vietnam.get())
    sel_resultLang.append(arrLang_var_Indonesia.get())
    sel_resultLang.append(arrLang_var_Laos.get())
    sel_resultLang.append(arrLang_var_Thailand.get())
    sel_resultLang.append(arrLang_var_Russia.get())
    sel_resultLang.append(arrLang_var_Portugal.get())
    sel_resultLang.append(arrLang_var_Taiwan.get())
    sel_resultLang.append(arrLang_var_All.get())

def main():    
    # Set Location of UI argument
    frame_select_startLang.place(x = 30, y = 30)
    startLang_radioBtn_kor.grid(row = 0, column = 0, pady = 3)
    startLang_radioBtn_eng.grid(row = 1, column = 0)
    startLang_radioBtn_ch.grid(row = 2, column = 0)

    frame_select_arrLang.place(x = 160, y = 30)
    frame_sep_arrLang1.grid(row = 0, column = 0)
    frame_sep_arrLang2.grid(row = 0, column = 1)
    frame_sep_arrLang3.grid(row = 0, column = 2)

    arrLang_checkBtn_reTL.grid(row = 0, column = 0)
    arrLang_checkBtn_Eng.grid(row = 0, column = 0)
    arrLang_checkBtn_Ch.grid(row = 0, column = 0) 
    arrLang_checkBtn_Jp.grid(row = 1, column = 0) 
    arrLang_checkBtn_Spain.grid(row = 1, column = 0)
    arrLang_checkBtn_France.grid(row = 1, column = 0) 
    arrLang_checkBtn_Germany.grid(row = 2, column = 0)
    arrLang_checkBtn_Vietnam.grid(row = 2, column = 0)
    arrLang_checkBtn_Indonesia.grid(row = 2, column = 0) 
    arrLang_checkBtn_Laos.grid(row = 3, column = 0) 
    arrLang_checkBtn_Thailand.grid(row = 3, column = 0)
    arrLang_checkBtn_Russia.grid(row = 3, column = 0) 
    arrLang_checkBtn_Portugal.grid(row = 4, column = 0) 
    arrLang_checkBtn_Taiwan.grid(row = 4, column = 0) 
    arrLang_checkBtn_All.grid(row = 4, column = 0) 

    frame_progressbar.place(x = 115, y = 210)
    progress_label.grid(row = 0, column = 0)
    progressbar.grid(row = 1, column = 0)
    startTL_btn.grid(row = 2, column = 0, rowspan = 3)
    
if __name__ == '__main__':

    # Init Tkinter
    root = Tk()
    root.title('Translate Macro')
    root.geometry('500x340')
    
    # Init Value(global)
    sel_resultLang = []
    set_resultLnag = []
    startLangCode = ''
    arrLangCode = ['re', 'en', 'zh-CN', 'ja', 'es', 'fr', 'de', 'vi', 'id', 'lo', 'th', 'ru', 'pt', 'ch-TW', 'all']

    startLang_var = StringVar()
    arrLang_var_reTL = IntVar() 
    arrLang_var_Eng = IntVar() 
    arrLang_var_Ch = IntVar() 
    arrLang_var_Jp = IntVar() 
    arrLang_var_Spain = IntVar() 
    arrLang_var_France = IntVar() 
    arrLang_var_Germany = IntVar()
    arrLang_var_Vietnam = IntVar()
    arrLang_var_Indonesia = IntVar() 
    arrLang_var_Laos = IntVar() 
    arrLang_var_Thailand = IntVar() 
    arrLang_var_Russia = IntVar()
    arrLang_var_Portugal = IntVar()
    arrLang_var_Taiwan = IntVar()
    arrLang_var_All = IntVar() 
    p_var = IntVar()

    # Definition UI argument(global)
    frame_select_startLang = LabelFrame(root, text = 'Start Language')
    startLang_radioBtn_kor = Radiobutton(frame_select_startLang, text = 'Korean', value = 'kr', variable = startLang_var)
    startLang_radioBtn_eng = Radiobutton(frame_select_startLang, text = 'English', value = 'en', variable = startLang_var)
    startLang_radioBtn_ch = Radiobutton(frame_select_startLang, text = 'Chineses', value = 'zh-CN', variable = startLang_var)
    
    frame_select_arrLang = LabelFrame(root, text = 'Result Language') # borderwidth = 상수: 라벨 프레임 두께
    frame_sep_arrLang1 = LabelFrame(frame_select_arrLang, text = '', borderwidth = 0)
    frame_sep_arrLang2 = LabelFrame(frame_select_arrLang, text = '', borderwidth = 0)
    frame_sep_arrLang3 = LabelFrame(frame_select_arrLang, text = '', borderwidth = 0)
   
    arrLang_checkBtn_reTL = Checkbutton(frame_sep_arrLang1, text = 'Re-Translate  ', variable = arrLang_var_reTL)
    arrLang_checkBtn_Eng = Checkbutton(frame_sep_arrLang2, text = 'English     ', variable = arrLang_var_Eng)
    arrLang_checkBtn_Ch = Checkbutton(frame_sep_arrLang3, text = 'Chinese      ', variable = arrLang_var_Ch)
    arrLang_checkBtn_Jp = Checkbutton(frame_sep_arrLang1, text = 'Japanese      ', variable = arrLang_var_Jp)
    arrLang_checkBtn_Spain = Checkbutton(frame_sep_arrLang2, text = 'Spain       ', variable = arrLang_var_Spain)
    arrLang_checkBtn_France = Checkbutton(frame_sep_arrLang3, text = 'France        ', variable = arrLang_var_France)
    arrLang_checkBtn_Germany = Checkbutton(frame_sep_arrLang1, text = 'Germany      ', variable = arrLang_var_Germany)
    arrLang_checkBtn_Vietnam = Checkbutton(frame_sep_arrLang2, text = 'Vietnam    ', variable = arrLang_var_Vietnam)
    arrLang_checkBtn_Indonesia = Checkbutton(frame_sep_arrLang3, text = 'Indonesia    ', variable = arrLang_var_Indonesia)
    arrLang_checkBtn_Laos = Checkbutton(frame_sep_arrLang1, text = 'Laos            ', variable = arrLang_var_Laos)
    arrLang_checkBtn_Thailand = Checkbutton(frame_sep_arrLang2, text = 'Thailand    ', variable = arrLang_var_Thailand)
    arrLang_checkBtn_Russia = Checkbutton(frame_sep_arrLang3, text = 'Russia          ', variable = arrLang_var_Russia)
    arrLang_checkBtn_Portugal = Checkbutton(frame_sep_arrLang1, text = 'Portugal       ', variable = arrLang_var_Portugal)
    arrLang_checkBtn_Taiwan = Checkbutton(frame_sep_arrLang2, text = 'Taiwan       ', variable = arrLang_var_Taiwan)
    arrLang_checkBtn_All = Checkbutton(frame_sep_arrLang3, text = 'All Lnaguages', variable = arrLang_var_All)

    frame_progressbar = LabelFrame(root, text = '', borderwidth = 0)
    progressbar = ttk.Progressbar(frame_progressbar, maximum = 100, length = 250, variable = p_var)
    startTL_btn = Button(frame_progressbar, text = '번역시작', command = btncmd, width = 15)
    progress_label = Label(frame_progressbar, text = '대기중...')

    main()
    root.mainloop()