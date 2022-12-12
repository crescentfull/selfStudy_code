class Character:
    # 상수값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30
    
    def __init__(self):
        self.__hp = Character.NORMAL
        
    def levelUp(self):
        self.__hp = Character.STRONG
    
    def damage(self):
        self.__hp = Character.WEAK
        
    def getHp(self):
        return self.__hp
    
    # __str__() 은 문자열을 리턴하게 해주는 것이 주 목적
    def __str__(self):
        return "HP : " + str(self.__hp)

        
if __name__ == "__main__":
    ch = Character()
    print(ch)
    ch.levelUp()
    print(ch)
    ch.damage()
    print(ch)