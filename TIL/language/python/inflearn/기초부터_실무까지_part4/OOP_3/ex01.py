# 클래스 다중상속 실습
'''
다중상속 : 여러 부모클래스로부터 상속을 받아서 새로운 클래스를 만드는 것
부모클래스를 몇 개를 상속받아도 상관은 없지만 그러지말자
문제점
1. 다중상속을 하다보면 부모클래스에서 같은 이름을 가진 멤버가 존재할수 있기 때문에 충돌성을 배제할 수가 없다.
2. 하나의 조상클래스를 두번 이상 상속을 받을 가능성이 높다
파이썬에서는 단일, 다중 상속을 지원한다.

'''

class Person(object):
    def __init__(self):
        pass
    def greeting(self):
        print("안녕하세요")

class University(object):
    def __init__(self):
        pass
    def manage_credit(self):
        print("학점관리를 합시다")
        
# 2개의 조상클래스를 상속받음
class Undergraduate(Person, University):
    def __init__(self):
        # 부모클래스를 2개 상속받았기 때문에 생성자도 각 부모클래스에 해당하는 부분을 호출해줘야함
        Person.__init__(self)
        University.__init__(self)
    def study(self):
        print("공부중")
        
if __name__ == "__main__":
    student = Undergraduate()
    student.greeting() # >>> 안녕하세요 / Person
    student.manage_credit() # >>> 학점관리를 합시다 / University
    student.study() # >>> 공부중 / Undergraduate