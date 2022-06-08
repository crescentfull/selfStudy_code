class Car:
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        print(self.name)

class ElectronicCar(Car):
    def get_info(self):
        print(self.name, 'electronic')

class GasolinCar(Car):
    def get_info(self):
        print(self.name, 'gasolin')
        
eCar1 = ElectronicCar('ev6')
gCar1 = GasolinCar('g80')

eCar1.get_info()
gCar1.get_info()