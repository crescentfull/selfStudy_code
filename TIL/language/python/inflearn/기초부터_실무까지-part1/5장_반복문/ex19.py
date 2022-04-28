#      *
#     ***
#    *****
#   *******
#  *********
# ***********



for i in range(1,6):
    for j in range(5-i): #공백
        print(" ",end="")
    for j in range(1,i*2):# 별표찍기
        print("*", end="")    
    print("")
    
# 2. format() 이용 풀이
print("-------------------")
for i in range(1, 11, 2):
    #중앙 정렬을 위해서는 ^ 특수문자를 사용하면 된다.
    print("{:^10}".format("*"*i))
    
# 3. 마름모만들기
for i in range(1,6):
    for j in range(5-i): #공백
        print(" ",end="")
    for j in range(1,i*2):# 별표찍기
        print("*", end="")    
    print("")
for i in range(4,0,-1):
    for j in range(5-i): #공백
        print(" ",end="")
    for j in range(1,i*2):# 별표찍기
        print("*", end="")    
    print("")