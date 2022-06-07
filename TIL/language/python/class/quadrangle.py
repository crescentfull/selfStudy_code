class Quadrangle:
    def __init__(self, width, height, color):
        self.width  = width
        self.height = height
        self.color  = color
        
    def get_area(self):
        return self.width * self.height
    
    def set_area(self, data1, data2):
        self.width  = data1
        self.height = data2

sqaure1 =  Quadrangle(1, 2, 'blue')
sqaure2 =  Quadrangle(3, 4, 'red')
sqaure1.set_area(10, 5)
sqaure2.set_area(7, 7)
sqaure1.color = 'red'
sqaure1.color = 'blue'

print(sqaure1.get_area())
print(sqaure2.get_area())