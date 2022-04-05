##상황  : 자라는 아이들의 키를 관리하는 
class Child :
    #클래스 생성자 정의
    def __init__(self, Child_name, Child_height) :
        self.name = Child_name
        self.height = Child_height
        
        #필요한 메소드 구현
        def getName(self) :
            return self.name # 이름 정보를 반환
        
        def getHeight(self) :
            return self.height #키 정보를 반환
        
        def growHeight(self, add) :
            temp=self.height #임시 지역변수. 성장전 키값 저장
            self.height += add
            print("성장했습니다. {}->{}".format(temp,self.height)) #성장결과 출력
            
##메인 코드 영역

#어린이 인스턴스 2개 생성
c1 = Child('Tom',150) #Child_name => Tom, Child_height => 150
c2 = Child('Jerry',100) #Child_name => Jerry, Child_height => 100

##메소드 사용하여 인스턴스 활용
#1. 현재 이름과 키 정보를 조회
print("현재 {}의 키는 {}cm 입니다.".format(c1.getName(), c1.getHeight()))
print("현재 {}의 키는 {}cm 입니다.".format(c2.getName(), c2.getHeight()))

#2. 키 성장
c1.growHeight(10) #growHeight의 매개변수 add값을 10 넣어줌
c2.growHeight(30) 

#3. 현재 이름과 키 정보 조회
print("현재 {}의 키는 {}cm 입니다.".format(c1.getName(). c1.getHeight()))
print("현재 {}의 키는 {}cm 입니다.".format(c2.getName(). c2.getHeight()))
