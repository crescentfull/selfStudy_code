'''
Sction 1
Multithreading - Thread(5) - Prod VS Cons Using Queue
Keyword - 생산자 소비자 패턴(Producer/Consumer Pattern)
'''
'''
Producer-Consumer Pattern
    (1) 멀티스레드 디자인 패턴의 정석
    (2) 서버측 프로그래밍 핵심
    (3) 주로 허리역할 중요
    
    Python Event 객체
    (1) flag 초기값(0)
    (2) set() -> 1, clear() ->0, wait() 1->리턴/0->대기, isSet()-> 현재 flag 상태
'''
import concurrent.futures
import logging
import queue, random, threading, time

# 생산자
def producer(queue, event):
    '''
    네트워크 대기 상태라 가정(서버)
    '''
    while not event.is_set():
        msg = random.randint(1,11)
        logging.info(f'Producer got message: {msg}')
        queue.put(msg)
    
    logging.info('Producer received event EXIT')
# 소비자
def consumer(queue, event):
    '''
    응답 받고 소비하는 것으로 가정 or DB 저장
    '''
    while not event.is_set() or not queue.empty():
        msg = queue.get()
        logging.info(f'Consumer storing message: {msg} (size={queue.qsize()})')
        
    logging.info('Consumer received event Exiting')


if __name__ == '__main__':
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 사이즈가 중요하다
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 플래그 초기 값 0
    event = threading.Event()
    
    # with context 
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event) #실행함수, 파라미터 1, 파라미터2
        executor.submit(consumer, pipeline, event) #실행함수, 파라미터 1, 파라미터2
    
        # 실행 시간 조정
        time.sleep(2)
    
        logging.info("Main : about to SET EVENT")
    
        # 프로그램 종료
        event.set()