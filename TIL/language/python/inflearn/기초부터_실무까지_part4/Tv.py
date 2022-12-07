# 클래스 TV
class Tv:
    # 필드 선언
    color = ""      # 색깔
    power = False   # 전원
    channel = 0     # 채널
    volume = 0      # 볼륨
    
    # Tv 전원
    def powerTv(self, power, tv):
        self.power = power
        if self.power == True:
            print(f"{tv}의 전원이 켜졌습니다")
        else:
            print(f"{tv}의 전원이 꺼졌습니다.")

    # Tv의 채널 증가
    def channelUp(self, channel, tv):
        if channel <0:
            print("음수 불가")
            return
        if self.power == False:
            print(f"{tv} 전원을 키세요")
            return        
        self.channel += channel
        
    #Tv 채널 감소
    def channelDown(self, channel, tv):
        if channel <0:
            print("음수 불가")
            return
        if self.power == False:
            print(f"{tv}의 전원을 키세요")
            return
        self.channel -= channel

    #Tv 볼륨 증가
    def volumeUp(self, volume, tv):
        if volume <0:
            print("음수 불가")
            return
        if self.power == False:
            print(f"{tv} 전원을 키세요")
            return
        self.volume += volume
        
    #Tv 볼륨 감소
    def volumeDown(self, volume, tv):
        if volume <0:
            print("음수 불가")
            return
        if self.power == False:
            print(f"{tv} 전원을 키세요")
            return
        self.volume -= volume
        
    
    def printTv(self, tv):
        print(f"TV의 색상 : {tv},{self.color}")
        print(f"TV의 전원 : {tv},{self.power}") 
        print(f"TV의 채널 : {tv},{self.channel}")
        print(f"TV의 음량 : {tv},{self.volume}")