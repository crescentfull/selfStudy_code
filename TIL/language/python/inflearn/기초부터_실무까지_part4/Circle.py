import math

class Circle:
    
    __radius = 0
    
    def __init__(self, radius):
        self.__radius = radius
        print("매개변수가 있는 생성자 호출")
    
    def getRadius(self):
        return self.__radius
    def setRadius(self):
        return self.__radius
        
    def circleRound(self):
        circleRound = round(self.__radius * 2 * math.pi, 2)
        return circleRound
    def circleArea(self):
        circleArea = round(self.__radius * self.__radius * math.pi, 2)
        return circleArea
    
    def __str__(self):
        print("원의 반지름 : ", self.__radius)
        