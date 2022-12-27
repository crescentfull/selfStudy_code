# 자식클래스 Marine 클래스 정의
from Unit import *

class Marine(Unit):
    mode = ""
    
    # 부모클래스 추상메서드 오버라이딩
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"마린의 위치 : {self.x}, {self.y}로 이동")
        
    # 드랍쉽 고유기능 추가
    def stimPack(self):
        self.mode = "공격모드 : 광폭화"
        print(self.mode)
