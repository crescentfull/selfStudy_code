# phone 클래스 정의(조상클래스)
# 모든 클래스의 최고 조상클래스는 object 클래스이다
class Phone:
    # 멤버 8개
    # 생성자
    def __init__(self):
        self.model = ""
        self.color = ""
    
    # 메서드 정의
    def powerOn(self):
        print("전원 ON")
    def powerOff(self):
        print("전원 OFF")
    def bell(self):
        print("ring ring ring~")
    def sendVoice(self, msg):
        print(f"me : {msg}")
    def receiveVoice(self, msg):
        print(f"other : {msg}")
    def hangUp(self):
        print(f"Drop OFF")