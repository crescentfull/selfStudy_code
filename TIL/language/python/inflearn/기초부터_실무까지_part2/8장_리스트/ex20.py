# 2차원 리스트 체커보드 형태
# 출력 함수
def printList(li):
    for row in range(len(li)):
        for col in range(len(li[row])):
            print(li[row][col], end=" ")
        print() # 줄바꿈
# 2차원 리스트를 체커보드 형태로 초기화하는 함수
def init(li):
    for row in range(len(li)):
        for col in range(len(li[row])):
            if (row+col)%2 == 0:    #(row+col)이 짝수이면 1을 지정
                li[row][col] = 1

if __name__ == "__main__":
    table = []
    for row in range(10):
        table += [[0]*10]
    init(table)
    printList(table)