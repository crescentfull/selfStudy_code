##클래스 사용 예제
class 클래스이름 :
    #클래스 생성자 정의
    def __init__(self, 인자1, 인자2) :
        self.필요한속성1 = 인자1
        self.필요한속성2 = 인자2
        
        #필요한 메소드 구현
        def 필요한_메소드1(self):
            코드구현
            
        def 필요한_메소드2(self):
            코드구현
            
## 메인코드영역
c1 = 클래스이름(c1의 인자1, c1의 인자2)
c2 = 클래스이름(c2의 인자1, c2의 인자2)

#메소드 사용하여 인스턴스 활용
c1.필요한_메소드1()
c2.필요한_메소드1()

c1.필요한_메소드2()
c2.필요한_메소드2()