'''
Section 3
Concurrency, CPU Bound VS I/O Bound - Blocking I/O VS Non-Blocking I/O
Keyword - Blocking I/O, Non-Blocking I/O, Sync, Async
'''

'''

Blocking I/O VS Non-Blocking I/O

    blocking I/O
    - 시스템 콜 요청시 -> 커널 IO 작업 완료시까지 응답 대기   # 커널 : OS
    - 제어권(IO 작업) -> 커널 소유 -> 응답(Response)전 까지 대기(Block) -> 다른 작업 수행이 불가(대기상태)
    
    Non-blocking I/O
    - 시스템 콜 요청시 -> 커널 IO 작업 완료 여부에 상관없이 즉시 응답
    - 제어권(IO 작업) -> 유저 프로세스 -> 다른 작업 수행 가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료 여부 확인
    
    Async VS Sync
    
        Asnc : IO 작업 완료 여부에 대한 Notification은 커널(호출되는 함수) - > 유저프로세스(호출하는 함수) # Async non-blocking IO 중요
        Sync : IO 작업 완료 여부에 대한 Notification은 유저프로세스(호출하는 함수) -> 커널(호출되는 함수)

'''