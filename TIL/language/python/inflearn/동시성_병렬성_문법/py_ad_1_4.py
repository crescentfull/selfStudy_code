'''
Sction 1
Multithreading - Thread(2)-Daemon, Join
Keyword - DaemonThread. Join
'''
'''

DaemonThread(데몬스레드)
    (1) 백그라운드 실행
    (2) 메인스레드 종료시 즉시 종료(강제)
    (3) 주로 백그라운드 무한 대기 이벤트 발생을 실행하는 부분을 담당 -> JVM(가비지 컬렉션), 자동 저장 등
    (4) 일반 스레드는 작업 종료시 까지 실행
    
    
'''
import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    #time.sleep(3) # 3sec
    for i in d:
        print(i)
    logging.info("Sub-Thread %s: finished", name)

# 메인 영역
if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', range(5)), daemon=True)
    y = threading.Thread(target=thread_func, args=('Second', range(20)))
    z = threading.Thread(target=thread_func, args=('Third', range(10)), daemon=True)

    logging.info("Main-Thread: before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    z.start()
    
    # DaemonThread check
    print(x.isDaemon())
    print(y.isDaemon())
    print(z.isDaemon())
    
    # 주석 전후 결과 확인
    # x.join() # daemon을 쓰는데 join을 쓴다? 굉장히 효율적이지 못한 코드이다
    # y.join()
    # z.join()
    # 자식 스레드가 종료될때까지 메인스레드 대기
    
    logging.info("Main-Thread: wait for the thread to finish")
    
    logging.info("Main-Thread: DONE")
    
'''
메인 스레드가 종료되어도 서브스레드는 자신이 할일은 한뒤에 종료가 된다.
(스레드는 한번 시작되면 완료되기 전까지 계속 진행된다.)
'''