'''
Sction 1
Multithreading - Python's GIL
Keyword - CPython, 메모리관리, GIL 사용이유
'''
'''

GIL(Global Interpreter Lock)
    남아있는 이유?
    멀티스레드로 사용할때랑 싱글스레드를 사용했을 때를 비교해보니, 싱글스레드가 더 빨랐다. 그러니까 GIL를 사용해서 멀티스레드 제한을 걸어두겠다.
    싱글스레드에서 성능이 저하된다면, 그런 구현은 파이썬에 넣지 않는게 맞다. - 귀도 반 로섬

    (1) CPython -> Python(bytecode) 실행 시 여러 thread(멀티스레드) 사용할 경우 
        단일 스레드 만이 Python object에 접근하게 제한하는 mutex
    (2) Cpython 메모리 관리가 취약하기 때문에(즉, thread-safe)
    (3) 단일 스레드로 충분히 빠르다.
    (4) 프로세스 사용 가능(Numpy/Scipy)등 GIL 외부 영역에서 효율적인 코딩이 가능하도록 라이브러리 혹은 패키지가 존재
    (5) 병렬 처리는 Multiprocessing, asyncio 사용 가능, 선택지 다양
    (6) thread 동시성을 완벽하게 처리하기 위해 Jython(python문법을 java에서 실행시키는 문법), IronPython, Stackless Python 등이 존재

'''