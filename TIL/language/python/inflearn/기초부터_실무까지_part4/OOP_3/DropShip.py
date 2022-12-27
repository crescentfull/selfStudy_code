# 자식클래스 DropShip 클래스 정의
from Unit import *

class DropShip(Unit):
    mode = ""
    
    # 부모클래스 추상메서드 오버라이딩
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"드랍쉽의 위치 : {self.x}, {self.y}로 이동")
        
    # 드랍쉽 고유기능 추가
    def load(self):
        self.mode = "탑승모드 : 유닛 탑승"
        print(self.mode)
    def unload(self):
        self.mode = "탑승모드 : 유닛 하강"
        print(self.mode)
