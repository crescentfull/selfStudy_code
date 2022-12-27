from ContentSender import *

class KakaoSender(ContentSender):
    content = ""
    def __init__(self, title, name, content):
        # 부모클래스 생성자 호출
        super().__init__(title, name)
        self.content = content
    # 조상클래스의 멤버인 추상메서드를 오버라이딩 한 것
    # kakaoSender 클래스는 인스턴스를 생성할 수가 있다.
    def sendMsg(self, recipient):
        print("제목 = ", self.title)
        print("이름 = ", self.name)
        print("내용 = ", self.content)
        print("받는사람 = ", recipient)