'''
Section 3
Concurrency, CPU Bound vs I/O Bound - IO Bound(2) asyncio
Keyword - ascyncio
'''
'''

동시 프로그래밍 패러다임 변화
싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU 연산, DB연동, API 호출 대기 시간 늘어남
파이썬 3.4 -> 비동기(asyncio) 표준 라이브러리 등장

'''

import time 
import asyncio

# sync
def exe_calculate_sync(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calcualtiong.....')
        time.sleep(1)
    print(f'{name} : {n} working DONE!')

def process_sync():
    start = time.time()

    exe_calculate_sync('one',3)
    exe_calculate_sync('two',2)
    exe_calculate_sync('one',1)
    
    end = time.time()
    
    print(f'>>> total seconds : {end - start}')
    
# async
async def exe_calculate_async(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calcualtiong.....')
        await asyncio.sleep(1) #time.sleep(1)  ->> time 모듈은 비동기가 아니다. 이미 time 모듈안에서 def sleep() 이런식으로 동기로 설정되어 있기 때문이다. 따라서 await time.sleep()으로 사용 할 수 없다.
    print(f'{name} : {n} working DONE!')

async def process_async(): # 비동기로 실행 할때는 async를 붙인다. 
    start = time.time()
    
    # 비동기 함수내에서 함수를 호출하려면 await을 붙인다
    # 함수가 여러개이기 때문에 asyncio.wait([]) 리스트 함수로 묶어서 선언해준다.
    await asyncio.wait([
        exe_calculate_async('One', 3),
        exe_calculate_async('Two', 2),
        exe_calculate_async('Three', 1)
    ]) 

    
    end = time.time()
    
    print(f'>>> total seconds : {end - start}')
    
if __name__ == '__main__':
    # sync
    #process_sync()
    
    # async
    # python 3.7 이상
    asyncio.run(process_async())
    # 3.7 밑에 버전 
    # asyncio.get_event_loop().run_until_complete(process_async())