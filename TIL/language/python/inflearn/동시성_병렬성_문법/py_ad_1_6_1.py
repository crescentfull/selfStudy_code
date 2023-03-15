'''
Sction 1
Multithreading - Thread(4) - Lock, DeadLock
Keyword - Lock, DeadLock, Race Condition, Thread synchronization
'''
'''

용어 설명
    (1) 세마포어(Semaphore) : 프로세스간 공유된 자원에 접근 시, 어떤 문제 발생가능성이 있기 때문에 
        -> 한개의 프로세스만 접근 할수 있도록 접근 처리 고안(경쟁 상태 예방)
    
    (2) 뮤텍스(Mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 -> 경쟁 상태 예방
    (3) Lock : 상호 배제를 위한 잠금(Lock)처리 -> 데이터 경쟁
    (4) 데드락(DeadLock) : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착상태)
    (5) Thread synchronization(스레드 동기화)를 통해서 안정적으로 동작하게 처리한다(동기화 메소드, 동기화 블럭)
    (6) Semaphore와 Mutex의 차이점은? 세마포어는 뮤텍스가 될수 있으나 뮤텍스는 세마포어가 될 수 없다.(세마포어가 하나일때)
        -> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용
        -> 뮤텍스 개체는 단일 스레드가 리소스 또는 중요 섹션을 소비하는 것을 허용
        -> 세마포어는 리소스에 대한 제한된 수의 동시 엑세스를 허용
'''

import logging
from concurrent.futures import ThreadPoolExecutor
import time

class FakeDataStore:
    #공유 변수(value)
    def __init__(self):
        self.value = 0

if __name__ == "__main__":
    # logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info(f'Test update. Starting value is {store.value}')
    
    # With context시작
    with ThreadPoolExecutor(max_workers=2) as executor:
        for i in ['First', 'Second', 'Third']:
            executor.submit(store.update, i)
            
    logging.info(f'Testing update. Ending value is {store.value}')