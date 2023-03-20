'''
Section 2
Parallelism with Multiprocessing - multiprocessing(4) - Sharing state
Keyword - memory sharing, array, value
'''

from multiprocessing import Process, current_process, Value, Array # 데이터가 공유하는 패키지는 엄격하게 선언해줘야한다
import os

# 프로세스 메모리 공유 예제 (공유 ok)

# 실행함수
def generate_update_number(v: int):
    for _ in range(50):
        v.value += 1
    print(current_process().name, 'data', v.value)

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent process ID {parent_process_id}')
    
    # 리스트 선언
    processes = []
    
    # 프로세스 메모리 공유 변수
    # from multiprocess import shared_memory 사용가능 (3.8이상)
    # from multiprocess import Manager 사용가능
    # share_numbers = Array('i',range(50))
    share_value = Value('i',0)  # -> 다른 사람도 쉽게 알아볼수 있도록 명시적으로 해두는것을 권장
    for _ in range(1,10):
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        # 배열에 담기
        processes.append(p)
        # 실행
        p.start()
    
    # join
    for p in processes:
        p.join()
    # 최종 프로세스 부모 변수 확인 (공유되는지 확인)
    print('share_value : ', share_value)
if __name__ == '__main__':
    main()
