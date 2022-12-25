# 다중상속 실습
class Person:
    def __init__(self):
        print("I'm human")

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("I'm student")

class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        print("I'm employee")