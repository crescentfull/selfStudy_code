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
        if num % start_num == 0:
            break 
    if num == start_num:
        print("소수  : ", start_num)
        sum += start_num
        print("합계 : ", sum)
        lastData = start_num
        print("마지막 소수 : ", lastData)
