# 추상클래스 실습
'''

'''

from abc import *

class ContentSender(metaclass=ABCMeta):
    # 추상클래스라고 하여도 추상메서드의 목록만 존재해야 될 이유는 전혀없다
    # 추상클래스도 멤버변수, 생성자, 추상메서드를 가질 수 있다.
    title = ""
    name = ""
    # 생성자
    def __init__(self, title, name):
        self.title = title
        self.name = name
        
    @abstractclassmethod
    def sendMsg(self, recipient):
        pass
    
# cs = ContentSender("ㅁ","ㅇ")
# TypeError: Can't instantiate abstract class ContentSender with abstract method sendMsg