'''
Section 3
Concurrency, CPU Bound VS I/O Bound - What is Concurrency
Keyword - Concurrency
'''

'''

Concurrency(동시성)

    - CPU 가용성 극대화를 위해서 Paralleism의 단점 및 어려움을 소프트웨어(구현)레벨에서 해결하기 위한 방법
    - 싱클코어에 멀티스레드 패턴으로 작업을 처리
    - 동시 작업에 있어서 일정량 처리 후 다음 작업으로 넘어가는 방식
    - 즉, 제어권 주고 받으며 작업을 처리하는 패턴, 병렬적은 아니나, 유사한 처리 방식이다

Concurrency(동시성) VS Parralleism(병렬성)

    동시성 : 논리적, 
            동시 실행 패턴(논리적), 싱글코어, 멀티 코어에서 실행가능, 한 개의 작업에서 공유 처리, 
            BUT! 디버깅이 매우 어렵다. Mutex, Deadlock
    병렬성 : 물리적,
            물리적으로 동시 실행, 멀티코어에서 구현가능, 주로 별개의 작업 처리할 때 활용
            BUT! 디버깅이 어렵다
            OpenMP, MPI, CUDA

'''