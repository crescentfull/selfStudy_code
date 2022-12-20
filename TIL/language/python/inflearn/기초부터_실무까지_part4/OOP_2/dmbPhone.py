# Phone class 자식
from phone import *

class DmbPhone(Phone):
    # 멤버 12개(phone것도 포함)
    # 생성자
    def __init__(self, model, color, channel):
        # 부모클래스 생성자 호출 2가지 방법
        # super().__init__()
        Phone.__init__(self)
        self.model = model
        self.color = color
        self.channel = channel

    # 메서드 추가
    def trunOnDmb(self):
        print(f'채널 : {self.channel}번 방송수신 시작')
    def turnOffDmb(self):
        print(f'채널 수신 종료')
    def changeChannelDmb(self, channel):
        print(f'채널 : {channel}번으로 채널 변경')
    