# 추상클래스 실습
# 부모클래스 정의
from abc import *

class Unit(metaclass=ABCMeta):
    x = 0
    y = 0
    name = ""
    
    @abstractclassmethod
    def move(self, x, y):
        pass
    
    def stop(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name
        print(f"현재 위치 : {self.x}, {self.y}에 {self.name}이(가) 멈춤니다")