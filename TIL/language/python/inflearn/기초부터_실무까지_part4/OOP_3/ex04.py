# 2.메서드의 다형성
class SalesWorker:
    def __init__(self, name):
        self.__name = name
    def work(self):
        print(self.__name, "물건을 팝니다")
        
class DevWorker(SalesWorker):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name
    def work(self):
        print(self.__name, "물건을 개발합니다.")
        
if __name__ == "__main__":
    employee1 = SalesWorker("알바1")
    employee2 = SalesWorker("알바2")
    employee3 = SalesWorker("알바3")
    employee4 = SalesWorker("알바4")
    dev1 = DevWorker("개발자1")
    dev2 = DevWorker("개발자2")
    dev3 = DevWorker("개발자3")
    dev4 = DevWorker("개발자4")
    
    workers = [employee1,employee2,employee3,employee4,dev1,dev2,dev3,dev4]
    print(workers)
    for worker in workers:
        worker.work()
'''
>>> 
알바1 물건을 팝니다
알바2 물건을 팝니다
알바3 물건을 팝니다
알바4 물건을 팝니다
개발자1 물건을 개발합니다.
개발자2 물건을 개발합니다.
개발자3 물건을 개발합니다.
개발자4 물건을 개발합니다.
# 인스턴스의 타입에 따라 
'''