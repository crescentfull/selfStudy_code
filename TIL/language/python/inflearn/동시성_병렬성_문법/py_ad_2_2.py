'''
Section 2
Parallelism with Multiprocessing - multiprocessing(1) - Join, is_alive
keyword - multiprocessing, processing state
'''

from multiprocessing import Process
import time, logging

def proc_func(name):
    print(f'Sub-Process {name}: starting')
    time.sleep(3)
    print(f'Sub-Process {name}: finished')

def main():
    # logging format 
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    # 함수 인자 확인
    p = Process(target=proc_func, args=('First',))
    
    logging.info('Main-Process: before creating Process')
    
    #프로세스
    p.start()
    logging.info('Main-Process: During Process')
    
    logging.info('Main-Process: Terminated Process') 
    p.terminate() # sub process kill
    
    logging.info('Main-Process: Joined Process')
    p.join()
    
    # 상태확인
    print(f'Process p is alive: {p.is_alive()}')
if __name__ == '__main__':
    main()