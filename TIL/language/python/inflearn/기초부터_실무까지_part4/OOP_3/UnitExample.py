# Unit, Tank, DropShip, Marine 클래스 실행파일
from Tank import *
from DropShip import *
from Marine import *

if __name__ == "__main__":
    print("-"*40)
    tank = Tank()
    tank.move(100,300)
    tank.siegeMode()
    tank.stop('탱크',1,2)
    print("-"*40)
    marine = Marine()
    marine.move(1,4)
    marine.stimPack()
    marine.stop('marine',1,2)
    print("-"*40)
    dropShip = DropShip()
    dropShip.move(333,444)
    dropShip.load()
    dropShip.unload()
    dropShip.stop('드랍쉽',1,2)
    print("-"*40)