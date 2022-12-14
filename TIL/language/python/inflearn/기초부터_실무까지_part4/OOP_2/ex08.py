# 클래스의 상속 :  조상(부모, 슈퍼)클래스의 멤버(필드, 메서드, 생성자제외)를 그대로 자손(자식, 서브)클래스가 물려받아 새로운 클래스를 만드는 것
# 조상클래스의 멤버가 추가, 삭제, 수정이 되면 조상클래스에 영향을 끼치지 아니한다.
# 자손클래스로 내려가면 갈수록 멤버의 갯수가 많아지고 반대로 조상클래스로 올라가면 멤버의 갯수가 적어진다

# 조상클래스
class Car:
    # 조상클래스의 멤버는 2개이다
    speed = 0
    
    def upSpeed(self, speed):
        self.speed = speed
        print(f"현재속도(조상클래스) : {self.speed}")
        
# 자식클래스
class Sedan(Car):
    pass

if __name__ == "__main__":
    sedan = Sedan()
    sedan.upSpeed(100)