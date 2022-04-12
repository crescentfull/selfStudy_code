# 안녕하세요 5번 출력해보라
cnt = 0
for x in range(5):
    cnt += 1
    print("hi")
print("마지막 횟수 : ", cnt)
print("-----------------------------")
# x 는 루프변수, In 뒷부분은 시퀀스
# 시퀀스에 올수 있는 것은, 문자열 혹은 리스트이다
for x in [0,1,2,3,4]:
    print("안녕하세요")

# end=" " 
for x in range(5):
    print(x, end=" ")