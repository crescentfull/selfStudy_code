'''
Section 3
Concurrency, CPU Bound vs I/O Bound(3) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, requests, multiprocessing
'''
import multiprocessing
import requests, time

# I/O 바운드 멀티프로세싱

# 쓰레드보다 프로세스가 비용이 더 높다
# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행 할 때 마다 객체 생성은 좋지 않음 -> 각 프로세스마다 할당

session = None

def set_global_session():
    global session # 객체를 미리 전역변수로 만들어두면 함수 실행할때마다 객체생성을 하지 않아도 되기 때문에 실행속도가 조금이라도 향상된다.
    if not session:
        session = requests.Session()
    
# 실행함수1(다운로드)
def request_site(url):
    # 세셕 획득
    #  
    
    #세션확인
    print(session)
    
    with session.get(url, verify=False) as response:
        name = multiprocessing.current_process().name
        print(f'[{name} -> Read Contents: {len(response.content)}, Status Code : {response.status_code} from {url}]')

# 실행함수2(요청)
def request_all_sites(urls):
    # 멀티프로세싱 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)
    
def main():
    # 테스트 URLS
    urls = [
        "https://www.jython.org",
        "https://www.naver.com",
        "https://yahoo.com"
    ]*3
    
    # 실행시간 측정
    start_time = time.time()
    
    # 실행
    request_all_sites(urls)
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    # 결과
    print(f'Downloaded {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()
