import threading

from queue import Queue

def creator(data, q):
    print('creating data and putting it on the queue')
    print('\n')
    for item in data:
        evt = threading.Event()
        q.put((item, evt))
        print('watting for data to be doubled')
        evt.wait()

def consumer(q):
    while True:
        data, evt = q.get()
        print('receive original data: {}'.format(data))
        processed = data * 5
        print('receive processed data : {}'.format(processed))
        print('\n')
        evt.set()
        q.task_done()

if __name__ == '__main__':
    q = Queue()
    data = [7, 14, 39, 66, 77, 88, 99, 11, 22]
    thread_one = threading.Thread(target = creator, args = (data, q))
    thread_two = threading.Thread(target = consumer, args = (q,))
    thread_one.start()
    thread_two.start()

    q.join()
    
    # 작업 완료를 알리기 위해 큐에 시그널을 보낸다
    # q.task_done()
    # 모든 사항을 처리할 때까지 큐 완료를 기다린다.
    # q.join()