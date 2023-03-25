'''
Section 2
Parallelism with Multiprocessing - multiprocessing(5) - Queue, Pipe
Keyword - Queue, Pipe, Communications between processes
'''

# 프로세스 통신 구현 Queue
from multiprocessing import Process, Queue, current_process
import time, os

def worker(id, baseNum, q):
    pass
def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpgid()
    print(f'Parent process ID{parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = []
    
    # 시작시간
    start_time = time.time()
    
    # Queue 선언
    q = Queue()

    for i in range(10):
        t = Process(name=str(i), target=worker, args=(1, 100000, 1))
        
        # 배열담기
        processes.append(t)
        
        # 시작
        t.start()
        
    for process in processes:
        process.join()
        
    # 순수 계산시간
    print(f"--- {time.time() - start_time} seconds ---")
    
    # 종료
    q.put('exit')
    
    # 대기
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
        
if __name__ == "__main__":
    main()