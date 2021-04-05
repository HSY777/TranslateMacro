import threading, requests, time
# https://wikidocs.net/82581 for문 쓰레드생성 

def readSentenceFromExcel():
    startWord = 'startWord11'
    combine_data = 'combine_data11'
    return startWord, combine_data

def getResultFromGooleTL_01():
    list_arriveWord.append('list_arriveWord01')

def getResultFromGooleTL_02():
    list_arriveWord.append('list_arriveWord02')

def startTL(startLnag):
    a, b = readSentenceFromExcel()
    t11 = threading.Thread(target = getResultFromGooleTL_01)
    t22 = threading.Thread(target = getResultFromGooleTL_02)
    t11.start()
    t22.start()
    print(a, b)

t1 = threading.Thread(target = startTL, args = ('en', ))
t1.start()

list_arriveWord = []
time.sleep(5)
print(list_arriveWord)

