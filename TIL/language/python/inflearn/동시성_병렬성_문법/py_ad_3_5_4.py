'''
Section 3
Concurrency, CPU Bound vs I/O Bound(3) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, requests, multiprocessing, asyncio
'''
import time
import asyncio
import aiohttp

# IO bound Asyncio 예제
# threading 보다 높은 코드 복잡도 -> async , await 적절하게 코딩

# 실행함수1(다운로드)
async def request_site(session, url):
    # 세셕 획득
    #  
    
    #세션확인
    print(session)
    
    async with session.get(url) as response:
        print(f'Read Contents {0}, from {1}'.format(response.status_code, url))

# 실행함수2(요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            #태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)
            
        # task 확인
        print(*tasks)
        print(tasks)
        
        await asyncio.gather(*tasks, return_exceptions=True)
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
    asyncio.run(request_all_sites(urls))
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    print()
    
    # 결과
    print(f'Downloaded {len(urls)} sites in {duration} seconds')
    
if __name__ == "__main__":
    main()
