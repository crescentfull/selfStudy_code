# thread 쓸때 유용한 Futures 패키지 
'''
Sction 1
Multithreading - Thread(3) - ThreadPoolExecutor
Keyword - Many Threads, concurrent.futures, (xxx)PoolExecutor
'''
'''

그룹스레드
    (1) python 3.2 이상 표준 라이브러리 사용
    (2) concurrent.futures
    (3) with 사용으로 생성, 소멸 라이프사이클 관리 용이
    (4) 디버깅하기가 난해함(단점)
    (5) 대기중인 작업 -> Queue -> 완료 상태조사 -> 결과 또는 예외 -> 단일화(캡슐화)    
'''

import logging
import time
from concurrent.futures import ThreadPoolExecutor

# 영역 3개
def task(name):
    logging.info(f'Sub-Thread {name}: starting')
    
    res = 0
    for i in range(10001):
        res = res + i
    
    logging.info(f'Sub-Thread {name}: finising result: {res}')
    
    return res
def main():
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    logging.info('Main-Thread: before creating and running thread')

    # # 실행 방법 1
    # # max_worker: 작업의 갯수가 넘어가면 직접 설정이 유리
    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ('First',))
    # task2 = excutor.submit(task, ('Second',))
    # task3 = excutor.submit(task, ('Third',))

    # # 결과값 반환
    # print(task1.result())
    # print(task2.result())
    # print(task3.result())
    
    # 실행 방법 2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task,['First', 'Second'])
        
        # 결과 확인
        print(list(tasks))
    
if __name__ == '__main__':
    main()


# concurrent.future 패키지 => 스레딩 사용할수 있도록 만들어 둔 패키지