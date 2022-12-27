from Unit import *

class Tank(Unit):
    mode = ""
    
    # 부모클래스 추상메서드 오버라이딩
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"탱크의 위치 : {self.x}, {self.y}로 이동")
        
    #탱크 고유기능 추가
    def siegeMode(self):
        self.mode = "공격모드 : 시즈모드 변환"
        print(self.mode)