def add(*args):
    sum = 0
    print(type(args))
    for i in args:
        sum += i
    return sum

print(add(11,2,2,3,4,5,5))
print(type(add(1)))
def calculate(n, **kwargs):
    print(n, kwargs) # kwargs >>> 딕셔너리로 값 출력
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(5, add=3, multiply=5) 

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make") #kw["make"]
        self.model = kw.get("model") #kw["model"]
                        # get() 매개변수가 없을때 none값을 리턴한다. 오류발생 X
my_car = Car(make="nissan") #model="gtr"
print(my_car.model)