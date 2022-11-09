# 2차원 리스트에 대한 실습
# 3행 5열의 2차원 리스트
double_list = [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15] 
              ]

print(double_list)
print(double_list[0][1])

# 리스트 주소값 출력
print(id(double_list))
print(id(double_list[0]))
print(id(double_list[1]))
print(id(double_list[2]))
print(id(double_list[0][0]))
print(id(double_list[1][0]))
print(id(double_list[2][0]))

#가변배열
double_list2 = [
                [1,2,3,4,5],
                [6,7,10],
                [11,12,14,15] 
              ]
print(len(double_list2))
print(len(double_list2[0]))
print(len(double_list2[1]))
print(len(double_list2[2]))

# 2차원 리스트 출력
# 더블루프 필수.
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        print(double_list[i][j], end="\t") #tap띄우기
    print()# 줄바꿈
    

# 2차원 리스트는 정적인 것 보다는 동적으로 생성하는 경우가 훨씬 많다.
rows = int(input("원하는 행을 입력해주세요 : "))
cols = int(input("원하는 열을 입력해주세요 : "))
dbl_list = []
for row in range(rows):
    dbl_list += [[0]*cols]
print(dbl_list)
dbl_list_comp = [([0]*cols) for row in range(rows)]
print(dbl_list_comp)

# 행의 합계
double_list = [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15] 
              ]
sum = 0
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        sum += double_list[i][j]
print("double_list 전체 합계 : ", sum)