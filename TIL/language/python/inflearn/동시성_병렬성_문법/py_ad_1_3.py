'''
Sction 1
Multithreading - Thread(1)-Basic
Keyword - Threading basic
'''
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3) # 3sec
    logging.info("Sub-Thread %s: finished", name)

# 메인 영역
if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))
    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    
    # 주석 전후 결과 확인
    # x.join()
    # 자식 스레드가 종료될때까지 메인스레드 대기
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: DONE")
    
'''
메인 스레드가 종료되어도 서브스레드는 자신이 할일은 한뒤에 종료가 된다.
(스레드는 한번 시작되면 완료되기 전까지 계속 진행된다.)
'''