# Monitor class 이용

from Monitor import *

if __name__ == "__main__":
    # 매개변수가 있는 생성자를 호출하는 방법
    # company, inch, price, color
    monitor1 = Monitor("lg",32,3000000,"white")
    monitor1.__str__()
    
    print("-"*40)
    # setter 메서드를 통해서 기존에 생성자로 생성했던 값을 변경하고 있다.
    monitor1.setCompany("삼성")
    monitor1.setInch(27)
    monitor1.setPrice(150000)
    monitor1.setColor("black")
    monitor1.__str__()
