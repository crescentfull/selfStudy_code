from Tv import *

if __name__ == "__main__":
    #인스턴스 생성
    tv1 = Tv()
    tv2 = Tv()
    # 인스턴스의 필드와 메서드를 tv1 인스턴스명(참조변수)조작을 하고 있다.
    tv1.color = "black"
    tv1.powerTv(True, "tv1")
    tv1.channelUp(9, "tv1")
    tv1.volumeUp(25, "tv1")
    tv1.printTv("tv1")
    tv1.channelUp(-100,"tv1")
    tv1.powerTv(False, "tv1")
    tv1.volumeUp(30,"tv1")
    
    print("-"*30)
    
    tv2.color = "white"
    tv2.powerTv(True, "tv2")
    tv2.channelUp(9, "tv2")
    tv2.volumeUp(25, "tv2")
    tv2.printTv("tv2")
    tv2.channelUp(-100,"tv2")
    tv2.powerTv(False, "tv2")
    tv2.volumeUp(30,"tv2")