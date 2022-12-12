# none 참조값 : 변수가 아무 것도 가리키고 있지 않다면 none으로 초기화를 해주는 것이 권장사항
# 모든 변수는 초기화를 해주는 것이 제일 좋다.
# none(c랑 java는 null) 은 아무것도 참조하지 않고 있다는 특별한 값

class TV:
    power = False
    volume = 0
    channel = 0
    
    def __init__(self, power, channel, volume):
        self.power = power
        self.channel = channel
        self.volume = volume
        
    def powerTV(self, power):
        self.power = not power
        
    def __str__(self):
        print(self.power)
        print(self.volume)
        print(self.channel)
if __name__ == "__main__":
    tv = None
    print(tv) # 결과가 none 나온다
    # AttributeError TV가 없는데 어떻게 power()를 호출할 수 있을까
    tv = TV(True, 10, 25)
    tv.__str__()
    tv.powerTV(True)