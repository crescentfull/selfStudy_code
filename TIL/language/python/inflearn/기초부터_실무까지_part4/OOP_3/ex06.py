# 추상클래스 
'''
추상클래스 : 클래스안에 최소 추상메서드가 1개이상 존재하면 그 클래스를 추상클래스다라고 함
abc(abstract base class) 모듈을 이용
@abstractmethod 어노테이션을 추상메서드 위에 붙여준다
# 추상메서드는 선언부만 존재하고 구현부는 없는 메서드 이다
추상클래스는 인스턴스를 절대! 생성할 수가 없다.
'''
from abc import *

class StudentBase(metaclass=ABCMeta):
    # 아래 어노테이션은 인터프리터에게 strudy 메서드가 추상메서드
    # 체크하라는 명령을 줌
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        pass

# Student 클래스는 인스턴스를 만들 수 없다. 그 이유는 추상메서드 1개를 재정의하지 않기 때문이다.
class Student(StudentBase):
    def study(self):
        print("공부 합니다")
class Student1(Student):
    def go_to_school(self):
        print("학교를 갑니다")

if __name__ == "__main__":
    # 추상클래스를 절대 인스턴스를 생성할 수 없다
    # 상속을 통해서 자식클래스에 추상메서드를 전부 오버라이딩을 했을때 인스턴스 생성이 가능하다!
    # student = StudentBase()
    # >>> TypeError: Can't instantiate abstract class StudentBase with abstract methods go_to_school, study
    student1 = Student1()
    student1.study()
    student1.go_to_school()
    
    # 추상클래스의 용도 : 추상클래스를 상속받는 각각의 자식클래스에서 다른 내용으로 구현될 것을 예상하고 뼈대(가이드라인)만 만든다
    '''
    예) 추상클래스에 play() 추상메서드가 존재한다면 mp3, cdplayer, lp, tapeplayer 클래스에 play()메서드가 다 존재할 것,
    play() 메서드는 선언부만 같은 내용으로 오버라이딩이 되어 다른결과를 만들어 줄수 있다.
    '''