from Disk import *
# 자식 클래스 정의
class HddDisk(Disk):
    __capacity = 0
    __rpm = 0 
    
    def __init__(self, capacity, rpm):
        Disk.__init__(self, 1, 5)
        self.__capacity = capacity
        self.__rpm = rpm
        
    def getCapacity(self):
        return self.__capacity
    def getRpm(self):
        return self.__rpm
    
    def showPrint(self):
        # 내꺼 출력
        return "HDD 디스크의 용량은 " +str(self.__capacity)+"gb 이며"\
                "rpm은 "+ str(self.__rpm)+"이다."
        # # 부모클래스 출력
        # return "HDD 디스크의 용량은 " +str(super().getCapacity())+"gb 이며"\
        #         "rpm은 "+ str(super().getRpm())+"이다."