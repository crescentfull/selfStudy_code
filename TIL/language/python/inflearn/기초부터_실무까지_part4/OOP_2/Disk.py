# 부모클래스 정의
class Disk(object):
    capacity = 0
    rpm = 0
    
    def __init__(self, capacity, rpm):
        self.__capacity = capacity
        self.__rpm = rpm
        
    def getCapacity(self):
        return self.__capacity
    def getRpm(self):
        return self.__rpm 
    
    def showPrint(self):
        return "디스크의 용량은 " +str(self.__capacity)+"gb 이며"\
                "rpm은 "+ str(self.__rpm)+"이다."