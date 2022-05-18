# 소수를 2부터 계속 더할 때, 2000보다 작은 최대합은 얼마이고,
# 마지막으로 더해지는 소수는 얼마인지를 출력
# 중첩루프, 조건식 사용

from tracemalloc import start


start_num = 0
num = 0
sum = 0
lastData = 0

# for num in range(1,2001):
#     if num%2 == 0:
#         sum += num
#     num+=1
# print(sum)

for num in range(2,2001):
    for start_num in range(2,num+1):
        # 배수/소수 걸러주는 조건식
        if num % start_num == 0:
            break 
    # 아래 조건이 참이다라는 것은 자기 자신으로 나눠서 나머지가 0이 나왔기 때문에 '소수'라는 것임으로 루프 실행 가능
    if num == start_num:
        print("소수  : ", start_num)
        sum += start_num
        print("합계 : ", sum)
        lastData = start_num
        print("마지막 소수 : ", lastData)
