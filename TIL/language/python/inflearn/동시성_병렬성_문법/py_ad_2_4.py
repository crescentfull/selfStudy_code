'''
Section 2
Parallelism with Multiprocessing - multiprocessing(3) - ProcessPoolExecutor
Keyword - ProcessPoolExecutor, as_completed, futures Object, timeout, dict
'''
from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 urls
URLS = [
    'http://www.daum.net/',
    'http://www.naver.com/',
    'http://www.cnn.com/',
    'http://www.google.com/',
    'http://www.youtube.com/',
]

# 실행함수
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

def main():
    # 프로세스풀 context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # Future 로드(실행x, 적재하는거)
        future_to_url = {executor.submit(load_url, url, 60):  url for url in URLS}
        
        for future in as_completed(future_to_url): # timeput=1
            # key 값이 Future 객체
            url = future_to_url[future] # == future_to_url.get() ? dict이라서
            
            try:
                # 결과
                data = future.result()
            except Exception as exc:
                # 예외처리
                print(f'{url} generated an exception: {exc}')
            else:
                # 결과확인
                print(f'{url} page is {len(data)} bytes')
if __name__ == '__main__':
    main()