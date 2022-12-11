class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 특수 메소드 __add__() 정의 (2개 인스턴스 매개변수 )
    def __add__(self, other):
        # 인스턴스의 더하기 연산을 하고 해당하는 값을 가지고 새로운 인스턴스를 생성하여 리턴
        return Vector2D(self.x + other.x, self.y + other.y)
    
    # 특수 메소드 __sub__()
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    # 특수 메소드 __mul__() 정의
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    
    # 특수 메서드 __eq__()
    def __eq__(self, other):
        return Vector2D(self.x == other.x & self.y == other.y)
    # 인스턴스의 멤버변수들의 값을 출력
    # print(인스턴스명) >>> 자동으로 호출해줌
    def __str__(self):
        return f"{self.x}, {self.y}"

if __name__ == "__main__":
    v1 = Vector2D(5, 2)
    v2 = Vector2D(5, 3)
    v3 = Vector2D(5, 4)
    vector_result = v1 + v2
    print(vector_result.__str__())
    