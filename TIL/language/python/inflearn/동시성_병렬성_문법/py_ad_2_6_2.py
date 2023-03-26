'''
Section 2
Parallelism with Multiprocessing - multiprocessing(5) - Pipe
Keyword - Pipe, Communications between processes
'''

# 프로세스 통신 구현 Queue
from multiprocessing import Process, Pipe, current_process
import time, os

def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 누적
    sub_total = 0

    # 계산
    for i in range(baseNum):
        sub_total += 1
    
    # Produce
    conn.send(sub_total)
    conn.close()
    # 출력
    print(f'Process ID: {process_id}, Process Name: {process_name}, ID: {id}')
    print(f'Result : {sub_total}')

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    print(f'Parent process ID: {parent_process_id}')
    
    # 시작시간
    start_time = time.time()
    
    # pipe 선언
    parent_conn, child_conn = Pipe()
    
    t = Process(name=str(1), target=worker, args=(1, 100000, child_conn))
        
        # 시작
    t.start()
        
    t.join()
    # 순수 계산시간
    print(f"--- {time.time() - start_time} seconds ---")

    print()
    
    print(f'Main-Processing Total Count={parent_conn.recv()}')
    print('Main-Processing Done!')
if __name__ == "__main__":
    main()