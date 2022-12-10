from Person import *

if __name__ == "__main__":
    # 기본생성자 호출
    person1 = Person()
    person1.__str__()
    
    print("-"*30)
    
    person2 = Person()
    person2.__str__()
    
    print("-"*30)

    print("-"*30)
    print("person1")
    # print(id(person1))
    # print(id(person2))
    print(person1.getName())
    person1.setName("김길동")
    person1.age = 50
    print("person1.name : ", person1.getName())
    print("person1.address : ", person1.getAddress())
    print("person1.age : ", person1.getAge())