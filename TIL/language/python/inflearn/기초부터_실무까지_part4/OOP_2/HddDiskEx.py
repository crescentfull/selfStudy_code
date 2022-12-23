# Disk, HddDisk 실행 파일
from HddDisk import *

if __name__ == "__main__":
    disk = Disk(500, 7200)
    hddDIsk = HddDisk(32, 500)

    print(disk.showPrint())
    print(hddDIsk.showPrint())